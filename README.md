# fonctions.py
Il s'agit d'un fichier de fonctions communes aux trois programmes. Il est essentiel.
    
# decrypteur
Il permet au client de déchiffrer ce que l'AS lui envoie. Il s'utilise comme suit:

```
decrypteur ID_client message_chiffré
```

# Notes
* Les messages chiffrés sont encodés en base64 avant d'être envoyés sur la sortie standard, afin d'éviter les problèmes lors des appels subséquents. Ils sont ensuite décodés automatiquement par les différents serveurs.

* Il faut que python soit installé pour exécuter les programmes.

* Il faut que les programmes soient exécutables. Pour cela, utiliser `chmod +x nom_du_fichier`

* Si cela ne fonctionne pas, une dernière méthode est d'utiliser `python nom_du_fichier options`

* Il est inutile de réutiliser les exemples de "commandes.txt", le timestamp les invaliderait.

* Il y a un exemple d'exécution normale dans Programme. Pour l'exécuter, rendez-vous dans celui-ci et tapez `./exemple_execution.sh` ou `bash exemple_execution.sh`.
