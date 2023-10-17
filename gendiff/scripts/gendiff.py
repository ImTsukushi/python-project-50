#!/usr/bin/env python
from gendiff.diffgenerator import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish'], help='set format output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == '__main__':
    main()
