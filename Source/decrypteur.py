#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import common functins and standard library modules
from fonctions import Encryption, Decryption, DicoFromFile
import sys, base64

# Get and parse arguments, and cles.txt
IDc = sys.argv[1]
keys = DicoFromFile()
cle = keys[IDc]

# base64 to normal
encrypte = base64.b64decode(sys.argv[2])

# print decrypted Ticket
print base64.b64encode(Decryption(cle, encrypte))
