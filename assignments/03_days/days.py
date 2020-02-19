#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-19
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

    parser.add_argument('days',
                        metavar='str',
                        help='A day of the week',
                        nargs='+')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    days = args.days
    dic = {'Monday': 'On Mondays I never go to work', 'Tuesday': 'On Tuesdays I stay at home',
            'Wednesday': 'On Wednesdays I never feel inclined', 'Thursday': 'On Thursdays, it\'s a holiday',
            'Friday': 'And Fridays I detest', 'Saturday': 'Oh, it\'s much too late on a Saturday', 'Sunday': 'And Sunday is the day of rest'}


    for n in days:
        print(dic.get(n, f'Can\'t find "{n}"'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
