'''
Problem 5:
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---------------------------------------------
Solution:
Just using analytical Gauss formula to compute sum of integers and sum of squares.
I don't think there is something faster then a closed formula :)
'''


def sum_integers(n: int) -> int:
    '''Return sum of integers using Gauss formula'''
    return n * (n+1) / 2

def sum_squares(n: int) -> int:
    return n * (n+1) * (2*n+1) / 6

def solution(n: int) -> int:
    return int(sum_integers(n) ** 2 - sum_squares(n))


if __name__ == '__main__':
    print(f'Solution is {solution(100)}')
