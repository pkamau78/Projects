#!/usr/bin/env python
import math


def main():
    while True:
        s = raw_input("How many digits of pi do you want to see? ")
        try:
            digits = int(s)
            if digits > 0:
                break
            else:
                print "Enter a proper nonnegative integer."
        except ValueError:
            print "Enter a proper nonnegative integer."
    print digits


if __name__ == "__main__":
    main()
