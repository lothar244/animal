#!/usr/bin/python3

import sys


def cat():
    print("Meow")

def human():
    print("Hello")

if __name__ == '__main__':
    if sys.argv[1] == 'cat':
        cat()
    else:
        human()