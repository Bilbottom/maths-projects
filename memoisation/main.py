"""
https://en.wikipedia.org/wiki/Memoization
"""
import timeit
import sys

sys.setrecursionlimit(1500)


def best_fibonacci_func(n: int) -> int:
    """
    Stolen from the main man, Daniel Nerozi
    """
    if n in {0, 1}:
        return 1

    sequence = [1, 1]
    sequence.extend(sequence[c - 1] + sequence[c - 2] for c in range(2, n + 1))
    return sequence[n]


def fibonacci(n: int) -> int:
    """
    Naive fibonacci implementation
    """
    return 1 if n in {0, 1} else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoised(start: int) -> int:
    """
    Memoised version of the fibonacci function -- only saved in cache
    """
    fib_cache = {
        '0': 1,
        '1': 1
    }

    def inner_fib(n: int) -> int:
        key = str(n)
        if key in fib_cache:
            return fib_cache[key]

        value = inner_fib(n - 1) + inner_fib(n - 2)
        fib_cache[key] = value
        return value

    return inner_fib(start)


def fibonacci_timer(number):
    """
    Time the three different versions
    """
    repeat = 30

    def time_fibonacci():
        [fibonacci(i) for i in range(repeat)]

    def time_fibonacci_memoised():
        [fibonacci_memoised(i) for i in range(repeat)]

    def time_fibonacci_dan():
        [best_fibonacci_func(i) for i in range(repeat)]

    print('Original:', timeit.timeit(time_fibonacci, number=number))
    print('Memoised:', timeit.timeit(time_fibonacci_memoised, number=number))
    print("Daniel's:", timeit.timeit(time_fibonacci_dan, number=number))


def main():
    fibonacci_timer(100)


if __name__ == '__main__':
    main()
