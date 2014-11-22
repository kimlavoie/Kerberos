#-*- coding: utf-8 -*-

# This function encrypt a message, using the scheme in specs
def Encryption(key, message):
    longueur = int(len(message) / len(key)) + 1
    key_modifie = key * longueur
    encodage = ""
    for i in range(len(message)):
        c = ord(message[i]) + ord(key_modifie[i])
        while c > 122:
            c = c - 122 + 32
        encodage = encodage + str(chr(c))
        
    return encodage

# This function decrypt a message, using the scheme in specs
def Decryption(key, encrypte):
    longueur = int(len(encrypte) / len(key)) + 1
    key_modifie = key * longueur
    message = ""
    for i in range(len(encrypte)):
        c = ord(encrypte[i]) - ord(key_modifie[i])
        while c < 33:
            c = c + 122 - 32
        message = message + str(chr(c))
        
    return message
    
# Create a dictionary from "cles.txt". Yes, it's hardcoded!
def DicoFromFile():
    file_content = ""
    dico = {}
    with open("cles.txt","r") as f:
        file_content = f.readlines();
    for line in file_content:
        key_value = line.strip().split(" ")
        dico[key_value[0]] = key_value[1]
    return dico
