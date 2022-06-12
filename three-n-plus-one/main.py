"""
https://en.wikipedia.org/wiki/Collatz_conjecture
https://www.youtube.com/watch?v=094y1Z2wpJg
"""


def collatz(term: int):
    while term > 1:
        print(term, end=' ')
        if term % 2:
            # n is odd
            term = 3 * term + 1
        else:
            # n is even
            term //= 2
    print(1, end='')


if __name__ == '__main__':
    n = int(input('Enter n: '))
    print('Sequence: ', end='')
    collatz(n)
