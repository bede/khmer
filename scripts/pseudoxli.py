#!/usr/bin/env python
#
# This file is a part of khmer, http://github.com/ged-lab/khmer/, and is
# Copyright (C) Michigan State University, 2009-2014. It is licensed under the
# three-clause BSD license; see doc/LICENSE.txt.
# Contact: khmer-project@idyll.org
#

"""
Single entry point script for khmer
"""

import argparse
from oxli import fq2fa


def get_parser():
    """
    returns the parser object for the oxli subcommand handler
    """
    parser = argparse.ArgumentParser(
        description='Single entry point script for khmer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(help='foo')

    # sub parser for fastq-to-fasta
    parser_fq2fa = subparsers.add_parser('fastq-to-fasta', help="Converts \
            FASTQ format(.fq) files to FASTA format(.fa)")

    fq2fa.add_args(parser_fq2fa)
    parser_fq2fa.set_defaults(func=fastq_to_fasta)

    return parser


def fastq_to_fasta(args):
    """
    fastq_to_fasta subcommand handler function
    """
    fq2fa.do_fastq_to_fasta(args)


def main():
    """
    main function; does the parsing and kicks off the subcommand
    """
    args = get_parser().parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
