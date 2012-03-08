#!/usr/bin/env python

def trivial_hash(data):
    hashed_data = 0
    for char in data:
        hashed_data += ord(znak)
    return hashed_data % 999
