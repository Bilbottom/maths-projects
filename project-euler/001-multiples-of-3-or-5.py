"""
## Problem 1 - [Multiples of 3 or 5](https://projecteuler.net/problem=1)
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples_of_3_or_5(upper_limit: int = 1000) -> int:
    return sum(i for i in range(upper_limit) if i % 3 == 0 or i % 5 == 0)


if __name__ == '__main__':
    print(sum_multiples_of_3_or_5(1000))
