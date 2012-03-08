#!/usr/bin/env python

import sys, crypt, string, random

password = sys.argv[1]
if len(sys.argv) >= 3:
    salt = sys.argv[2]
else:
    salt = ''
    # salt = ''.join(random.sample(string.ascii_letters, 2))

protected_password = crypt.crypt(password, salt)
print protected_password
