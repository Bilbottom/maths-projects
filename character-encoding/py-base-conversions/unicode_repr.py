import dicts
from hex_bin_repr import bin_to_hex


###
# UTF-8 encoding
###
#
# uft-8 1 byte:  0 - 127 (7 significant bits)
#    0xxxxxxx
#
# utf-8 2 bytes: 128 - 2047 (8 - 11 significant bits)
#    110xxxxx 10xxxxxx
#
# utf-8 3 bytes: 2048 - 65,535 (12 - 16 significant bits)
#    1110xxxx 10xxxxxx 10xxxxxx
#
# utf-8 4 bytes: 65,536 - 2,097,152 (17 - 21 significant bits)
#    11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
###


# byte: max significant digits
max_byte_dict = {
    0: 0,
    1: 7,
    2: 11,
    3: 16,
    4: 21
}


def _get_utf8_bytes_required(sig_digits):
    for x in max_byte_dict:
        if sig_digits <= max_byte_dict[x]:
            return x
    return 0


def _parse_to_byte(sig_bin_string, utf8_bytes):
    parse_string = sig_bin_string.zfill(max_byte_dict[utf8_bytes])
    if utf8_bytes == 1:
        return '0' + parse_string
    elif utf8_bytes == 2:
        return '110' + parse_string[0:5] + ' 10' + parse_string[5:11]
    elif utf8_bytes == 3:
        return '1110' + parse_string[0:4] + ' 10' + parse_string[4:10] + ' 10' + parse_string[10:16]
    elif utf8_bytes == 4:
        return '11110' + parse_string[0:3] + ' 10' + parse_string[3:9] + ' 10' + parse_string[9:15] + ' 10' + parse_string[15:21]


def bin_to_utf8(bin_string):
    sig_bin = bin_string.replace(' ', '').lstrip('0')
    utf8_bytes = _get_utf8_bytes_required(len(sig_bin))
    if utf8_bytes < 1:
        return None
    # return sig_bin, utf8_bytes
    return _parse_to_byte(sig_bin, utf8_bytes)


def bin_to_utf8_hex(bin_string):
    return bin_to_hex(bin_to_utf8(bin_string))
