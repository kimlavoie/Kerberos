#!/usr/bin/env python
#-*- coding: utf-8 -*-
from fonctions import Encryption, Decryption, DicoFromFile
import sys, time, base64

keys = DicoFromFile()
Kv = keys["V1"]

entree = sys.argv[1]

tab_entree = entree.split("#")

IDc = tab_entree[0]
ADc = tab_entree[1]
IDv = tab_entree[2]
TICKETv = base64.b64decode(tab_entree[3])

dec_TICKETv = Decryption(Kv, TICKETv)

tab_TICKETv = dec_TICKETv.split("#")

if IDc != tab_TICKETv[0] or ADc != tab_TICKETv[1] or IDv != tab_TICKETv[2] or IDv != "V1" or int(time.time())  > int(tab_TICKETv[3]) + int(tab_TICKETv[4]):
	print "Non"
else:
	print "OK"
