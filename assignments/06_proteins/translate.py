#!/usr/bin/env python3
"""
Author : cory
Date   : 2020-03-17
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

    parser.add_argument('nucleic_acids',
                        metavar='str',
                        help='DNA/RNA')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    #parser.add_argument('-o',
                  #      '--outfile',
                   #     help='Output filename',
                   #     metavar='FILE',
                   #     type=argparse.FileType('r'),
                    #    default='out.txt')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dict = {line[0:3].upper(): line[4:].upper().strip() for line in args.codons}
    k = 3
    for codon in [args.nucleic_acids[i:i + k] for i in range(0, len(args.nucleic_acids) - k + 1, k)]:
       if codon.upper() in dict:
        open(args.outfile, 'wt') if args.outfile else sys.stdout
        args.outfile.write(codon.upper() + '\n')
        args.outfile.close()



    #print(dict)


    #for codon in args.nucleic_acids:
     #   if codon.upper() in dict:
      #      print(dict[line])


            #out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
            #out_fh.write(args.nucleic_acids.upper() + '\n')
            #out_fh.close()









# --------------------------------------------------
if __name__ == '__main__':
    main()
