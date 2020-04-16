#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-04-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO
import re
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-c',
                    '--cdhit',
                    help='Output file from CD-HIT (clustered proteins)',
                    metavar='FILE',
                    type=argparse.FileType('r'),
                    default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    args = parser.parse_args()

    if not args.cdhit:
        parser.error(f'the following arguments are required: -c/--cdhit')
    if not args.proteins:
        parser.error(f'the following arguments are required: -p/--proteins')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    tots = 0
    seq_tots = 0

    for line in args.cdhit:
        match = re.search(r'>(\d+)', line)
        if match:
            id = match.group(1)
            protein_ids = set()
            protein_ids.add(id)
            tots += 1
           #print(protein_ids)

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        prot_id = re.sub(r'\|.*', '', rec.id)

        if prot_id not in protein_ids:
            SeqIO.write(rec, args.outfile, 'fasta')
            seq_tots += 1


    print(f'Wrote {seq_tots:,d} of {tots:,d} unclustered proteins to \"{args.outfile.name}\"')





# --------------------------------------------------
if __name__ == '__main__':
    main()
