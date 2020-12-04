#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from daft_scraper.listing import Listing


class TestDaftScraper(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_confirm_next_json_parseable(self):
        with open('tests/fixtures/listing.json', 'r') as fixture:
            got = Listing().load(json.load(fixture)['listing'])

        self.assertEqual(got.get('id'), 2315059)
        self.assertEqual(got.get('price'), 3328)
        self.assertEqual(got.get('numBedrooms'), 3)
        self.assertEqual(got.get('numBathrooms'), None)

        # Test that the nested Lambda works
        first_subunit = got.get('prs').get('subUnits')[0]
        self.assertEqual(first_subunit.get('id'), 2605808)

        # Test seller
        self.assertEqual(got.get('seller').get('sellerId'), 9601)
