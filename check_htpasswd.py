#!/usr/bin/env python

import sys, fileinput
import crypt, hashlib

def read_htpasswd():
    htpasswd = {}
    for line in fileinput.input(sys.argv[1]):
        if len(line.strip()) == 0:
            continue
        line = line.strip().split(':')
        username = line[0]
        password = line[1]
        htpasswd[username] = password
    return htpasswd

def hashes_match(my_password, crypted_password):
    # print "given crypt: %s" % crypted_password
    # print "guess crypt: %s" % crypt.crypt(my_password, crypted_password)
    return (crypted_password == crypt.crypt(my_password, crypted_password))

def find_user():
    my_username = sys.argv[2]
    my_password = sys.argv[3]
    htpasswd = read_htpasswd()
    for username in htpasswd:
        if (my_username == username) and hashes_match(my_password, htpasswd[username]):
            print "user '%s' with password '%s' found" % (my_username, my_password)
            return
    print "user '%s' not found" % my_username

find_user()
