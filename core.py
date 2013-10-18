import csv
from read_customers import ReadUrl
from service.BandwidthService import BandwidthService
from service.ChannelService import ChannelService
from service.UrlService import parse_url

__author__ = 'song'


def get_bandwidth():
    read_url = ChannelService("730")
    x = read_url.get_channels()
    print "-----------", x
    url = parse_url(x)
    bandwidth = {}
    for u in url:
        read_url = BandwidthService(u)
        band = read_url.get_flux()
        if "9050" in u:
            bandwidth["_9050"] = band
        elif "10200" in u:
            bandwidth["_10200"] = band
        elif "20002" in u:
            bandwidth["_20002"] = band
        else:
            bandwidth["_18600"] = band
    return bandwidth


def write_excel(_dict=None):
    w = csv.writer(open("output.csv", "w"))
    for key, val in _dict.items():
        w.writerow([key, val])


def _bandwidth(bandwidth, data):
    data.append(bandwidth["_9050"])
    data.append(bandwidth["_10200"])
    data.append(bandwidth["_18600"])
    data.append(bandwidth["_20002"])


def main():
    bandwidth = get_bandwidth()
    data = []
    #writer = csv.writer(open("songxiaofeng.csv", "w"))
    #for x in bandwidth:
    print bandwidth["_9050"]
    _bandwidth(bandwidth, data)
    #print tuple(data)
    #write_excel(tuple(data))
    #writer.writerow(tuple(data))
    #print bandwidth


if __name__ == "__main__":
    main()