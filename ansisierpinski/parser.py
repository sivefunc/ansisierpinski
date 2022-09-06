import argparse

def parser():
    parser = argparse.ArgumentParser(
            prog="AnsiSierpinski",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Simple sierpinski triangle viewer")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2022 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            '-r', '--rows', 
            type=int,
            default=32,
            help='rows of sierpinski triangle',
            metavar="")
 
    parser.add_argument(
            '-f', '--fill', 
            action="store_true",
            help='sierpinski triangle size the same as terminal screen')

    parser.add_argument(
            '-sn', '--shownum', 
            action="store_true",
            help="sierpinski triangle without graphics")
   
    args = parser.parse_args()
    return args
