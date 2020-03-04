#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-03-03
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='An Input File',
                        default='')

    parser.add_argument('-m',
                        '--min',
                        help='Minimum pairs',
                        metavar='Int',
                        type=int,
                        default='0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.file:
        sp = line.split()
        comp = (list(zip(sp[0], sp[1])))
        dis = sum(1 for a, b in comp if a != b) + abs(len(sp[1])) - abs(len(sp[0]))

        if dis >= args.min:
            print(f'{dis:8}:{sp[0]:19} {sp[1]:20}')














    #for fh in file:
     #   word1 = file.split([0])
      #  word2 = file.split([1])
       # print(word1)

    #for line in file:
     #   print(line, end='')








# --------------------------------------------------
if __name__ == '__main__':
    main()
