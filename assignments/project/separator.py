#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-04-22
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Separates forward and reversed reads from interleaved lines',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='A FASTQ file')


    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='separated')

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Snake Jazz"""

    args = get_args()


    for fh in args.file:
        basename = os.path.basename(fh.name)
        sp = basename.split('.')
        _f = '_f.'.join(sp)
        _r = '_r.'.join(sp)

        forward = os.path.join(args.outdir, _f)
        reverse = os.path.join(args.outdir, _r)

        out_f = open(forward, 'wt')
        out_r = open(reverse, 'wt')
        n = 0
        fornum = 0
        revnum = 0
        for rec in SeqIO.parse(fh, 'fastq'):
            n += 1
            if n % 2 == 0:
                SeqIO.write(rec, out_f, 'fastq')
                fornum += 1
            else:
                SeqIO.write(rec, out_r, 'fastq')
                revnum += 1
        out_f.close()
        out_r.close()

    print('Done. You are valued and apppreciated.')
    print(f'You have also written {fornum:,d} sequences to {out_f.name} and {revnum:,d} sequences to {out_r.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
