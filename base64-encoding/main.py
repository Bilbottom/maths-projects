"""
Try to replicate the base64 encoding logic
"""
import base64
import string


def b64_encode(string_to_encode: str) -> str:
    return base64.b64encode(string_to_encode.encode('UTF-8')).decode()


def my_b64_encode(string_to_encode: str) -> str:
    """
    https://www.base64encode.org/
    https://www.lifewire.com/base64-encoding-overview-1166412
    """
    def bit_pattern(s: str) -> str:
        """
        Convert the string of characters into a string of 0s and 1s representing the binary of the original string

        E.g. the string 'Man' would map to the ASCII 77 (M), 97 (a), and 110 (n). In binary, these ASCII decimals map
        to 01001101 (77), 01100001 (97), and 01101110 (110). This functions concatenates and returns these binary
        representations as a string, such as '010011010110000101101110'
        """
        return ''.join([bin(ord(_)).replace('b', '').rjust(8, '0') for _ in s])

    def chunkify(s: str) -> list:
        """
        Convert a string into chunks, each of size 6

        For example, the binary string '010011010110000101101110' would be split into the list:
            ['010011', '010110', '000101', '101110']
        """
        return [s[i:i + 6] for i in range(0, len(s), 6)]

    def index_lookup(chunks: list) -> str:
        """
        Convert a list of strings representing binary into their corresponding decimal, and then replace each of them
        with the character that has the index of that decimal in the base-64 character set (index starts at 0)

        The base-64 character set used in this function is the MIME Base64 implementation which uses A-Z, a-z, and 0-9
        for the first 62 characters, with '+' and '\\' for the last two:

            ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+\\

        For example, the list of strings
            ['010011', '010110', '000101', '101110']
        would first map to the decimals
            [19, 22, 5, 110]
        which then map to the characters
            ['T', 'W', 'F', 'u']
        in the base-64 character set, hence a return value of 'TWFu'
        """
        char_lookup = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+\\'
        pre_padding = ''.join([char_lookup[int(chunk.ljust(6, '0'), 2)] for chunk in chunks])
        final_chunk_len = len(chunks[-1])
        if final_chunk_len not in {2, 4, 6}:
            raise ValueError('Unexpected number of bits in final byte')
        return pre_padding + ['', '==', '='][(final_chunk_len // 2) % 3]

    return index_lookup(chunkify(bit_pattern(string_to_encode)))


def main():
    credential_string = 'IAmBill:P4ssw0rd'
    print(b64_encode(credential_string))
    print(my_b64_encode(credential_string))


if __name__ == '__main__':
    main()
