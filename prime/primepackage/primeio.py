#!/usr/bin/python
'''Reads a list of primes from a csv and writes a list of primes to csv
 
This reads an inputed file name and returns a list from that file.
It also writes a list of primes to a csv file name.

 
'''
 
__author__ = "Jeremy Craven"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jecraven@valdosta.edu"
__status__ = "Finished"


import csv


def write_primes(prime_list, file_name):
    '''Writes a list of primes to a dedicated file name
 
    Takes an input list of prime numbers and writes the list to a row in a CSV file
 
    Args:
        prime_list (list): list of prime integers
        file_name (str): intput file name.
 
    Returns:
        This method is void.
 
    Raises:
        IOError: io error.
 
    Examples:
        >>> write_primes(l, 'readme.txt');
 
    '''
    with open(file_name, "w") as open_file:
        csv_writer = csv.writer(open_file)
        csv_writer.writerow(prime_list)


def read_primes(file_name):
    '''Reads a list of primes from a dedicated file name
 
    Takes an input csv file of prime numbers and returns the list of these numbers 
 
    Args:        
        file_name (str): intput file name.
 
    Returns:
        list: list of integers
 
    Raises:
        IOError: io error.
 
    Examples:
        >>> l = read_primes('readme.txt');
 
    '''
    open_file = open(file_name, "r")
    return open_file.__next__()
