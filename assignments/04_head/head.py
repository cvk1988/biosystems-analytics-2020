#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-20
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='str',
                        help='Input file',
                        nargs='?',
                        type=argparse.FileType('r'))

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        nargs='?',
                        type=int,
                        default='10')

    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num \"{args.num}\" must be greater than 0')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.FILE

    num = args.num
    lines = 0

    for line in file:
        lines += 1
        print(line, end='')
        if lines == num:
            break

# --------------------------------------------------
if __name__ == '__main__':
    main()
