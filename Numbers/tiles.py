#!/usr/bin/env python


def validate_positive_float(prompt_str):
    """
    Ask the user for input and only return when a positive number under the
    ceiling is given.

    """
    while True:
        s = raw_input(prompt_str)
        try:
            n = float(s)
            if n >= 10000000:
                print "Enter a float smaller than 10000000." 
            elif n > 0:
                return n
            else:
                print "Enter a positive float."
        except ValueError:
            print "Enter a positive float."


def main():
    w = validate_positive_float("Enter the width of your floor (ft). ")
    l = validate_positive_float("Enter the length of your floor (ft). ")
    p = validate_positive_float("Enter the cost per sq ft for your tiles "
                                "($/sq ft). ")
    print "A {:.2f}x{:.2f} sq ft floor will cost ${:.2f} to tile".\
          format(w, l, p * w * l)


if __name__ == "__main__":
    main()
