"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________
filesmall = 'taxi-trips-wrvz-psew-subset-small.csv'
filamedium = 'taxi-trips-wrvz-psew-subset-medium.csv'
filelarge = 'taxi-trips-wrvz-psew-subset-large.csv'
Structure = None
recursionLimit = 20000

# ___________________________________________________
#  Menu principal
# ___________________________________________________

"""
Menu principal
"""

def printmenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información ")
    print("3- Requerimiento #1 ")
    print("4- Requerimiento #2 ")
    print("5- Requerimiento #3 ")

def cargar_info():
    print("¿Preparado para la carga de datos?")
    print("->  Si desea cargar el archivo pequeño marque 1 ")
    print("->  Si desea cargar el archivo mediano marque 2 ")
    print("->  Si desea cargar el archivo grande marque 3 ")
    rta=input("Digite su opción: ")
    if rta ==1:
        controller.loadInfo(cont,filesmall)
    elif rta ==2:
        controller.loadInfo(cont,filamedium)
    elif rta ==3:
        controller.loadInfo(cont,filelarge)
    else:
        print("Opción erronea, no se ha cargado la información")

def Req1():
    print("hola 1")

def Req2():
    print("hola 2")

def Req3():
    print("hola 3")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.iniciar_catalogo()
    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(cargar_info, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(Req1, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 4:
        executiontime = timeit.timeit(Req2, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    elif int(inputs[0]) == 5:
        executiontime = timeit.timeit(Req3, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    else:
        sys.exit(0)
sys.exit(0)