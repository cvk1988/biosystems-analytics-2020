#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-04-08
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random
from Bio import SeqIO
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='A file')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0.00 < args.pct <= 1:
        parser.error(f'--pct \"{args.pct}\" must be between 0 and 1')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    numf = 0
    nums = 0
    for i, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        numf += 1
        print(f'  {i}: {basename}')

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                nums += 1
        out_fh.close

    if numf == 1:
        print(f'Wrote {nums:,d} sequences from {numf} file to directory \"{args.outdir}\"')
    else:
        print(f'Wrote {nums:,d} sequences from {numf} files to directory \"{args.outdir}\"')





# --------------------------------------------------
if __name__ == '__main__':
    main()
