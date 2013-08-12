#!/usr/bin/env python


def fib(N):
    """
    Recursively return the next term and the term before it in the Fibonacci
    sequence.
    
    """
    if N > 1:
        terms = fib(N - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms
    else:
        return [1, 0]


def validate_positive_integer():
    """
    Ask the user for input and only return when a positive integer under
    500 is given.

    """
    while True:
        s = raw_input("Which term in the Fibonacci sequence you want to see? ")
        try:
            terms = int(s)
            if terms >= 500:
                print "Enter a number smaller than 500."
            elif terms > 0:
                return terms
            else:
                print "Enter a positive integer."
        except ValueError:
            print "Enter a positive integer."


def main():
    N = validate_positive_integer()
    print fib(N)[1]


if __name__ == "__main__":
    main()
