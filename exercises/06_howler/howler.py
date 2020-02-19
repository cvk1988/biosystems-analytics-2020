#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-18
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

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Makes a new file',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    print(args.text.upper(), file=out_fh, end='')
    print()
    out_fh.close()


    # print(args.text.upper())




# --------------------------------------------------
if __name__ == '__main__':
    main()
