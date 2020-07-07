#!/usr/bin/env python

import argparse
import sys

sys.path.append("../lib/MustangLib")
from mustangRouter import route

# parser = argparse.ArgumentParser(
#         description='A simple example program to print a friendly greeting.')
# parser.add_argument('--version', action='version',
#         version='helloworld ' + helloworld.__version__)

def foo():
    return route.doRoute('boo')

def do(argv=None):
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any arguments.
    # This just checks for the special --version and --help arguments and
    # ensures the user hasn't passed any other unrecognized arguments.
    print("Hello, world")
    return 0


if __name__ == '__main__':
    print(foo())