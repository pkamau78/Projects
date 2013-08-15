#!/usr/bin/env python
from random import randrange


def miller_rabin_prime_test(n, iterations):
    """
    Implementation of the Miller-Rabin primality test, with a slight
    modification where we return True for 1 or 2.

    This test is not deterministic, but with a high iterations factor it is
    extremely robust.

    """
    if n < 3:
        return True
    elif n % 2 == 0:
        return False
    s = 0
    d = n - 1

    while True:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    assert(2**s * d == n - 1)
    
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True

    for i in range(iterations):
        a = randrange(2, n)
        if try_composite(a):
            return False
    return True


def ask_for_prime():
    """
    Prompts the user to calculate the next prime or terminate the program.

    Pressing enter is equivalent to entering yes, so the user can just hold
    down the enter button to continuously calculate primes.

    """
    while True:
        try:
            s = raw_input("Would you like to see another prime (y/n)? ")
        except:
            print "Please input a valid answer (y/n). "
            continue
        if s == "y" or s == "Y" or s == "yes" or s == "Yes" or s == "":
            return True
        elif s == "n" or s == "N" or s == "no" or s == "No":
            print "Have a nice day!"
            return False
        else:
            print "Please input a valid answer (y/n). "


def get_next_prime(n):
    """
    Uses Bertrand's Theorem to get a suitable search range for finding the next
    prime number.

    """
    if n == 1:
        return 2
    for p in range(n + 1, 2*n):
        if miller_rabin_prime_test(p, 100):
            return p
    print "Error finding the next prime"


def get_starting_number():
    """
    Ask the user for input and only return when a positive integer under the
    ceiling is given.

    """
    while True:
        s = raw_input("Enter a number to start finding primes above. ")
        try:
            n = int(s)
            if n >= 10000000000:
                print "Enter an integer smaller than 1000000000 (10^10)." 
            elif n > 0:
                return n
            else:
                print "Enter a positive integer."
        except ValueError:
            print "Enter a positive integer."


def main():
    n = get_starting_number()
    while ask_for_prime():
        n = get_next_prime(n)
        print n


if __name__ == "__main__":
    main()
