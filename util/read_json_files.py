import json

__author__ = 'song'

import glob
import os


def read_files():
    search_dir = "../tmp/"
    _files = filter(os.path.isfile, glob.glob(search_dir + "*.tmp"))
    _files.sort(key=lambda x: os.path.getmtime(x))
    return _files


def parse_json(_path=None):
    json_data = open(_path)
    data = json.load(json_data)
    return data


def get_bandwidth_channels():
    channels = []
    _files = read_files()
    for f in _files:
        channels.append(parse_json(f))
    return channels


if __name__ == "__main__":
    files = read_files()
    for x in files:
        parse_json(x)