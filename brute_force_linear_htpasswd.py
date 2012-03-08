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

def read_htpasswd_dict():
    htpasswd_dict = []
    for line in fileinput.input(sys.argv[2]):
        if len(line.strip()) == 0:
            continue
        line = line.strip().split()
        if len(line) < 2:
            continue
        htpasswd_dict.append(line[1])
    return htpasswd_dict

def hashes_match(my_password, crypted_password):
    # print "given crypt: %s" % crypted_password
    # print "guess crypt: %s" % crypt.crypt(my_password, crypted_password)
    return (crypted_password == crypt.crypt(my_password, crypted_password))

def brute_force():
    htpasswd = read_htpasswd()
    htpasswd_dict = read_htpasswd_dict()
    for user in htpasswd:
        passwd_found = False
        for passwd in htpasswd_dict:
            if hashes_match(passwd, htpasswd[user]):
                passwd_found = True
                break
        if passwd_found:
            print "%s:%s" % (user, passwd)
        else:
            print "%s:" % (user)

brute_force()
