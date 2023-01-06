
import numpy as np
from semblable import matriceSemblable
from ecriture import ecrire
from readfile import lire

#----récupération de la matrice A dans le fichier VLPRNS.DAT---

valeur=input("Entrer le numéro de matrice EX: 00 ")
A=lire("VLPRNS.DAT",valeur)

#----récupértion de la précision de l'utilisateur-----
epsi=input("Entrez une précision ex: 0.0001! ")
epsi=float(epsi)

#-----calcule des valeurs propres de A---------
 
valeurPropres=matriceSemblable(np.array(A),epsi)

#--------Saisi du nom du fichier d'enregistrement-----
nom_fichier=input("Entrez le nom du fichier de sauvegade des valeurs propres ex: data! ")
nom_fichier=str(nom_fichier)

#--------Ecriture dans le fichier d'enregistrement-----

ecrire(f"{nom_fichier}.txt",valeurPropres)
print("résultat enregistrer avec succès")
