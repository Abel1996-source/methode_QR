
import numpy as np
from qr import methodeQr
from diagonale import diagonale
from diagonale import soustraction


def matriceSemblable(A,epsi):
    m,n =np.shape(A)
    B=np.zeros((m,n))
    ecart=soustraction(diagonale(A),diagonale(B),n)
    #k=0
    while True:
        (Q,R)=methodeQr(A)
        A=np.dot(R,Q)
        ecart=soustraction(diagonale(A),diagonale(B),n)
        B=A
        print("traitement en cours....")
        if ecart<epsi:
             break

    valeurPropres=diagonale(A)
    return np.array(valeurPropres)
