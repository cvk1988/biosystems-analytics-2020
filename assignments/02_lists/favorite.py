#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-11
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

    parser.add_argument('fav',
                        metavar='str',
                        nargs='+',
                        help='A favorite thing')

    parser.add_argument('-s',
                        '--sep',
                        help='Seperate your things',
                        default=', ',)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fav = args.fav


    few = args.sep


    if len(fav) == 1:
        print(f'{fav[0]}')
        print(f'This is one of my favorite things.')
    else:
        print(few.join(fav))
        print(f'These are a few of my favorite things.')





# --------------------------------------------------
if __name__ == '__main__':
    main()
