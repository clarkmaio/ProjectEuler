'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

------------------------------------------------------
'''

import numpy as np
import timeit


def is_palindrome(n: int) -> bool:
    n_digit = int(np.log10(n)) + 1
    n_digit_center = n_digit // 2 + 1
    for i in range(n_digit_center):
        check = str(n)[i] == str(n)[-i-1]
        if not check:
            return False
    return True


def brute_force(max_digit: int = 3) -> tuple:
    '''
    Brute force: loop over all 3-digit couples
    To avoid double counting loop on:
    i from 100 to 999
        j from i to 999
    '''
    largest = 10**(max_digit - 1)
    largest_i = 10**(max_digit - 1)
    largest_j = 10**(max_digit - 1)

    range_number_i = range(10**(max_digit - 1), 10**(max_digit))
    for i in range_number_i:
        range_number_j = range(i, 10**(max_digit))
        for j in range_number_j:
            prod = i * j
            if (prod > largest) and is_palindrome(prod):
                largest = prod
                largest_i = i
                largest_j = j

    return largest, largest_i, largest_j


def brute_force_opt(max_digit: int = 3) -> tuple:
    '''
    Just brute force but loop starting from biggest numbers
    '''
    largest = 10**(max_digit - 1)
    largest_i = 10**(max_digit - 1)
    largest_j = 10**(max_digit - 1)

    range_number_i = range(10**(max_digit)-1, 10**(max_digit - 1)-1, -1)
    for i in range_number_i:
        range_number_j = range(10**(max_digit)-1, i-1, -1)
        for j in range_number_j:
            prod = i * j
            if (prod > largest) and is_palindrome(prod):
                largest = prod
                largest_i = i
                largest_j = j

    return largest, largest_i, largest_j



if __name__ == '__main__':
    largest, i, j = brute_force_opt(3)
    print(f'Brute force solution: {i}*{j} = {largest}')

    N = 100
    print(f'Execution time brute force: {timeit.timeit(lambda: brute_force(3), number=N)/N}')
    print(f'Execution time brute force opt: {timeit.timeit(lambda: brute_force_opt(3), number=N)/N}')
