
def ecrire(nom,valeur):
    
        fichier = open(f"{nom}", "a")
        for i in range(1,2): 
            fichier.write(f"\n {valeur}")   
        fichier.close()