#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-05-07
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import csv
from tabulate import tabulate
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    col = args.col
    val = args.val


    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if col not in reader:
        sys.exit(f'--col \"{col}\" not a valid column! \n Choose from {reader.fieldnames}')

    #val_str = str(reader.restval)
    val_col = str(reader.fieldnames)
    for rec in reader:
        if re.search(val, str(rec.values), re.IGNORECASE):
            csv.DictWriter(args.outfile, rec)
        if re.search(col, val_col, re.IGNORECASE):
            csv.DictWriter(args.outfile, rec)



    # writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    # writer.writeheader()


# --------------------------------------------------
# def read_csv(fh):
#     """Read the CSV input"""
#     args = get_args()
#     for row in csv.DictReader(args.file, delimiter=args.delimiter):
#         print(row['key'], row['value'])
#

# --------------------------------------------------


# --------------------------------------------------
if __name__ == '__main__':
    main()

