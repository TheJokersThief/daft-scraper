import sys
import typer
from tabulate import tabulate
from typing import List

from daft_scraper.search import SearchType, DaftSearch
from daft_scraper.search.options import (
    PriceOption, BedOption, LeaseLengthOption, PropertyType, PropertyTypesOption,
    Facility, FacilitiesOption, MediaType, MediaTypesOption, AdState,
    AdStateOption, Sort, SortOption, Furnishing, FurnishingOption
)
from daft_scraper.search.options_location import LocationsOption, Location


app = typer.Typer()


@app.command()
def search(
    search_type: SearchType,
    headers: List[str] = ['id', 'price', 'title', 'propertyType', 'url'],
    location: List[str] = [Location.ALL.value],
    max_pages: int = sys.maxsize,
    min_price: int = 0,
    max_price: int = sys.maxsize,
    min_beds: int = 0,
    max_beds: int = sys.maxsize,
    min_lease: int = 0,
    max_lease: int = sys.maxsize,
    property_type: List[PropertyType] = [PropertyType.ALL.value],
    ad_state: AdState = AdState.AVAILABLE.value,
    facility: List[Facility] = [Facility.NONE.value],
    media_type: List[MediaType] = [MediaType.ALL.value],
    sort: Sort = Sort.BEST_MATCH.value,
    furnishing: Furnishing = Furnishing.ALL_FURNISHINGS.value
):
    location = [Location(location) for location in location]
    options = [
        LocationsOption(location),
        PriceOption(min_price, max_price),
        BedOption(min_beds, max_beds),
        PropertyTypesOption(property_type),
        AdStateOption(ad_state),
        FacilitiesOption(facility),
        MediaTypesOption(media_type),
        SortOption(sort),
        FurnishingOption(furnishing),
        LeaseLengthOption(min_lease, max_lease),
    ]

    api = DaftSearch(search_type)
    listings = api.search(options, max_pages)

    table_data = []
    for listing in listings:
        row = [getattr(listing, header, "") for header in headers]
        table_data.append(row)

    print(tabulate(table_data, headers=headers))


@app.command()
def test():
    pass


def main():
    app()


if __name__ == "__main__":
    main()
