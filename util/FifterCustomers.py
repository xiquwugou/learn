from read_customers import ReadUrl
from util.read_json_files import get_bandwidth_channels

__author__ = 'song'


def get_already_read_channels():
    channels = get_bandwidth_channels()
    _filter_customers = []
    for z in channels:
        _filter_customers.append(z["customerCode"])
    _c_f = set(_filter_customers)
    return _c_f


def filter_customer():
    read_url = ReadUrl("http://rcmsapi.chinacache.com:36000/customers")
    customers = read_url.get_customers()
    _customers = []
    for x in customers:
        _customers.append(x['code'])
    _customers = set(_customers)
    yy = get_already_read_channels()
    for y in list(_customers):
        if y in yy:
            _customers.remove(y)
    return list(_customers)

if __name__ == "__main__":
    filter_customer()

