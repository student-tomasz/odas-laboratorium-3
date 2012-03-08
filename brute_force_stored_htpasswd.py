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
    htpasswd_dict = {}
    for line in fileinput.input(sys.argv[2]):
        if len(line.strip()) == 0:
            continue
        line = line.strip().split()
        if len(line) < 2:
            continue
        # print "htpasswd_dict[%s] = %s" % (hashlib.md5(line[1]).hexdigest(), line[1])
        htpasswd_dict[hashlib.md5(line[1]).hexdigest()] = line[1]
    return htpasswd_dict

def brute_force():
    htpasswd = read_htpasswd()
    htpasswd_dict = read_htpasswd_dict()
    for user in htpasswd:
        if htpasswd[user] in htpasswd_dict:
            print "%s:%s" % (user, htpasswd_dict[htpasswd[user]])
        else:
            print "%s:" % (user)

brute_force()
