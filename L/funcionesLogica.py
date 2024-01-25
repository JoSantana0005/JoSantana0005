import random
from matplotlib_venn import venn2, venn2_circles,venn3,venn3_circles
import matplotlib.pyplot as plt
def teclado(universal):
    for i in range(20):
        num = int(input("Ingrese un numero:"))
        universal.add(num)
    return universal
def tecladoSub(conjunto1):
    n = int(input("Ingrese la longitud del subconjunto: "))
    for i in range(n):
        num = int(input("Ingrese un numero"))
        conjunto1.add(num)
    return conjunto1
def aleatorio(universal):
    for i in range(20):
        universal.add(random.randint(0,100))
    return universal
def aleatorioSub(universal,conjunto1):
    n = int(input("Ingrese la longitud del subconjunto: "))
    for i in range(0,n):
        conjunto1.add(random.choice(list(universal)))
    return conjunto1

def union(conjunto1,conjunto2):
    union = conjunto1 | conjunto2
    return union
def uniondeTres(conjunto1,conjunto2,conjunto3):
    union12 = conjunto1 | conjunto2
    union123 = union12 | conjunto3
    return union123
def uniondeCuatro(conjunto1,conjunto2,conjunto3,conjunto4):
    union12 = conjunto1 | conjunto2
    union34 = conjunto3 | conjunto4
    union1234 = union12 | union34
    return union1234
def interseccion(conjunto1,conjunto2):
    inter = conjunto1 & conjunto2
    return inter
def intersecciondeTres(conjunto1,conjunto2,conjunto3):
    inter12 = conjunto1 & conjunto2
    inter123 = inter12 & conjunto3
    return inter123
def intersecciondeCuatro(conjunto1,conjunto2,conjunto3,conjunto4):
    inter12 = conjunto1 & conjunto2
    inter34 = conjunto3 & conjunto4
    inter1234 = inter12 & inter34
    return inter1234
def diferencia(conjunto1,conjunto2):
    difer = conjunto1 - conjunto2
    return difer
def diferenciadeTres(conjunto1,conjunto2,conjunto3):
    difer12 = conjunto1 - conjunto2
    difer123 = difer12 - conjunto3
    return difer123
def diferenciadeCuatro(conjunto1,conjunto2,conjunto3,conjunto4):
    difer12 = conjunto1 - conjunto2
    difer34 = conjunto3 - conjunto4
    difer1234 = difer12 - difer34
    return difer1234
def complemento(universal,conjunto1):
    comple = universal - conjunto1
    return comple
