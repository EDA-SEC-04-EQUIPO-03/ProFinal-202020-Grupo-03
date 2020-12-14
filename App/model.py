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
import datetime 
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
                'uniones': None,
                'ids':None
                }

    analyzer['company'] = m.newMap(numelements=14000,
                                 maptype='CHAINING',
                                 comparefunction=comparecompanie)
    analyzer['uniones'] = gr.newGraph(datastructure='ADJ_LIST',
                                    directed=True,
                                    size=1000,
                                    comparefunction=compareAreas)
    analyzer['ids'] = m.newMap(numelements=14000,
                                 maptype='CHAINING',
                                 comparefunction=compareIds)

        
    return analyzer


# Funciones para agregar informacion al grafo

def AddrutaById(strupa, ID, file):
    structure=strupa["ids"]
    existeid= m.contains(structure, ID)
    if existeid:
        entrada=m.get(structure, ID) 
        struc=me.getValue(entrada)  
    else:
        struc=newID(ID) 
        m.put(structure, ID, struc) 
    lt.addLast(struc["listaids"], file)

def newID(ID):
    IDD = {"ID":"","listaids":None,"size":None}
    IDD["ID"]=ID
    IDD["listaids"]= lt.newList('SINGLE_LINKED', compareIds)
    return IDD


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
    return dik

def AddViaje(analyzer,trip):
    #Cada estación se agrega como un vértice al grafo, si es que aún no existe.
    
    a=trip["trip_start_timestamp"].split("T")
    fechai=datetime.time.fromisoformat(a[1])
    #b=trip["trip_end_timestamp"].split("T")
    #fechaf=datetime.time.fromisoformat(b[1])
    
    fechaistr=datetime.time.strftime(fechai,'%H:%M:%S')
    #fechafstr=datetime.time.strftime(fechaf,'%H:%M:%S')
    origin = trip['pickup_community_area']+"-"+fechaistr
    destination = trip['dropoff_community_area']
    if trip['trip_seconds']!="" and trip['trip_seconds']!=" " and trip['trip_seconds']!=None:
        duration = int(float(trip['trip_seconds']))
    else:
        duration=0.0
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

def getCompaTopService(strupa):
    structure=strupa["company"]
    listanums=[] #num servicios compañias
    listaarreglo=lt.newList('ARRAY_LIST',Comparecompanie) #lista nombre compañias
    listallaves=m.keySet(structure)
    iterator=it.newIterator(listallaves)
    while it.hasNext(iterator):
        cada_llave=it.next(iterator)
        entrada=m.get(structure,cada_llave)
        dicc=me.getValue(entrada)
        #tuplilla=agregartopsservice(dicc)
        #analizartops(tuplilla, int(numero))
        lt.addLast(listaarreglo,dicc["name"]) 
        listanums.append(lt.size(dicc["listacompas"]))
    return (listanums,listaarreglo)

def getnumcompas(strupa):
    i=0
    mapa=strupa["company"]
    listakeys=m.keySet(mapa)
    iterator=it.newIterator(listakeys)
    while it.hasNext(iterator):
        cada_llave=it.next(iterator)
        entrada=m.get(mapa,cada_llave)
        dicc=me.getValue(entrada)
        if lt.size(dicc["listacompas"])!=0:
            i+=1
    return i


def getCompaTopTaxi(strupa):
    strukk=strupa["company"]
    listallaves=m.keySet(strukk)
    iterator=it.newIterator(listallaves)
    listanums=[]#num taxis compañias
    listaids=[]#lista id taxis
    listaarreglo=lt.newList('ARRAY_LIST',Comparecompanie)  #lista nombre compañias
    while it.hasNext(iterator):
        cada_llave=it.next(iterator)
        entrada=m.get(strukk,cada_llave)
        dicc=me.getValue(entrada)
        hola(dicc,listaarreglo,listanums,listaids)
        #tuplin=agregartopstaxi(dicc)
    return (listanums,listaarreglo)

def hola(dicc,listaarreglo,listanums,listaids):
    iterator=it.newIterator(dicc["listacompas"])
    while it.hasNext(iterator):
        cada_single=it.next(iterator) #info archivo CSV
        present= not lt.isPresent(listaarreglo,dicc["name"])
        if (cada_single["taxi_id"] not in listaids) and present: 
            listanums.append(1)
            listaids.append(cada_single["taxi_id"])
            lt.addLast(listaarreglo,dicc["name"])
        elif (cada_single["taxi_id"] not in listaids) and  present:
            pos=hallarposicionarray(listaarreglo,dicc["name"])
            listanums[pos]=listanums[pos]+1
            listaids.append(cada_single["taxi_id"])


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

def evaluarrutaslimite(strupa,Ai,H1,Hf):
    listar=[]
    estructura=gr.vertices(strupa["uniones"])
    iterator=it.newIterator(estructura)
    while it.hasNext(iterator):
        vertex=it.next(iterator) #cada vertex
        if H1 in vertex and Ai in vertex:
            listar.append(vertex)
        if Hf in vertex and Ai in vertex:
            listar.append(vertex)
    return listar
            

def ruta(strupa,areaInicio, areaFinal):
    ruta = []
    dijsktra = djk.Dijkstra(strupa['uniones'],areaInicio)
    if djk.hasPathTo(dijsktra, areaFinal):
        ruta.append(areaInicio)
        ruta_lt = djk.pathTo(dijsktra, areaFinal)
        iterador = it.newIterator(ruta_lt)
        while it.hasNext(iterador):
            element = it.next(iterador)
            ruta.append(element['vertexB'])
    else:
        ruta = ["No", "hay", "ruta"]
    timet=djk.distTo(dijsktra,areaFinal)
    return (ruta,timet)





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
            i=i-45
        elif 24 in i and 45 in i:
            i=0
    return lista

def totaltaxis(stru):
    structure=stru["ids"]
    return m.size(structure)


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

def Comparecompanie(company, companyentry):
    if (company == companyentry):
        return 0
    elif (company > companyentry):
        return 1
    else:
        return 0

def compareIds(date1, date2):
    # print(date1, date2)
    date2=str(date2['key'])
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1