#!/usr/bin/env python

import sys, string, crypt

passwd = sys.argv[1]
chars = string.ascii_letters
for a in chars:
    for b in chars:
        for c in chars:
            guess = a+b+c
            crypted = crypt.crypt(guess, passwd)
            if crypted == passwd:
                print "znaleziono haslo: %s" % guess
                exit()
print "nie znaleziono hasla"
