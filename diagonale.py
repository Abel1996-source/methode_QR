
import numpy as np

#-----fonction qui récupère les éléments diagonaux des matrices-------
def diagonale(a):
    A=np.array(np.matrix(a))
    B=A.diagonal()
    return B

#-----fonction qui effectue la soustraction des éléments diagonaux des matrices----
def soustraction(a,b,n):
    result=0
    equa=np.abs(a-b)
    for i in range(0,n):
        result=equa[i]+result
    return result
