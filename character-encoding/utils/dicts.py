import json
import pathlib

from bidict import bidict


with open(f'{pathlib.Path(__file__).parent.resolve()}/mappings/dec_hex.json', 'r') as infile:
    dec_hex_dict = bidict(json.load(infile))

with open(f'{pathlib.Path(__file__).parent.resolve()}/mappings/hex_bin.json', 'r') as infile:
    hex_bin_dict = bidict(json.load(infile))
