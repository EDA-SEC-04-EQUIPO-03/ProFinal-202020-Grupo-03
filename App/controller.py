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

import config as cf
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def iniciar_catalogo():
    catalogo=model.Estructura()
    return catalogo
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadInfo(structure, infofile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    infofile = cf.data_dir + infofile
    input_file = csv.DictReader(open(infofile, encoding="utf-8"),
                                delimiter=",")
    for line in input_file:
        companie=line["company"]
        ids=line["taxi_id"]
        if companie is None:
            line["company"]="LonelyWorker S.A"
            companie="LonelyWorker S.A"
        model.AddRutaByCompany(structure, companie, line)
        if ids is not None:
            model.AddrutaById(structure,ids,line)
        model.AddViaje(structure,line)
    return structure

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getcompataxi(strupa):
    
    return model.getCompaTopTaxi(strupa)

def getcompaservice(strupa):
    return model.getCompaTopService(strupa)


def mejorhorario(strupa,areaInicio,areaFinal,horaInicio,Horafinal):
    #listavertex=model.hallarposilesvertex(strupa,horaInicio,Horafinal)
    evaluarrutaslimite=model.evaluarrutaslimite(strupa,areaInicio,horaInicio,Horafinal)
    timepasado=999999999999999
    print("Evaluando "+str(len(evaluarrutaslimite))+" opciones")
    ruta=["No","existe","ruta","para","ningún","nodo"]
    for cadavertex in evaluarrutaslimite:
        grut=model.ruta(strupa,str(cadavertex),areaFinal)
        if grut[0]!=["No", "hay", "ruta"]:
            if grut[1]<timepasado:
                timepasado=grut[1]
                ruta=grut[0]
    return (ruta,timepasado)

def getcompascontaxi(strupa):
    return model.getnumcompas(strupa)

def totaltaxis(strupa):
    return model.totaltaxis(strupa)