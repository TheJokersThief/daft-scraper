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
