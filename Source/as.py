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
IDtgs = tab_entree[2]
TS1 = str(int(time.time()))
Duree1 = str(3600)

# Parse cles.txt and create a dictionnary (Array map)
keys = DicoFromFile()

# Catch missing IDc
try:
    Kc = keys[IDc]
except KeyError:
    print "Identifiant inconnu"
    sys.exit(1)
    
# Catch missing IDtgs
try:
    Ktgs = keys[IDtgs]
except KeyError:
    print "TGS inconnu"
    sys.exit(1)

# Generate Ticket
TICKETtgs = Encryption(Ktgs, IDc + "#" + ADc + "#" + IDtgs + "#" + TS1 + "#" + Duree1)

# Send results in base64
result = base64.b64encode(Encryption(Kc, TICKETtgs))
print result
