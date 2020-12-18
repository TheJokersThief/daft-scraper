#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mock
import unittest
from bs4 import BeautifulSoup

from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import PropertyType, PropertyTypesOption, Facility, FacilitiesOption, PriceOption, BedOption
from daft_scraper.search.options_location import LocationsOption, Location


with open('tests/fixtures/sample_page.html') as file:
    SEARCH_PAGE_HTML = BeautifulSoup(file.read(), features="html.parser")


class TestDaftScraper(unittest.TestCase):

    def setUp(self):
        self.api = DaftSearch(SearchType.RENT)

    def tearDown(self):
        pass

    @mock.patch('daft_scraper.Daft.get', return_value=SEARCH_PAGE_HTML)
    def test_search(self, *args):
        options = [
            PropertyTypesOption([PropertyType.APARTMENT]),
            FacilitiesOption([Facility.PARKING, Facility.SERVICED_PROPERTY]),
            LocationsOption([Location.SWORDS_DUBLIN]),
            PriceOption(0, 1000),
            BedOption(1, 4),
        ]

        got = self.api.search(options)
        self.assertEqual(got[0].__dict__['id'], 1443907)

    def test__translate_options(self):
        wanted = {
            'propertyType': ['apartments'],
            'facilities': ['parking', 'serviced-property'],
            'location': ['swords-dublin'],
            'rentalPrice_from': 0,
            'rentalPrice_to': 1000,
            'numBeds_from': 1,
            'numBeds_to': 4
        }
        options = [
            PropertyTypesOption([PropertyType.APARTMENT]),
            FacilitiesOption([Facility.PARKING, Facility.SERVICED_PROPERTY]),
            LocationsOption([Location.SWORDS_DUBLIN]),
            PriceOption(0, 1000),
            BedOption(1, 4),
        ]
        got = self.api._translate_options(options)
        self.assertEqual(got, wanted)

    def test__translate_options__use_saleprice(self):
        wanted = {
            'salePrice_from': 100000,
            'salePrice_to': 200000
        }

        for sale_type in DaftSearch.SALE_TYPES:
            api = DaftSearch(sale_type)
            options = [
                PriceOption(100000, 200000),
            ]
            got = api._translate_options(options)
            self.assertEqual(got, wanted)

    def test__build_search_path(self):
        got = self.api._build_search_path()
        self.assertEqual(got, "property-for-rent/ireland")

    @mock.patch('daft_scraper.Daft.get', return_value=SEARCH_PAGE_HTML)
    def test__get_page_data(self, *args):
        path = self.api._build_search_path()
        got = self.api._get_page_data(path, params={})
        self.assertEqual(len(got.keys()), 12)

    @mock.patch('daft_scraper.Daft.get', return_value=SEARCH_PAGE_HTML)
    def test__get_listings(self, *args):
        path = self.api._build_search_path()
        page_data = self.api._get_page_data(path, params={})

        got = self.api._get_listings(page_data['props']['pageProps']['listings'])
        self.assertEqual(got[0].__dict__['id'], 1443907)

    def test__calc_offset(self):
        got = self.api._calc_offset(5)
        self.assertEqual(got, 100)
