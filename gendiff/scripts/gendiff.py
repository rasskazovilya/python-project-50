#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def get_cli_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        choices=['stylish', 'plain', 'json']
    )

    return parser.parse_args()


def main():
    args = get_cli_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
