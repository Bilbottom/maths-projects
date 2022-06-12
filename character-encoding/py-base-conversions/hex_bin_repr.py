from bidict import bidict


def _get_div_rem(integer, mod):
    # recursive helper for dec_to_hex()
    divisor = integer // mod
    remainder = integer % mod
    return divisor, remainder


def dec_to_base(dec_string, base):
    assert base < 10  # need character set mapping after 10, eg F -> 15 in hex
    if dec_string == '0':
        return '0'

    ret_string = ''

    div_rem = _get_div_rem(int(dec_string), base)
    ret_string = str(div_rem[1]) + ret_string

    while div_rem[0] >= base:
        div_rem = _get_div_rem(int(div_rem[0]), base)
        ret_string = str(div_rem[1]) + ret_string
    ret_string = str(div_rem[0]) + ret_string

    return ret_string


hex_bin = bidict({
    # ' ': ' ',
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
})


def hex_to_bin(hex_string_in, nibbles=-1):
    ret_string = ''
    if nibbles != -1:
        assert nibbles >= len(hex_string_in)
        hex_string = '0' * (nibbles - len(hex_string_in)) + hex_string_in
    else:
        hex_string = hex_string_in

    for c in hex_string:
        ret_string += ' ' + hex_bin[c]

    return ret_string[1:]


def bin_to_hex(bin_string_in):
    sig_bin = bin_string_in.replace(' ', '').lstrip('0')
    bin_length = 8 * ((len(sig_bin) // 8) + (len(sig_bin) % 8 > 0))  # round up to nearest 8
    bin_string = sig_bin.zfill(bin_length)
    ret_string = ''
    for i in range(bin_length // 4):
        nibble = bin_string[(4 * i):(4 * (i + 1))]
        space = ' ' * ((i % 2) == 0)
        ret_string += space + hex_bin.inverse[nibble]
    return ret_string[1:]
