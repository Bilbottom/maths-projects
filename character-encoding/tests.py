"""
Test some of the functions

TODO: convert to proper unit tests
"""
import itertools

from utils import base_representations as br


def test_dec_to_binary():
    for dec in range(10000):
        if str(br.dec_to_base(dec, 2)) != f'{dec:b}':
            print(f'{dec=}', f'{br.dec_to_base(dec, 2)=}', f'{dec:b}')


def test_dec_to_base():
    for dec, base in itertools.product(range(10000), range(2, 10)):
        base_repr = str(br.dec_to_base(dec, base))
        if int(base_repr, base) != dec:
            print(f'{dec=}', f'{br.dec_to_base(dec, base)=}')


def test_bin_to_hex():
    for dec in range(10000):
        bin_repr = f'{dec:b}'
        hex_repr = br.bin_to_hex(str(bin_repr))
        if int(hex_repr, 16) != dec:
            print(f'{dec=}', f'{br.dec_to_base(dec, 16)=}')


if __name__ == '__main__':
    # test_dec_to_binary()
    # test_dec_to_base()
    test_bin_to_hex()
