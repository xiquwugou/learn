#!/usr/bin/env python
#encoding: utf-8

import unittest
from read_customers import ReadUrl

__author__ = 'song'


class ReadChannel(object):
    def __init__(self, url):
        self.url = url

    def get_channels(self, user_name):
        print self.name
        return ""


class IsOddTests(unittest.TestCase):
    def test_read_channel(self):
        read_url = ReadUrl("http://localhost:36000/customers")
        qq = read_url.get_channels("qq")
        self.assertIsNotNone(qq)

    def test_get_customers(self):
        read_url = ReadUrl("http://localhost:36000/customers")
        customers = read_url.get_customers()
        self.assertIsNotNone(customers)

    #def test_read_channels(self):
    #    read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
    #    x = read_url.load_page()
    #    print type(x)
    #
    #    for a in x:
    #        print a
    #
    #    self.assertEqual(2, 1)
