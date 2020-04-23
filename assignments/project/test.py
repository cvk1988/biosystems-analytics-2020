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
from subprocess import getstatusoutput
from numpy import mean
from itertools import chain
from shutil import rmtree
import re
import random
import string

prg = './separator.py'
file1 = './file1.fastq'
file2 = './file2.fastq'

# --------------------------------------------------
def random_string():
    """generate a random string"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """usage"""

    for file in [prg, file1, file2]:
        assert os.path.isfile(file)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """die on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------

# --------------------------------------------------
def test_defaults():
    """runs on good input"""

    out_dir = 'separated'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{prg} {file1}')
        assert rv == 0
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 2

        out_file = os.path.join(out_dir, 'file1_f.fastq')
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(out_file, 'fastq'))
        assert len(seqs) == 155

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_options():
    """runs on good input"""

    out_dir = random_string()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        cmd = f'{prg} -o {out_dir} {file1} {file2}'
        print(cmd)
        rv, out = getstatusoutput(cmd)
        assert rv == 0

        assert re.search(
            f'You have also written 250 sequences to {out_dir}/file2_f.fastq and 250 sequences to {out_dir}/file2_r.fastq.',
            out)
        assert re.search(
            'Done. You are valued and apppreciated.', out)

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 4

        seqs_written = 0
        for file in files:
            seqs_written += len(
                list(SeqIO.parse(os.path.join(out_dir, file), 'fastq')))

        assert seqs_written == 811
    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)
# --------------------------------------------------
