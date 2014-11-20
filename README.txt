Le fichier "fonctions.py":
    Il s'agit d'un fichier de fonctions communes aux trois programmes. Il est essentiel.
    
Le programme "decrypteur":
    Il permet au client de déchiffrer ce que l'AS lui envoie. Il s'utilise comme suit:
        decrypteur ID_client message_chiffré

Les messages chiffrés sont encodés en base64 avant d'être envoyés sur la sortie standard, 
afin d'éviter les problèmes lors des appels subséquents. Ils sont ensuite décodés automatiquement 
par les différents serveurs.

Il faut que python soit installé pour exécuter les programmes.