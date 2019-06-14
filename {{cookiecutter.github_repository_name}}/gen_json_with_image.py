#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Create a json file with a base64 file string inside
uri-scheme doc: https://en.wikipedia.org/wiki/Data_URI_scheme
"""
import argparse
import base64
import json
import os
from pprint import pprint


def create_json_with_file(file, file_type, for_js):
    filename = os.path.basename(file)
    full_filename, file_extension = os.path.splitext(file)
    b64 = base64.b64encode(open(file, "rb").read())
    try:
        # Python2
        print(file + "='''\\\n" + b64 + "'''")
    except TypeError:
        # Python3
        print(file + "='''\\\n" + b64.decode("utf8") + "'''")

    if for_js:
        my_json = {
            'file': 'data:file/{};base64,{}'.format(file_extension[1:], b64.decode("utf8"))
        }
    else:
        my_json = {
            'filename': filename,
            'uri-scheme': 'data:{}/{};base64'.format(file_type, file_extension[1:]),
            'file': '{}'.format(b64.decode("utf8"))
        }
    with open(full_filename + '.json', 'w') as outfile:
        json.dump(my_json, outfile)


def parsing_command_line():
    args = parser.parse_args()
    pprint(args)
    return args


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='0.5.0')
group1 = parser.add_argument_group()
group1.add_argument('-n', '--file_name', help='the full path filename')
group1.add_argument('-t', '--file_type', help='the file type (image/pdf/...)')
group1.add_argument('-j', '--for_js', default=0, type=int,
                    help='for javascript framework (default: 0 (no))')


if __name__ == '__main__':
    args = parsing_command_line()
    if args.file_name:
        create_json_with_file(args.file_name, args.file_type, args.for_js)
