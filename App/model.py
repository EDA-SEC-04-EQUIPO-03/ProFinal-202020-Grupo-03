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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def Estructura():
    try:
        analyzer = {
                    'company': None,
                    }

        analyzer['company'] = m.newMap(numelements=14000,
                                     maptype='CHAINING',
                                     comparefunction=comparecompanie)
        
        
        return analyzer
 except Exception as exp:
        error.reraise(exp, 'model:Analizador')


# Funciones para agregar informacion al grafo

def AddRutaByCompany(estrupa, name, fileline):
    structure=strupa["company"]
    chequearcompa=m.contains(structure, name)
    if chequearcompa:
        entrada=m.get(structure, name)
        stropa=me.getValue(entrada)
    else:
        stropa=newRutaCompany(name)
        m.put(structure, name, stropa)
    lt.addLast(stropa["listacompas"], fileline)

def newRutaCompany(compa):
    dik = {"name":"","listacompas":None,"size":None}
    dik["name"]=compa
    dik["listacompas"]= lt.newList('SINGLE_LINKED', comparecompanie)



# ==============================
# Funciones de consulta
# ==============================

def getCompaTopTaxi(strupa):
    Mayores={"Top1":None,"Top2":None,"Top3":None} #company name
    mayores={"Top1":0,"Top2":0,"Top3":0} #num taxis
    structure=strupa["company"]
    for cada_compa in structure:
        dicc=structure[cada_compa]
        rta=analizarTop(Mayores,dicc)
    return rta

def analizarTop(Top,top,dicc): #names,nums,dicc
    compania=dicc["name"]
    num_taxis=lt.size(dicc["listacompas"])
    if num_taxis>top["Top1"] and (compania != Top["Top1"]) and num_taxis>top["Top2"] and num_taxis>top["Top3"]:
        top["Top1"]=num_taxis
        Top["Top1"]=compania
    elif num_taxis>top["Top2"] and (compania != Top["Top2"]) and num_taxis>top["Top3"] and num_taxis<top["Top1"]: #and Top["Top2"]!=Top["Top1"]
        top["Top2"]=num_taxis
        Top["Top2"]=compania
    elif num_taxis>top["Top3"] and (compania != Top["Top3"]) and num_taxis<top["Top1"] and num_taxis<top["Top2"]: #and Top["Top2"]!=Top["Top1"]
        top["Top3"]=num_taxis
        Top["Top3"]=compania
    return (Top,top)

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================

def comparecompanie(company, entrada):
    companyentry = me.getKey(entrada)
    if (company == companyentry):
        return 0
    elif (company > companyentry):
        return 1
    else:
        return 0