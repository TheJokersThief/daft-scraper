import json
import sys
from bs4 import BeautifulSoup
from enum import Enum
from typing import List, Callable

from daft_scraper import Daft
from daft_scraper.listing import Listing, ListingSchema
from daft_scraper.search.options import Option, PriceOption, SalePriceOption


def empty_post_process_hook(listing: Listing, raw_data: dict) -> Listing:
    return listing


class SearchType(Enum):
    RENT = "property-for-rent"
    SALE = "property-for-sale"
    SHARE = "sharing"
    NEW_HOMES = "new-homes-for-sale"
    COMMERCIAL_RENT = "commercial-properties-for-rent"
    COMMERCIAL_SALE = "commercial-properties-for-sale"


class DaftSearch():
    PAGE_SIZE = 20
    SALE_TYPES = [SearchType.SALE, SearchType.NEW_HOMES, SearchType.COMMERCIAL_SALE]

    def __init__(self, search_type: SearchType, post_process_hook: Callable = empty_post_process_hook):
        self.search_type = search_type
        self.post_process_hook = post_process_hook
        self.site = Daft()

    def search(self, query: List[Option], max_pages: int = sys.maxsize, page_offset: int = 0):
        path = self._build_search_path()

        # Convert options to their string form
        options = self._translate_options(query)

        # If only one location is specified, it should be in the URL, not the params
        locations = options.get('location', [])
        if len(locations) == 1:
            path = path.replace('ireland', locations[0])
            del options['location']

        # Init pagination params
        options['pageSize'] = self.PAGE_SIZE
        options['from'] = self._calc_offset(page_offset)

        # Fetch the first page and get pagination info
        page_data = self._get_page_data(path, options)
        totalPages = page_data['props']['pageProps']['paging']['totalPages']
        current_page = 0

        while current_page < min(totalPages, max_pages):
            listing_data = page_data['props']['pageProps']['listings']
            yield from self._get_listings(listing_data)

            options['from'] = self._calc_offset(current_page)
            page_data = self._get_page_data(path, options)
            current_page = page_data['props']['pageProps']['paging']['currentPage']

    def _build_search_path(self):
        """Build the URL path for searches"""
        return "/".join([self.search_type.value, "ireland"])

    def _translate_options(self, query):
        """Convert options into dict[str:str] form"""
        options = {}
        for option in query:
            if isinstance(option, PriceOption) and self.search_type in self.SALE_TYPES:
                # If the search is a sale type, translate the price option
                option = SalePriceOption(option.min, option.max)

            options = {**options, **option.get_params()}
        return options

    def _extract_json(self, page_html: BeautifulSoup):
        """Extract the JSON script tag and parse it for a page"""
        script_text = page_html.find('script', {'id': '__NEXT_DATA__'})
        return json.loads(script_text.string)

    def _get_page_data(self, path, params):
        """Request a page and parse its JSON"""
        page = self.site.get(path, params=params)
        return self._extract_json(page)

    def _get_listings(self, listings: dict):
        """Convert a dict of listings into marshalled objects"""
        for listing in listings:
            yield self.post_process_hook(
                Listing(ListingSchema().load(listing['listing'])),
                listing
            )

    def _calc_offset(self, current_page: int):
        """Calculate the offset for pagination"""
        return self.PAGE_SIZE * current_page
