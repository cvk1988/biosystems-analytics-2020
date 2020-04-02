#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-04-01
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')
    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        choices=['dna', 'rna'],
                        type=str,
                        default='dna')
    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to generate',
                        metavar='int',
                        type=int,
                        default=10)
    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)
    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)
    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='int',
                        type=float,
                        default=0.5)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args
# --------------------------------------------------
def create_pool(pctgc, max_len, seqtype):
    """ Create the pool of bases """
    t_or_u = 'T' if seqtype == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)
    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    seq_num = 0
    for i in range(args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, seq_len)
        finseq = ''.join(seq)
        seq_num += 1
        args.outfile.write(f'>{seq_num}\n{finseq}\n')

    args.outfile.close()

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile.name}".')




# --------------------------------------------------
if __name__ == '__main__':
    main()
