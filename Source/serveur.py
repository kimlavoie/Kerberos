#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import common functions and standard library modules
from fonctions import Encryption, Decryption, DicoFromFile
import sys, time, base64

# Generate key dictionary and find V1's key
keys = DicoFromFile()
Kv = keys["V1"]

# Get and parse arguments
entree = sys.argv[1]

tab_entree = entree.split("#")

IDc = tab_entree[0]
ADc = tab_entree[1]
IDv = tab_entree[2]
TICKETv = base64.b64decode(tab_entree[3])

# Generate a list of ticket's informations
dec_TICKETv = Decryption(Kv, TICKETv)
tab_TICKETv = dec_TICKETv.split("#")

# Make final verifications and output verdict
if IDc != tab_TICKETv[0] or ADc != tab_TICKETv[1] or IDv != tab_TICKETv[2] or IDv != "V1" or int(time.time())  > int(tab_TICKETv[3]) + int(tab_TICKETv[4]):
	print "Non"
else:
	print "OK"
