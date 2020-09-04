#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""
__author__ = 'Sarah Beverton'

import sys
import re
import argparse
# from collections import OrderedDict


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    result = []
    names_result = []
    title_result = []
    with open(filename, 'r') as f:
        contents = f.readlines()
        year_pattern = re.compile(r'Popularity\sin\s(\d{4})')
        names_pattern = \
            re.compile(r'\<td\>(\d+)\<\/td\>\<td\>(\w+)\<\/td\>\<td\>(\w+)')
        for line in contents:
            title = year_pattern.search(line)
            names = names_pattern.search(line)
            if title:
                title_result.append(title.group(1))
            if names:
                boy_tuple = names.group(2, 1)
                girl_tuple = names.group(3, 1)
                names_result.append(boy_tuple)
                names_result.append(girl_tuple)
        names_dict = {}
        for name, rank in sorted(names_result, key=lambda tup: tup[0]):
            existing_rank = names_dict.get(name)
            if (existing_rank is None) or int(rank) < int(existing_rank):
                names_dict[name] = rank
        print(names_dict)
        name_strings = \
            [' '.join(name_rank) for name_rank in names_dict.items()]
        result = title_result + name_strings
    return result


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    parser_output = []
    for file in file_list:
        parser_output.extend(extract_names(file))
    # print('\n'.join(parser_output[:40]))


if __name__ == '__main__':
    main(sys.argv[1:])
