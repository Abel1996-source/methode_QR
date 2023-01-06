
import numpy as np

def methodeQr(A):
   
    #recupération du nombre de ligne et de colonne de la matrice
    m,n = np.shape(A)
    #création de la matrice v de vecteur composé que de zeros 
    v = np.zeros((m,n))
  #création de la matrice R composé que de zeros 
    R = np.zeros((n,n))
    #création de la matrice A composé que de zeros 
    Q = np.zeros((m,n))
    #convertion de la matrice en dynamique 
    A=np.array(A)

    for i in range(0,n):
        v[:,i] = A[:,i]

    for i in range(0,n):
        R[i,i] = np.linalg.norm(v[:,i],2)
        Q[:,i] = v[:,i]/R[i,i]
        for j in range(i,n):
            R[i,j] = np.dot( (Q[:,i].conjugate()).T, v[:,j])
            v[:,j] = v[:,j] - R[i,j]*Q[:,i]

    return (Q,R)

