import csv
import json
import logging

import logging.config
import time
import datetime
import xlwt
from myexcel.ExcelMain import create_finance_title
from myexcel.xlwt_styles import EPIC_STYLE, REPORTER_LABEL_STYLE
from read_customers import ReadUrl
from service.BandwidthService import BandwidthService
from service.ChannelService import ChannelService
from service.UrlService import parse_url
from util.read_json_files import get_bandwidth_channels

__author__ = 'song'

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sync")


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0)
        logger.info('%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0))
        return ret

    return wrap


def get_bandwidth_by_channels(_channels):
    url = parse_url(_channels)
    bandwidth = {}
    for u in url:
        read_url = BandwidthService(u)
        band = read_url.get_flux()
        if "RegionID=9050" in u:
            bandwidth["_9050"] = band
        elif "RegionID=10200" in u:
            bandwidth["_10200"] = band
        elif "ISPID1=20002" in u:
            bandwidth["_20002"] = band
        else:
            bandwidth["_18600"] = band
    return bandwidth


def create_wordbook():
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet(u'Users')
    create_finance_title(worksheet)
    return workbook, worksheet


@timing
def _do_create_excel(_channels=None):
    workbook, worksheet = create_wordbook()
    x = 0
    for c in _channels:
        x += 1
        worksheet.write(x, 0, c['customerName'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 1, c['product_name'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 2, c['channelCode'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 3, c['state'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 4, c['channelDepartment'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 5, c['_9050'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 6, c['_10200'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 7, c['_18600'], REPORTER_LABEL_STYLE)
        worksheet.write(x, 8, c['_20002'], REPORTER_LABEL_STYLE)
    now = time.time()
    workbook.save('peak_flux' + str(now) + '.xls')


@timing
def get_bandwidth(customer_code):
    read_url = ChannelService(customer_code)
    _channels = read_url.get_channels()
    for user in _channels:
        _c = [user]
        _b = get_bandwidth_by_channels(_c)
        user["_9050"] = _b["_9050"]
        user["_10200"] = _b["_10200"]
        user["_20002"] = _b["_20002"]
        user["_18600"] = _b["_18600"]
        with open("tmp/" + str(user["channelCode"]) + ".tmp" + "", 'w') as outfile:
            json.dump(user, outfile)


def write_excel(_dict=None):
    w = csv.writer(open("output.csv", "w"))
    for key, val in _dict.items():
        w.writerow([key, val])


def _bandwidth(bandwidth, data):
    data.append(bandwidth["_9050"])
    data.append(bandwidth["_10200"])
    data.append(bandwidth["_18600"])
    data.append(bandwidth["_20002"])


@timing
def execute_customers():
    read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
    customers = read_url.get_customers()
    for x in customers:
        logger.info(x['code'])
        get_bandwidth(str(x["code"]))


if __name__ == "__main__":
    #execute_customers()
    channels = get_bandwidth_channels()
    _do_create_excel(channels)
    logger.info("done")

