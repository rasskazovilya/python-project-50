#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def generate_diff(path1, path2):
    first_file = json.load(open(path1))
    second_file = json.load(open(path2))

    deleted_keys = set(first_file.keys()) - set(second_file.keys())
    added_keys = set(second_file.keys()) - set(first_file.keys())
    common_keys = set(first_file.keys()).intersection(set(second_file.keys()))

    print(first_file)
    print(second_file)
    print(f'Del keys: {deleted_keys}')
    print(f'Add keys: {added_keys}')
    print(f'Common keys: {common_keys}')


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    first_file_path = Path.cwd() / 'gendiff' / 'scripts' / args.first_file
    second_file_path = Path.cwd() / 'gendiff' / 'scripts' / args.second_file

    generate_diff(first_file_path, second_file_path)


if __name__ == '__main__':
    main()
