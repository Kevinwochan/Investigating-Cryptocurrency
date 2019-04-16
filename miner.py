#!/usr/bin/python3

import hashlib
import sys

# A miner for a google sheets blockchain https://docs.google.com/spreadsheets/d/15RbZsEjpUYlY8HzzWKEV6sgUVALtlwJIagsNIS3rDCg/edit#gid=0

text = sys.argv[1]

for nonce in range(10000000):
    input = text + str(nonce)
    hash = hashlib.sha256(input.encode()).hexdigest()
    print (input, hash)
    if hash.startswith("0000"):
        print("Found Hash")
        break
