Le fichier "fonctions.py":
    Il s'agit d'un fichier de fonctions communes aux trois programmes. Il est essentiel.
    
Le programme "decrypteur":
    Il permet au client de d�chiffrer ce que l'AS lui envoie. Il s'utilise comme suit:
        decrypteur ID_client message_chiffr�

Les messages chiffr�s sont encod�s en base64 avant d'�tre envoy�s sur la sortie standard, 
afin d'�viter les probl�mes lors des appels subs�quents. Ils sont ensuite d�cod�s automatiquement 
par les diff�rents serveurs.

Il faut que python soit install� pour ex�cuter les programmes.