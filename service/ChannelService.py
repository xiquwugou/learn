#!/usr/bin/env python
#encoding: utf-8
import os
import unittest
from read_customers import ReadUrl
from util.Properties import Properties

__author__ = 'song'


class ChannelService(object):
    def __init__(self, user_name):
        p = self.get_properties()
        self.url = p["product_by_customerId"]
        self.channel_url = p["channels_by_CustomerId_productId"]
        self.user_name = user_name

    def get_products(self):
        url = self.url.format(customerCode="730")
        read_url = ReadUrl(url)
        return read_url.load_page()

    def get_channels(self):
        products = self.get_products()
        channels = []
        for p in products:
            c = self.get_channel(self.user_name, p['code'])
            for _c in c:
                channels.append(_c)
        return channels


    def get_channel(self, customer_code, product_code):
        url = self.channel_url.format(customerCode=customer_code, productCodes=product_code)
        read_url = ReadUrl(url)
        channel = read_url.load_page()
        return channel

    @staticmethod
    def get_properties():
        p = Properties()
        print os.getcwd()
        p.load(open('C:\\Users\\song\\learn\\config\\config.properties'))
        return p


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    #具体的测试用例，一定要以test开头
    def test_sum(self):
        read_channels = ReadChannel("qq")
        print read_channels.get_channels()
        self.assertEqual(1, 1)

    def test_get_channel(self):
        read_channels = ReadChannel("qq")
        print read_channels.get_channel("730", "11")
        self.assertEqual(1, 1)


