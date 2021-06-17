#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xml2json.py
https://github.com/vesche/xml2json
"""

import io
import os
import sys
import json
import magic
import argparse
import xmltodict


def xml2json(input_file, output_file):
    """Outputs a JSON file given an XML file."""

    # check for input & output file issues
    if not os.path.isfile(input_file):
        print('Error: {} not found!'.format(input_file))
        sys.exit(1)
    if os.path.isfile(output_file):
        print('Error: {} already exists!'.format(output_file))
        sys.exit(2)

    # check for correct file types
    if not magic.from_file(input_file, mime=True).endswith('xml'):
        print('Error: {} is not a valid xml file!'.format(input_file))
        sys.exit(3)
    if not output_file.endswith('.json'):
        print('Error: {} must output a .json file!'.format(output_file))
        sys.exit(4)

    # read in the xml file, allowing for non-ascii
    f = io.open(input_file, mode='r', encoding='utf-8')
    data = f.read()

    # convert raw xml data into a python dictionary
    conv_data = xmltodict.parse(data)

    # convert python dictionary into json data
    json_data = json.dumps(conv_data)

    # write json data to disk
    with open(output_file, 'w') as f:
        f.write(json_data)


def get_parser():
    parser = argparse.ArgumentParser(description='XML to JSON file converter')
    parser.add_argument('-i', '--input', help='input file',
                        type=str, required=True)
    parser.add_argument('-o', '--output', help='output file',
                        type=str, required=True)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    input_file = args['input']
    output_file = args['output']

    xml2json(input_file, output_file)


if __name__ == '__main__':
    main()
