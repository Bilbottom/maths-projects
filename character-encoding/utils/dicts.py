import json
from bidict import bidict


with open('mappings/dec_hex.json', 'r') as infile:
    dec_hex_dict = bidict(json.load(infile))

with open('mappings/hex_bin.json', 'r') as infile:
    hex_bin_dict = bidict(json.load(infile))
