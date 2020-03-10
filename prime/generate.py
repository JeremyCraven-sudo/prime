#!/usr/bin/python
'''Generates a list of 100 prime numbers and outputs it to a csv file
 
This generates a list of 100 prime numbers and outputs it to a file called
output.csv and prints the list to the console
 
'''
 
__author__ = "Jeremy Craven"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jecraven@valdosta.edu"
__status__ = "Finished"


from primepackage import *


def main():
    """Generate 100 prime numbers and output it into output.csv file
 
    """
    primes = get_n_prime(100)
 
    write_primes(primes, 'output.csv')
 
    prime_list = read_primes('output.csv')
 
    print(prime_list)


if __name__ == '__main__':
    main()

