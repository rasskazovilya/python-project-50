#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    first_file_path = Path.cwd() / 'gendiff' /'scripts' / args.first_file
    second_file_path = Path.cwd() / 'gendiff' /'scripts' / args.second_file
    first_file = json.load(open(first_file_path))
    second_file = json.load(open(second_file_path))

    print(first_file)
    print(second_file)


if __name__ == '__main__':
    main()
