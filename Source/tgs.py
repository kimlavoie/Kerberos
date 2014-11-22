#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Import common functions and standard library modules
from fonctions import Encryption, Decryption, DicoFromFile
import sys, time, base64

# Get and parse arguments
entree = sys.argv[1]

tab_entree = entree.split("#")

IDc = tab_entree[0]
ADc = tab_entree[1]
IDv = tab_entree[2]
TICKETtgs = base64.b64decode(tab_entree[3])

# The ID of this TGS
IDtgs = "TGS1"

# Parse cles.txt and generate a dictionary
keys = DicoFromFile()

# Get TGS key
Ktgs = keys[IDtgs]

# Make a list of all ticket informations
dec_TICKETtgs = Decryption(Ktgs, TICKETtgs)
tab_TICKETtgs = dec_TICKETtgs.split("#")

# Verify that all informations are OK
if IDc != tab_TICKETtgs[0] or ADc != tab_TICKETtgs[1] or IDtgs != tab_TICKETtgs[2] or IDtgs != "TGS1" or int(time.time()) > int(tab_TICKETtgs[3]) + int(tab_TICKETtgs[4]):
	print "Non"
	sys.exit(1)

# Get the key of the service
Kv = keys[IDv]

# Init timestamp and duration
TS2 = str(int(time.time()))
Duree2 = str(3600)

# Generate and print ticket
TICKETv = base64.b64encode(Encryption(Kv, IDc + "#" + ADc + "#" + IDv + "#" + TS2 + "#" + Duree2))
print TICKETv

 
