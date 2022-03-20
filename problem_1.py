'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

------------------------------------
My solution:

Instead of scrolling all the integers to check if they are divisible by 3 or 5
we will decompose the final result into the contribution of numbers divisible by 3 and 5.

The sum of all numbers divisible by 3 smaller than 1000 is:
3 + 6 + 9 + 12 + 15 + 18 +...999 = 3 * (1 + 2 + 3 + 4 + 5 + ... + 333)
The last value of the sum can be expressed in general as floor(N/3) (i.e. floor approximation of N/3).

This observation is very useful since let us compute the term with an analytical form:
= 3 * ( floor(N/3) * (floor(N/3) + 1) /2 )

The output will be the sum of the two components:
output = 3 * ( floor(N/3) * (floor(N/3) + 1) /2 ) + 5 * ( floor(N/3) * (floor(N/5) + 1) /2 )

!!! WAIT: to avoid double counting we have to substract those terms that are divisible by 3 and 5 (i.e. by 15)
FINAL OUTPUT = 3 * ( floor(N/3) * (floor(N/3) + 1) /2 ) +
               5 * ( floor(N/5) * (floor(N/5) + 1) /2 ) -
               15 * ( floor(N/15) * (floor(N/15) + 1) /2 )

'''

import timeit


def trivial_solution(N: int):
    '''
    Trivial solution
    Just loop over all integers and cumulate sum
    '''

    output = 0
    for i in range(1, N):
        if i%3==0 or i%5==0:
            output=output+i
    return output


def my_solution(N: int):
    '''

    '''

    # Number of integers mutiple of 3, 5, 15 smaller than N
    N_3 = (N-1)//3
    N_5 = (N-1)//5
    N_15 = (N-1) // 15

    SUM_3 = 3 * sum_1_N(N_3)
    SUM_5 = 5 * sum_1_N(N_5)
    SUM_15 = 15 * sum_1_N(N_15)

    output = SUM_3 + SUM_5 - SUM_15
    return output

def sum_1_N(N: int):
    '''Retur sum of integers from 1 to N'''
    return int((N * (N+1)) / 2)



if __name__ == '__main__':

    print(f'Trivial solution: {trivial_solution(1000)}')
    print(f'Execution time: {timeit.timeit(lambda: trivial_solution(1000), number=10000)}')


    print(f'Trivial solution: {my_solution(1000)}')
    print(f'Execution time: {timeit.timeit(lambda: my_solution(1000), number=10000)}')

