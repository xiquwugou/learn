#!/usr/bin/env python
#encoding: utf-8
import unittest

from xml.dom.minidom import parseString


__author__ = 'song'

import urllib2


class BandwidthService(object):
    def __init__(self, url):
        self.url = url

    def get_bandwidth_date(self):
        _file = urllib2.urlopen(self.url)
        data = _file.read()
        _file.close()
        str_xml = data.replace("GB2312", "utf-8")
        str_xml = unicode(str_xml, encoding='GB2312').encode('utf-8')
        dom = parseString(str_xml)
        return dom

    def get_flux(self):
        dom = self.get_bandwidth_date()
        return self._get_flux(dom)

    def summary(self):
        dom = self.get_bandwidth_date()
        _list = self.get_in_data(dom)
        results = [int(i) for i in _list]
        out_list = self.get_out_data(dom)
        results_out = [int(i) for i in out_list]
        data = {'indata_max': max(results),
                'indata_average': sum(results) / len(results),
                'outdata_max': max(results_out),
                'outdata_average': sum(results_out) / len(results_out)
        }
        return data

    @staticmethod
    def get_in_data(dom):
        xml_tag = dom.getElementsByTagName('InData')[0].toxml()
        xml_data = xml_tag.replace('<InData>', '').replace('</InData>', '')
        _list = xml_data.split(',')
        _list.pop()
        return _list

    @staticmethod
    def get_out_data(dom):
        xmlTag = dom.getElementsByTagName('OutData')[0].toxml()
        xmlData = xmlTag.replace('<OutData>', '').replace('</OutData>', '')
        list = xmlData.split(',')
        list.pop()
        return list

    @staticmethod
    def _get_flux(dom):
        xmlTag = dom.getElementsByTagName('OutFlux')[0].toxml()
        xmlData = xmlTag.replace('<OutFlux>', '').replace('</OutFlux>', '')
        return xmlData


class IsOddTests(unittest.TestCase):
    def test_read_channel(self):
        url = 'http://223.202.45.145/BillQueryService3/pub/query/billing/' \
              'LogBandWidthByChannelID?Type=standard&RegionID=9050&ChannelCount=1&' \
              'StartTime=20131005&EndTime=20131005&ChannelID1=7245'
        read_url = BandwidthService(url)
        band = read_url.summary()
        self.assertIsNotNone(band)

