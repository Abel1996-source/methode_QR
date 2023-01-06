
import numpy as np

def lire(a,valeur):
    matrice=[]
    if valeur=="00":
        
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[31].split()
            element1=content[32].split()
            matrice.append(element)
            matrice.append(element1)
            A=np.matrix(matrice,float)
        return A   
    if valeur=="01":
         with open(f"{a}", "r") as fichier:
             content = fichier.read().split('\n')
             element=content[38].split()
             element1=content[39].split()
             matrice.append(element)
             matrice.append(element1)
             A=np.matrix(matrice,float)
         return A
    if valeur=="02":
         with open(f"{a}", "r") as fichier:
             content = fichier.read().split('\n')
             element=content[45].split()
             element1=content[46].split()
             matrice.append(element)
             matrice.append(element1)
             A=np.matrix(matrice,float)
         return A
    if valeur=="03":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[52].split()
            element1=content[53].split()
            element2=content[54].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="04":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[60].split()
            element1=content[61].split()
            element2=content[62].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A          
    if valeur=="05":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[68].split()
            element1=content[69].split()
            element2=content[70].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="06":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[76].split()
            element1=content[77].split()
            element2=content[78].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="07":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[84].split()
            element1=content[85].split()
            element2=content[86].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="22":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[92].split()
            element1=content[93].split()
            element2=content[94].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="08":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[100].split()
            element1=content[101].split()
            element2=content[102].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="09":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[108].split()
            element1=content[109].split()
            element2=content[110].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            A=np.matrix(matrice,float)
        return A
    if valeur=="10":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[116].split()
            element1=content[117].split()
            element2=content[118].split()
            element3=content[119].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            A=np.matrix(matrice,float)
        return A
    if valeur=="11":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[125].split()
            element1=content[126].split()
            element2=content[127].split()
            element3=content[128].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            A=np.matrix(matrice,float)
        return A
    if valeur=="12":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[134].split()
            element1=content[135].split()
            element2=content[136].split()
            element3=content[137].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            A=np.matrix(matrice,float)
        return A
    if valeur=="13":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[143].split()
            element1=content[144].split()
            element2=content[145].split()
            element3=content[146].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            A=np.matrix(matrice,float)
        return A
    if valeur=="14":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[152].split()
            element1=content[153].split()
            element2=content[154].split()
            element3=content[155].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            A=np.matrix(matrice,float)
        return A
    if valeur=="15":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[161].split()
            element1=content[162].split()
            element2=content[163].split()
            element3=content[164].split()
            element4=content[165].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            A=np.matrix(matrice,float)
        return A
    if valeur=="16":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[171].split()
            element1=content[172].split()
            element2=content[173].split()
            element3=content[174].split()
            element4=content[175].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            A=np.matrix(matrice,float)
        return A
    if valeur=="17":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[181].split()
            element1=content[182].split()
            element2=content[183].split()
            element3=content[184].split()
            element4=content[185].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            A=np.matrix(matrice,float)
        return A
    if valeur=="18":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[191].split()
            element1=content[192].split()
            element2=content[193].split()
            element3=content[194].split()
            element4=content[195].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            A=np.matrix(matrice,float)
        return A
    if valeur=="19":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[201].split()
            element1=content[202].split()
            element2=content[203].split()
            element3=content[204].split()
            element4=content[205].split()
            element5=content[206].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            matrice.append(element5)
            A=np.matrix(matrice,float)
        return A
    if valeur=="20":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[212].split()
            element1=content[213].split()
            element2=content[214].split()
            element3=content[215].split()
            element4=content[216].split()
            element5=content[217].split()
            element6=content[218].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            matrice.append(element5)
            matrice.append(element6)
            A=np.matrix(matrice,float)
        return A
    if valeur=="21":
        with open(f"{a}", "r") as fichier:
            content = fichier.read().split('\n')
            element=content[224].split()
            element1=content[225].split()
            element2=content[226].split()
            element3=content[227].split()
            element4=content[228].split()
            element5=content[229].split()
            element6=content[230].split()
            element7=content[231].split()
            matrice.append(element)
            matrice.append(element1)
            matrice.append(element2)
            matrice.append(element3)
            matrice.append(element4)
            matrice.append(element5)
            matrice.append(element6)
            matrice.append(element7)
            A=np.matrix(matrice,float)
        return A