#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from daft_scraper import Daft


class TestDaftScraper(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_confirm_next_json_parseable(self):
        api = Daft()
        webpage = api.get('/property-for-rent/ireland')
        next_script_text = webpage.find('script', {'id': '__NEXT_DATA__'})
        json.loads(next_script_text.string)
