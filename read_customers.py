#!/usr/bin/env python
#encoding: utf-8

import json
import unittest
import urllib2

__author__ = 'song'

opener = urllib2.build_opener()


class ReadUrl():
    def __init__(self, url):
        self.url = url

    def load_page(self):
        req = urllib2.Request(self.url)
        f = opener.open(req)
        return json.load(f)

    def get_channels(self, user_name):
        self.url = "http://rcmsapi.chinacache.com:36000/customer/%s/channels" % user_name
        return self.load_page()

    def get_customers(self):
        return self.load_page()


class IsOddTests(unittest.TestCase):
    def test_read_channels(self):
        read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
        x = read_url.read_channels()
        print type(x)
        self.assertEqual(1, 1)
