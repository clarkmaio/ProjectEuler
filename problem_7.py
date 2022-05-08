'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import timeit
import numpy as np


def return_prime_number(n: int) -> int:
    '''
    Return nth prime number
    '''
    return


def prime_numbers(N: int) -> list:
    '''
    Return prime numbers from 2 to N
    '''

    numbers = np.array(range(2, N+1))
    prime_numbers_list = []

    is_empty_numbers = (np.shape(numbers)[0] == 0)
    while not is_empty_numbers:
        new_prime = numbers[0]
        prime_numbers_list.append(new_prime) # Store prime number
        numbers = drop_multiples_from_array(numbers, new_prime) # Drop multiplies
        is_empty_numbers = (np.shape(numbers)[0] == 0) # update is_empty

    return prime_numbers_list

def drop_multiples_from_array(v: np.array, n: int) -> np.array:
    '''
    Drop all multiples of n from array v.
    Return reduced array
    '''
    reduced_idx = np.where(v % n == 0)
    v_reduced = np.delete(v, reduced_idx)
    return v_reduced




if __name__ == '__main__':
    primes = prime_numbers(104744)
    print(f'Solution: {primes[10001]}')

