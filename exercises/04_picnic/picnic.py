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

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='A positional argument')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort that list',
                        action='store_true')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items= args.items

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print('You are bringing {}.'.format(' and '.join(items)))
    else:
        print('You are bringing {}.'.format)


# --------------------------------------------------
if __name__ == '__main__':
    main()
