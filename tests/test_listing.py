#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import mock
import unittest
from bs4 import BeautifulSoup

from daft_scraper.listing import ListingSchema, Listing


with open('tests/fixtures/ad_page_info.html') as file:
    AD_PAGE_HTML = BeautifulSoup(file.read(), features="html.parser")


class TestDaftScraper(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_confirm_next_json_parseable(self):
        with open('tests/fixtures/listing.json', 'r') as fixture:
            got = ListingSchema().load(json.load(fixture)['listing'])

        self.assertEqual(got.get('_id'), 2315059)
        self.assertEqual(got.get('price'), 14443.52)
        self.assertEqual(got.get('numBedrooms'), 3)
        self.assertEqual(got.get('numBathrooms'), None)

        # Test that the nested Lambda works
        first_subunit = got.get('prs').get('subUnits')[0]
        self.assertEqual(first_subunit.get('_id'), 2605808)

        # Test seller
        self.assertEqual(got.get('seller').get('sellerId'), 9601)

    @mock.patch('daft_scraper.Daft.get', return_value=AD_PAGE_HTML)
    def test_age_page_info(self, *args):
        listing = None
        with open('tests/fixtures/listing.json', 'r') as fixture:
            listing = Listing(ListingSchema().load(json.load(fixture)['listing']))

        self.assertEqual(listing.county, ["Cork"])
        self.assertEqual(listing.area, ["cork-city"])
        self.assertEqual(listing.views, 31956)
