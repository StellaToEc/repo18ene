"""
            Instituto Politecnico Nacional
            Escuela Superior de Cómputo
            Autor: Mondragon Zarate Jesus Alejandro y Martínez Cervantes Xenia Guadalupe
"""
from imagen import Imagen




if __name__ == '__main__':

    variable='si'
    img1 = Imagen('./image/3-regiones.png', 1)
    while variable!='no':
        variable=input("¿Quieres ingresar un patron (si-no)?")
        if(variable!='no'):
            img1.clasificador_insertar()

    img1.clasificador_clic()



