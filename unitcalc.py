#! /usr/bin/python2.7

"""
Your Name
Lab 11
Physics 91SI, Spring 2013

"""

import sys

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    print unitcalc(' '.join(sys.argv[1:]))

def unitcalc(s):
    """Parse a string describing an operation on quantities with units."""
    pass
if __name__ == "__main__": main()
