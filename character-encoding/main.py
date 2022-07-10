from utils.base_representations import hex_to_bin
from utils.unicode_repr import bin_to_utf8, bin_to_utf8_hex
from utils.dicts import hex_bin_dict


###
# Binary Code Point          | Binary UTF-8                        | Hex UTF-8
###
#                   010 0100 | 00100100                            | 24
#              000 1010 0010 | 11000010 10100010                   | C2 A2
#        0000 1001 0011 1001 | 11100000 10100100 10111001          | E0 A4 B9
#        0010 0000 1010 1100 | 11100010 10000010 10101100          | E2 82 AC
#        1101 0101 0101 1100 | 11101101 10010101 10011100          | ED 95 9C
# 0 0001 0000 0011 0100 1000 | 11110000 10010000 10001101 10001000 | F0 90 8D 88
###


def print_all_wiki_examples():
    def print_all(binary):
        print(binary, '|', bin_to_utf8(binary), '|', bin_to_utf8_hex(binary))

    print_all('010 0100')
    print_all('000 1010 0010')
    print_all('0000 1001 0011 1001')
    print_all('0010 0000 1010 1100')
    print_all('1101 0101 0101 1100')
    print_all('0 0001 0000 0011 0100 1000')


def check_digits(string):
    for i in string:
        if i not in hex_bin_dict:
            return -1
    return 0


def unicode_hex_to_utf8_hex(unicode_hex):
    hex_string = unicode_hex
    if unicode_hex[:2].upper() in ('U+', '\\X', '0X', 'H&'):
        hex_string = unicode_hex[2:]
    if check_digits(hex_string) != 0:
        raise ValueError(f'Unexpected character in the hex string {hex_string}')

    return bin_to_utf8_hex(hex_to_bin(hex_string))


if __name__ == '__main__':
    print(unicode_hex_to_utf8_hex('U+03C0'))  # Greek small letter pi
