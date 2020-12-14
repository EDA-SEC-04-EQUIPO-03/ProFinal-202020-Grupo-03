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
from DISClib.DataStructures import mapentry as me
from datetime import datetime 
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def Estructura():
    analyzer = {
                'company': None,
                'areacomu': None
                }

    analyzer['company'] = m.newMap(numelements=14000,
                                 maptype='CHAINING',
                                 comparefunction=comparecompanie)
    analyzer['uniones'] = gr.newGraph(datastructure='ADJ_LIST',
                                    directed=True,
                                    size=1000,
                                    comparefunction=compareAreas)
        
    return analyzer


# Funciones para agregar informacion al grafo

def AddRutaByCompany(estrupa, name, fileline):
    structure=estrupa["company"]
    hayviaje= m.contains(structure, name)
    if hayviaje:
        entrada=m.get(structure, name) 
        struc=me.getValue(entrada)  
    else:
        struc=newRutaCompany(name) 
        m.put(structure, name, struc) 
    lt.addLast(struc["listacompas"], fileline)

def newRutaCompany(compa):
    dik = {"name":"","listacompas":None,"size":None}
    dik["name"]=compa
    dik["listacompas"]= lt.newList('SINGLE_LINKED', comparecompanie)

def agregartopstaxi(dicc):
    listanums=[]#num taxis compañias
    listaids=[]#lista id taxis
    listaarreglo=lt.newList('ARRAY_LIST',None)  #lista nombre compañias
    iterator=it.newIterator(dicc["listacompas"])
    while it.hasNext(iterator):
        cada_single=it.next(iterator) #info archivo CSV
            
        if (cada_single["taxi_id"] not in listaids) and (not lt.isPresent(dicc["name"])):
            listanums.append(1)
            listaids.append(cada_single["taxi_id"])
            lt.addLast(listaarreglo,dicc["name"])
        elif (cada_single["taxi_id"] not in listaids) and  lt.isPresent(dicc["name"]):
            pos=hallarposicionarray(listaarreglo,dicc["name"])
            listanums[pos]=listanums[pos]+1
            listaids.append(cada_single["taxi_id"])
    return (listanums, listaarreglo)

def agregartopsservice(dicc):
    listanums=[] #num servicios compañias
    listaarreglo=lt.newList('ARRAY_LIST',None) #lista nombre compañias
    lt.addLast(listaarreglo,dicc["name"]) 
    listanums.append(lt.size(dicc["listacompas"]))
    return (listanums, listaarreglo)

def AddViaje(analyzer,trip):
    #Cada estación se agrega como un vértice al grafo, si es que aún no existe.
    horai=trip["trip_start_timestamp"].hour() 
    horaf=trip["trip_end_timestamp"].hour() 
    minui=trip["trip_start_timestamp"].minute() 
    minuf=trip["trip_end_timestamp"].minute() 
    fechai=horai+minui #h:mm
    fechaf=horaf+minuf #h:mm
    origin = trip['pickup_community_area']+"-"+fechai
    destination = trip['dropoff_community_area']+"-"+fechaf
    duration = float(trip['trip_seconds'])
    addStation(analyzer, origin)
    addStation(analyzer, destination)
    addConnection(analyzer, origin, destination, duration)

def addStation(analyzer, stationid):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(analyzer ["uniones"], stationid):
            gr.insertVertex(analyzer ["uniones"], stationid)
    return analyzer

def addConnection(analyzer, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    promedio=None
    edge = gr.getEdge(analyzer ["uniones"], origin, destination)
    if edge is None:
        gr.addEdge(analyzer["uniones"], origin, destination, duration)
    elif edge is not None and promedio is None:
        numero_viajes=1
        promedio=int(edge["weight"])
        promedio =(promedio*numero_viajes + duration)/(numero_viajes + 1)
        numero_viajes += 1
        edge["weight"]=promedio
    else:
        promedio=int(edge["weight"])
        promedio =(promedio*numero_viajes + duration)/(numero_viajes + 1)
        numero_viajes += 1
        edge["weight"]=promedio
    return analyzer

# ==============================
# Funciones de consulta
# ==============================

def getCompaTopService(strupa,numero):
    structure=strupa["company"]
    for cada_compa in structure:
        dicc=structure[cada_compa]
        tuplilla=agregartopsservice(dicc)
        analizartops(tuplilla, numero)

def getCompaTopTaxi(strupa,numero):
    strukk=strupa["compañy"]
    for cada_compi in strukk:
        dicc=strukk[cada_compi]
        tuplin=agregartopstaxi(dicc)
        analizartops(tuplin, numero)

def analizartops(tuplilla,numero):
    i=0
    while i<numero:
        maxvalue=max(tuplilla(0))
        posicion=tuplilla(0).index(maxvalue)

        valor=tuplilla(0).pop(posicion)
        nombrecompa=lt.getElement(tuplilla(1),posicion+1)
        lt.deleteElement(tuplilla(1),posicion+1)
        print("******************************")
        print(nombrecompa)
        print(str(valor))
        i+=1


def hallarposilesvertex(strupa,Hi,Hf):
    listav=[]
    sacarruta=[]
    estructura=gr.vertices(strupa["uniones"])
    iterator=it.newIterator(estructura)
    while it.hasNext(iterator):
        vertex=it.next(iterator) #cada vertex
        listav.append(vertex)
    listarevisar=crearsecuencia(strupa,int(Hi),int(Hf))
    for posiblehora in listarevisar:
        for posiblevertex in listav:
            if posiblehora in posiblevertex:
                sacarruta.append(posiblevertex)
    return sacarruta

def ruta(strupa,areaInicio, areaFinal):
    ruta = []
    dijsktra = djk.Dijkstra(strupa['graph'],areaInicio)
    if djk.hasPathTo(dijsktra, areaFinal):
        ruta.append(areaInicio)
        ruta_lt = djk.pathTo(dijsktra, areaFinal)
        iterador = it.newIterator(ruta_lt)
        while it.hasNext(iterador):
            element = it.next(iterador)
            ruta.append(element['vertexB'])
    else:
        ruta = 'No hay ruta'
    timet=djk.distTo(dijsktra,areaFinal)
    return (ruta,time)


# ==============================
# Funciones Helper
# ==============================

def hallarposicionarray(arreglar, name):
    i=0
    pos=-1
    while i<lt.size(arreglar):
        if lt.getElement(arreglar,i) in name:
            pos=i
        i+=1
    return pos

def crearsecuencia(strupa,LI,LF):
    i=LI
    lista=[]
    while i <= gr.numEdges(strupa["uniones"]) and i<LF:
        lista.append(str(i))
        if 45 not in i:
            i=i+15
        elif 24 not in i and 45 in i:
            i=i+100
        elif 24 in i and 45 in i:
            i=0
    return lista

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

def compareAreas(stop, keyvaluestop):
    stopcode = str(keyvaluestop['key'])
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1