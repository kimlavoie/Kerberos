#!/usr/bin/env python
#-*- coding: utf-8 -*-
from fonctions import Encryption, Decryption, DicoFromFile
import sys, base64

IDc = sys.argv[1]
keys = DicoFromFile()
cle = keys[IDc]
encrypte = base64.b64decode(sys.argv[2])

print base64.b64encode(Decryption(cle, encrypte))