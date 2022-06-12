"""
## Problem 3 - [Largest prime factor](https://projecteuler.net/problem=3)
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math


def is_prime(num: int) -> bool:
    """True if `num` is prime, else return False"""
    if num % 2 == 0 or num <= 1:
        return False
    return all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))


def get_factors(num: int) -> list:
    """The list of factors of `num`. Sorted in ascending order"""
    lower_factors = [i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]
    return sorted(set(lower_factors + [num // i for i in lower_factors]))


def get_prime_factors(num: int) -> list:
    """The list of prime factors of `num`"""
    return [i for i in get_factors(num=num) if is_prime(num=i)]


def largest_prime_factor(num: int) -> int:
    """The largest prime factor of `num`"""
    return max(get_prime_factors(num=num))


if __name__ == '__main__':
    x = 600851475143
    # print(get_factors(x))
    # print(get_prime_factors(x))
    print(largest_prime_factor(x))
