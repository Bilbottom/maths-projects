import json
from bidict import bidict


with open('utils/mappings/dec_hex.json', 'r') as infile:
    dec_hex_map = bidict(json.load(infile))


def _get_dec(hex_value):
    return dec_hex_map.inverse[str(hex_value)]


def _get_hex(dec_value):
    return dec_hex_map[str(dec_value)]


def _get_div_rem(integer, mod=16):
    # recursive helper for dec_to_hex()
    divisor = integer // mod
    remainder = integer % mod
    return divisor, remainder


def dec_to_hex(dec_string):
    if dec_string == '0':
        return '0'

    ret_string = ''
    div_rem = _get_div_rem(int(dec_string))
    ret_string = _get_hex(div_rem[1]) + ret_string
    while div_rem[0] > 15:
        div_rem = _get_div_rem(int(div_rem[0]))
        ret_string = _get_hex(div_rem[1]) + ret_string
    ret_string = _get_hex(div_rem[0]) + ret_string

    return ret_string


def hex_to_dec(hex_string):
    temp = 0
    string_len = len(hex_string)
    for i, c in enumerate(hex_string):  # need enumerate to get index for power
        power = (string_len - i - 1)
        temp += (16 ** power) * int(dec_hex_map.inverse[c])

    return str(temp)


if __name__ == '__main__':
    print(f"{hex_to_dec('0')=}")
    print(f"{dec_to_hex('0')=}")

    print(f"{hex_to_dec('F423F')=}")
    print(f"{dec_to_hex('999999')=}")

    print(f"{hex_to_dec('10FFFF')=}")

    print(f'{((2 ** 21) - 1)=}')
    print(f"{dec_to_hex(str((2 ** 21) - 1))=}")
