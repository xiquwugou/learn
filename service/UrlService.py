#!/usr/bin/env python
#encoding: utf-8
import os
import unittest
from read_customers import ReadUrl
from util.Properties import Properties

__author__ = 'song'


def get_properties():
    p = Properties()
    #print os.getcwd()
    p.load(open('C:\\Users\\song\\learn\\config\\config.properties'))
    return p


def get_channels(channels=None):
    _url = '&'
    for i in range(len(channels)):
        x = channels[i]
        _url = _url + 'ChannelID' + str(i + 1) + '=' + str((channels[i]['channelCode'])) + '&'
    return _url


def parse_url(channels=None):
    p = get_properties()
    s = get_channels(channels)
    _9050 = p['channelBandwidthGetterUrl.9050'].format(RegionID="9050",
                                                       ChannelCount=len(channels),
                                                       StartTime=p['startTime'],
                                                       EndTime=p['endTime'],
                                                       channels=s)
    _10200 = p['channelBandwidthGetterUrl.10200'].format(RegionID="10200",
                                                         ChannelCount=len(channels),
                                                         StartTime=p['startTime'],
                                                         EndTime=p['endTime'],
                                                         channels=s)
    _18600 = p['channelBandwidthGetterUrl.18600'].format(ChannelCount=len(channels),
                                                         StartTime=p['startTime'],
                                                         EndTime=p['endTime'],
                                                         channels=s)
    _20002 = p['channelBandwidthGetterUrl.20002'].format(ChannelCount=len(channels),
                                                         StartTime=p['startTime'],
                                                         EndTime=p['endTime'],
                                                         channels=s)
    return [_9050, _10200, _18600, _20002]


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    def test_parse_url(self):
        read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
        x = read_url.get_channels('qq')
        url = parse_url(x)
        for u in url:
            print u

        self.assertEqual(4, len(url))

    #具体的测试用例，一定要以test开头
    def test_get_channels(self):
        read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
        x = read_url.get_channels('qq')
        print x
        print get_channels(x)

        self.assertEqual(1, 1)

