"""
            Instituto Politecnico Nacional
            Escuela Superior de Cómputo
            Autor: Mondragon Zarate Jesus Alejandro y Martínez Cervantes Xenia Guadalupe
"""
#Se importa math para realoizar operaciones como raíces cuadradas y potencias
import math
#Método que clasificará usando distancia a infinito
def clasificarInfinito(r,g,b,z1,z2,z3):
    d1 = max((abs(r - z1[0]))**100,(abs(g - z1[1]))**100, (abs(b - z1[2]))**100)
    d2 = max((abs(r - z2[0]))**100,(abs(g - z2[1]))**100, (abs(b - z2[2]))**100)
    d3 = max((abs(r - z3[0]))**100,(abs(g - z3[1]))**100, (abs(b - z3[2]))**100)
    distancias = [d1, d2, d3]
    menor = d1

    for d in distancias:
        if d < menor:
            menor = d

    if menor == d1:
        return "Zona cielo"
    if menor == d2:
        return "Zona boscosa"
    if menor == d3:
        return "Zona suelo"

#Método que clasificará usando distancia cityblock
def clasificarCityBlock(r,g,b,z1,z2,z3):
    d1 = abs(r - z1[0]) + abs(g - z1[1]) + abs(b - z1[2])
    d2 = abs(r - z2[0]) + abs(g - z2[1]) + abs(b - z2[2])
    d3 = abs(r - z3[0]) + abs(g - z3[1]) + abs(b - z3[2])

    distancias = [d1, d2, d3]
    menor = d1

    for d in distancias:
        if d < menor:
            menor = d

    if menor == d1:
        return "Zona cielo"
    if menor == d2:
        return "Zona boscosa"
    if menor == d3:
        return "Zona suelo"
#Método que clasificará usando distancia Euclidiana
def clasificarEuclidiana(r,g,b,z1,z2,z3):
    d1 = math.sqrt(math.pow(abs(r - z1[0]),2) + math.pow(abs(g - z1[1]),2) + math.pow(abs(b - z1[2]),2))
    d2 = math.sqrt(math.pow(abs(r - z2[0]),2) + math.pow(abs(g - z2[1]),2) + math.pow(abs(b - z2[2]),2))
    d3 = math.sqrt(math.pow(abs(r - z3[0]),2) + math.pow(abs(g - z3[1]),2) + math.pow(abs(b - z3[2]),2))

    distancias = [d1, d2, d3]
    menor = d1

    for d in distancias:
        if d < menor:
            menor = d

    if menor == d1:
        return "Zona cielo"
    if menor == d2:
        return "Zona boscosa"
    if menor == d3:
        return "Zona suelo"
