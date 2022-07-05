"""
Not 'real' memoisation
"""
import timeit
import sys

from memoise_dicts import LookupTable

sys.setrecursionlimit(1500)


def factorial(n: int) -> int:
    """
    Simple factorial implementation
    """
    return 1 if n == 0 else n * factorial(n - 1)


def factorial_memoised(n: int, factorial_lookup: LookupTable) -> int:
    """
    Memoised version of the factorial function -- requires 'training'
    """
    key = str(n)
    if n == 0:
        return 1
    elif key in factorial_lookup:
        return factorial_lookup[key]
    else:
        fact = n * factorial_memoised(n - 1, factorial_lookup)
        factorial_lookup.add(key, fact)
        return fact


def factorial_timer(number, factorial_lookup: LookupTable):
    """
    Time the two different versions
    """
    def time_factorial():
        [factorial(i) for i in range(1200)]

    def time_factorial_memoised():
        [factorial_memoised(i, factorial_lookup) for i in range(1200)]

    print('Original:', timeit.timeit(time_factorial, number=number))
    print('Memoised:', timeit.timeit(time_factorial_memoised, number=number))


def main_factorial():
    with LookupTable('factorial.json') as lookup:
        # factorial_memoised(1000, lookup)
        factorial_timer(100, lookup)


def main():
    main_factorial()


if __name__ == '__main__':
    main()
