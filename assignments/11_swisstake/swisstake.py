#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-04-28
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO
import re
import string
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Swissprot file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='str',
                        type=str,
                        required=True,
                        default='')

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='str',
                        type=str,
                        nargs='*',
                        default=0)

    parser.add_argument('-o',
                        '--output',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')


    return parser.parse_args()

# --------------------------------------------------
def keyword():
    re.search

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_taken = 0
    num_skp = 0

    for rec in SeqIO.parse(args.file, "swiss"):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower,taxa))
            if skip_taxa.intersection(taxa):
                num_skp += 1
                continue

        keywords = annots.get('keywords')
        if keywords:
           keywords = set(map(str.lower, keywords))
           
           if wanted_kw.intersection(keywords):
               num_taken += 1
               write.SeqIO(rec, args.output, 'fasta-2line')
           else:
               num_skipped += 1


    print(f'Done, skipped {num_skp} and took {num_taken}. See output in  \"{args.output.name}\".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
