#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-06
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
                        help='Grindage')
    parser.add_argument('-s',
                       '--sorted',
                       action='store_true',
                       help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] ='and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))



# --------------------------------------------------
if __name__ == '__main__':
    main()
