#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-02-03
Purpose: Find the vowel in a string
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

    parser.add_argument('vowel',
                        metavar='str',
                        help='A vowel',
                        choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        help='Some text',
                        metavar='str',
                        type=str,
                        default='')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text
    #index =text.index(vowel)    
    
    #text.index(vowel)

    if vowel in text:
        print(f'Found "{vowel}" in "{text}" at index {text.index(vowel)}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')

    #print(f'Found "{vowel}" in "{text}" at index {index}.') if vowel in text else print(f'"{vowel}" not found')
    #print(index))
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
