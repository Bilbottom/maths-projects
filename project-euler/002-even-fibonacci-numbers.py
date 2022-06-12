"""
## Problem 2 - [Even Fibonacci numbers](https://projecteuler.net/problem=2)
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
 first 10 terms will be:

> 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
 even-valued terms.
"""
import itertools


def sum_of_even_fibonacci_numbers(limit: int = 4000000) -> int:
    a = 1
    b = 2
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        b, a = b + a, b
    return total


def joe_solution(limit: int = 4000000) -> int:
    def f():
        yield 1
        a, b = 1, 2
        while True:
            yield a
            b, a = b + a, b

    return sum(
        i
        for i in itertools.takewhile(lambda x: x < limit, f())
        if i % 2 == 0
    )


if __name__ == '__main__':
    print(sum_of_even_fibonacci_numbers(limit=4000000))
    print(joe_solution(limit=4000000))