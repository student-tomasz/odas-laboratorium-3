#!/usr/bin/env python

import sys, hashlib

md5 = hashlib.md5(sys.argv[1])
print md5.digest()
print md5.hexdigest()
