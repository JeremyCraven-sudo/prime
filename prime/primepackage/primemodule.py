#!/usr/bin/python
'''Checks numbers for primeness and gets list of n prime numbers.

This module gets the primeness of any number passed to is_prime and
can return a list of n prime numbers upon calling get_n_prime


'''

__author__ = "Jeremy Craven"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jecraven@valdosta.edu"
__status__ = "Finished"


def is_prime(check_num):
    '''Checks number for primeness

    This takes the number and evaluates whether or not the number is prime

    Args:
        check_num (int): intput number to be checked.

    Returns:
        boolean: true or false.

    Examples:
        >>> if(is_prime(22)):

    '''
    if check_num > 1:
        for i in range(2, check_num):
            if (check_num % i) == 0:
                return False
        return True
    return False


def get_n_prime(num):
    '''Gets a list of n prime numbers

    This takes an input number and makes a list that contains num amount of prime
    numbers

    Args:
        num (int): intput number that determines the amount of prime numbers

    Returns:
        list: a list of integers.

    Examples:
        >>> l = get_n_prime(20)

    '''
    prime_numbers = []
    count = 0
    current_num = 2
    while len(prime_numbers) < num:
        if is_prime(current_num):
            prime_numbers.append(current_num)
            count = count + 1
        current_num = current_num + 1
    return prime_numbers
