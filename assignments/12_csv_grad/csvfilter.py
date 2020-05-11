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
    val_col = ",".join(reader.fieldnames)
    seqs_wr = 0
    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    if re.search(col, val_col, re.IGNORECASE):
        for rec in reader:
            if col and val:
                text = rec[col]
                if re.search(col, str(rec.keys()), re.IGNORECASE):
                    if re.search(val, text, re.IGNORECASE):
                        writer.writerow(rec)
                        seqs_wr += 1
            elif val:
                if re.search(val, str(rec.values()), re.IGNORECASE):
                    writer.writerow(rec)
                    seqs_wr += 1
    else:
        sys.exit(f'--col \"{col}\" not a valid column! \n Choose from {",".join(reader.fieldnames)}')

    print(f'Done, wrote {seqs_wr} to \"{args.outfile.name}\".')





# --------------------------------------------------
if __name__ == '__main__':
    main()

