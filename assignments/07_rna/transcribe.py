#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-03-24
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

    parser.add_argument('input',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'))


    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.input
    out = args.outdir


    fls, lns = 0, 0
    for fh in file:
        fls += 1
        out_fl = os.path.join(out, os.path.basename(fh.name))
        out_fh = open(out_fl, 'wt')
        lines, num = [], 0
        for line in fh:
            num += 1
            lines.append(line.strip().replace('T', 'U'))
        lns += num
        wrtlns = '\n'.join(lines)
        out_fh.write(wrtlns)
        out_fh.close()
    sequence = 'sequence' if num == 1 else 'sequences'
    files = 'file' if fls == 1 else 'files'

    print(f'Done, wrote {lns} {sequence} in {fls} {files} to directory "{out}".')


   # def new_char(t):
       # return 'U' if t in 'T' else t

   # file = ''.join([new_char(t) for t in file])



    #for c in file:
     #   file.read()
      #  file.replace(a, t).upper()
       # print(file)

# --------------------------------------------------
if __name__ == '__main__':
    main()
