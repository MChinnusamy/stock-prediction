'''common util functions'''
import os
import urllib.request
import json

def format_path(path_from_root) -> str:
    '''generates absolute path from relative path'''
    base_path = os.path.dirname(os.path.realpath('__file__'))
    absolute_path = os.path.join(base_path, path_from_root)
    return absolute_path


def get_csv_file_list_in_dir(directory) -> list:
    '''generates a list of csv files in given directory'''
    filenames = os.listdir(directory)
    return [filename for filename in filenames if filename.endswith('csv')]


def url_builder(url, params) -> str:
    '''formats url'''
    separator = '&'
    rest_of_url = separator.join(params)
    url = url + rest_of_url
    return url


def make_dir_if_not_exists(path_from_root):
    '''creates directory if not exists'''
    directory = format_path(path_from_root)
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_json_from_url(url):
    '''fetch data as json from url'''
    with urllib.request.urlopen(url) as url2:
        data = json.loads(url2.read().decode())
        return data