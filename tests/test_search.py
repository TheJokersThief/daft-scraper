#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mock
import unittest

from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import PropertyType, PropertyTypesOption, Facility, FacilitiesOption


with open('tests/fixtures/sample_page.html') as file:
    SEARCH_PAGE_HTML = file.read()


class TestDaftScraper(unittest.TestCase):

    def setUp(self):
        self.api = DaftSearch(SearchType.RENT)

    def tearDown(self):
        pass

    @mock.patch('daft_scraper.Daft.get', return_value=SEARCH_PAGE_HTML)
    def test_search(self, *args):
        options = [
            PropertyTypesOption([PropertyType.APARTMENT]),
            FacilitiesOption([Facility.PARKING, Facility.SERVICED_PROPERTY])
        ]

        got = self.api.search(options)
        self.assertEqual(got[0]['id'], 1443907)

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
        self.assertEqual(got[0]['id'], 1443907)

    def test__calc_offset(self):
        got = self.api._calc_offset(5)
        self.assertEqual(got, 100)
