#!/usr/bin/env python3
"""
Author : Kai
Date   : 2021-05-12
Purpose: Change header for the units export tsv file

Run:
./parse_units_export.py -i units_export.tsv -o units.tsv

"""
import argparse
import os
import sys
import csv


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-o',
        '--outfile',
        help='output units file',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-i',
        '--infile',
        help='input units export file',
        metavar='str',
        type=str,
        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    outfile = args.outfile
    infile = args.infile

    # Read in argument input files
    input_list = []
    # open and save input data file as list of strings
    with open(infile, mode='r', encoding='utf-8-sig') as input:
        csv_reader = csv.reader(input, delimiter=',')
        # for row in csv_reader:
        #     input_list.append(row[0])
        header = next(csv_reader)
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                input_list.append(row[0])

    # header row
    header = ('ontology ID', 'label', 'definition')
    # Open and print outfile
    f = open(outfile, mode='w', encoding='utf-8-sig')
    print('\t'.join(header), file=f)
    for i in input_list:
        print(f'{i}', file=f)


# --------------------------------------------------
if __name__ == '__main__':
    main()
