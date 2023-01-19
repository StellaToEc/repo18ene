"""
            Instituto Politecnico Nacional
            Escuela Superior de Cómputo
            Autor: Mondragon Zarate Jesus Alejandro y Martínez Cervantes Xenia Guadalupe
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from clasificador import *

# Calculo del centroide del cielo o C1
img = cv2.imread('./image/cielo.png', 1)
img2 = cv2.imread('./image/3-regiones.png', 1)
wid = img.shape[1]
hgt = img.shape[0]
cont = 0
contx = 0
z1 = [0, 0, 0]

c1=[]
# Obtener el numero de pixeles en la zona
for i in range(hgt):

    for d in range(wid):
        pixel2 = img[i, d]
        if pixel2[0] == 0:
            contx = contx + 1
            c1.append([i,d])

# obtener el centroide considerando el 80% de pixeles
for i in range(hgt):
    for d in range(wid):
        pixel = img[i, d]
        pixel2 = img2[i, d]
        if int(pixel[0]) * int(pixel2[0]) == 0 and cont < contx * .8:
            z1[0] = z1[0] + pixel2[0]
            z1[1] = z1[1] + pixel2[1]
            z1[2] = z1[2] + pixel2[2]
            cont = cont + 1

z1[0] = z1[0] / cont
z1[1] = z1[1] / cont
z1[2] = z1[2] / cont
print('C1: ', z1)

# Calculo del centroide de zona boscosa o C2
img = cv2.imread('./image/boscosa.png', 1)
cont = 0
contx = 0
z2 = [0, 0, 0]
c2=[]
# Obtener el numero de pixeles en la zona
for i in range(hgt):
    for d in range(wid):
        pixel = img[i, d]
        pixel2 = img2[i, d]
        if int(pixel[0]) * int(pixel2[0]) == 0:
            contx = contx + 1
            c2.append([i,d])

# obtener el centroide considerando el 80% de pixeles
for i in range(hgt):
    for d in range(wid):
        pixel = img[i, d]
        pixel2 = img2[i, d]
        if int(pixel[0]) * int(pixel2[0]) == 0 and cont < contx * .8:
            z2[0] = z2[0] + pixel2[0]
            z2[1] = z2[1] + pixel2[1]
            z2[2] = z2[2] + pixel2[2]
            cont = cont + 1

z2[0] = z2[0] / cont
z2[1] = z2[1] / cont
z2[2] = z2[2] / cont
print('C2: ', z2)

# Calculo del centroide de zona suelo o C3
img = cv2.imread('./image/suelo.png', 1)
cont = 0
contx = 0
z3 = [0, 0, 0]
c3=[]
# Obtener el numero de pixeles en la zona
for i in range(hgt):
    for d in range(wid):
        pixel = img[i, d]
        pixel2 = img2[i, d]
        if int(pixel[0]) * int(pixel2[0]) == 0:
            contx = contx + 1
            c3.append([i,d])

# obtener el centroide considerando el 80% de pixeles
for i in range(hgt):
    for d in range(wid):
        pixel = img[i, d]
        pixel2 = img2[i, d]
        if int(pixel[0]) * int(pixel2[0]) == 0 and cont < contx * .8:
            z3[0] = z3[0] + pixel2[0]
            z3[1] = z3[1] + pixel2[1]
            z3[2] = z3[2] + pixel2[2]
            cont = cont + 1

z3[0] = z3[0] / cont
z3[1] = z3[1] / cont
z3[2] = z3[2] / cont
print('C3: ', z3)

def tasaError():
    print("DISTANCIA INFINITO")
    ci,bos,sue=0,0,0
    nn=0
    for i in range(hgt):
        for d in range(wid):
            pixel=img2[i,d]
            a=clasificarInfinito(int(pixel[0]), int(pixel[1]), int(pixel[2]), z1, z2, z3)
            if a == "Zona cielo":
                if [i,d] in c1:
                    ci=ci+1
            if a == "Zona boscosa":
                if [i,d] in c2:
                    bos=bos+1
            if a == "Zona suelo":
                if [i,d] in c3:
                    sue=sue+1

    print("Clasificaciones correctas", "\nZona cielo: ", ci,"\nZona cielo: ",bos,"\nZona suelo: ", sue)
    print("´Porcentaje de error: ", (((72044-(ci+bos+sue))/72044)*100))
    print("Total clasificaciones correctas: ", ci+bos+sue)

# clasificador_insertar imprime la clase del pixel ingresado
def clasificador_insertar():
    pixel = input('Ingresa el valor RGB del pixel, Ejem. 12 24 123: ').split(' ')
    clases = clasificarCityBlock(int(pixel[0]), int(pixel[1]), int(pixel[2]), z1, z2, z3)
    print(f"DISTANCIA CITY BLOCK: {pixel}: {clases}")
    clases = clasificarEuclidiana(int(pixel[0]), int(pixel[1]), int(pixel[2]), z1, z2, z3)
    print(f"DISTANCIA EUCLIDIANA: {pixel}: {clases}")
    clases = clasificarInfinito(int(pixel[0]), int(pixel[1]), int(pixel[2]), z1, z2, z3)
    print(f"DISTANCIA INFINITO: {pixel}: {clases}")
    print('*****************')
# clasificador_click imprime la clase del pixel de la imagen en el que hace clic
def clasificador_clic(event, x, y, flags, param):

    if (event == 1):
        r,g,b = param[y,x]
        clase = clasificarCityBlock(r,g,b,z1,z2,z3)
        print(f"DISTANCIA CITY BLOCK: {x},{y}: {param[y,x]}: {clase}",z1,z2,z3)
        clase = clasificarEuclidiana(r, g, b,z1,z2,z3)
        print(f"DISTANCIA EUCLIDIANA: {x},{y}: {param[y, x]}: {clase}")
        clase = clasificarInfinito(r, g, b,z1,z2,z3)
        print(f"DISTANCIA INFINITO: {x},{y}: {param[y, x]}: {clase}")
        print('*****************')
    if (event == 0):
        r,g,b = param[y,x]
        clase = clasificarCityBlock(r,g,b,z1,z2,z3)
        print(f"DISTANCIA CITY BLOCK: {x},{y}: {param[y,x]}: {clase}")
        clase = clasificarEuclidiana(r, g, b,z1,z2,z3)
        print(f"DISTANCIA EUCLIDIANA: {x},{y}: {param[y, x]}: {clase}")
        clase = clasificarInfinito(r, g, b,z1,z2,z3)
        print(f"DISTANCIA INFINITO: {x},{y}: {param[y, x]}: {clase}")
        print('*****************')

class Imagen():
    def __init__(self, nombre, tipo):
        self._imagen = cv2.imread(nombre, tipo)

    def abrir(self):
        cv2.imshow("imagen", self._imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def clasificador_clic(self):
        cv2.namedWindow("imagen")

        cv2.setMouseCallback("imagen", clasificador_clic, param=self._imagen)
        while True:
            cv2.imshow("imagen", self._imagen)
            # Para salir del bucle presionar la tecla Esc la cula tiene el valor ASCII = 27
            # de lo contrario la ventana se seguira abriendo sin fin
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
    def clasificador_insertar(self):
        clasificador_insertar()
    def valor_pixel(self, x, y):
        # Devolvemos el valor rgb de en formato [r,g,b] del pixel[x,y]
        return self._imagen[y, x]
