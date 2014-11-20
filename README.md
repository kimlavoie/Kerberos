# fonctions.py
Il s'agit d'un fichier de fonctions communes aux trois programmes. Il est essentiel.
    
# decrypteur
Il permet au client de d�chiffrer ce que l'AS lui envoie. Il s'utilise comme suit:

```
decrypteur ID_client message_chiffr�
```

# Notes
* Les messages chiffr�s sont encod�s en base64 avant d'�tre envoy�s sur la sortie standard, afin d'�viter les probl�mes lors des appels subs�quents. Ils sont ensuite d�cod�s automatiquement par les diff�rents serveurs.

* Il faut que python soit install� pour ex�cuter les programmes.

* Il faut que les programmes soient ex�cutables. Pour cela, utiliser `chmod +x nom_du_fichier`

* Si cela ne fonctionne pas, une derni�re m�thode est d'utiliser `python nom_du_fichier options`

* Il est inutile de r�utiliser les exemples de "commandes.txt", le timestamp les invaliderait.

* Il y a un exemple d'ex�cution normale dans Programme. Pour l'ex�cuter, rendez-vous dans celui-ci et tapez `./exemple_execution.sh` ou `bash exemple_execution.sh`.
