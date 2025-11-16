# 9. Implementar un grafo no dirigido que permita administrar vuelos internacionales contem-
# plando los siguientes requerimientos:

from graph import Graph
from clasesAV import Aeropuerto, Vuelo
import math

grafo = Graph(is_directed=False) 

# a. de cada aeropuerto se conoce: su nombre, ubicación (latitud y longitud) y cantidad de pis-
# tas;

# d. el grafo debe contener los aeropuertos de los siguientes países: Argentina, China, Brasil,
# Tailandia, Grecia, Alemania, Francia, Estados Unidos, Japón y Jamaica;
def cargar_aeropuertos(graph):
    graph.insert_vertex("Argentina", Aeropuerto("Argentina", -34.6, -58.4, 3))
    graph.insert_vertex("China", Aeropuerto("China", 39.9, 116.4, 4))
    graph.insert_vertex("Brasil", Aeropuerto("Brasil", -23.5, -46.6, 3))
    graph.insert_vertex("Tailandia", Aeropuerto("Tailandia", 13.7, 100.5, 2))
    graph.insert_vertex("Grecia", Aeropuerto("Grecia", 37.9, 23.7, 2))
    graph.insert_vertex("Alemania", Aeropuerto("Alemania", 52.5, 13.4, 4))
    graph.insert_vertex("Francia", Aeropuerto("Francia", 48.8, 2.3, 4))
    graph.insert_vertex("Estados Unidos", Aeropuerto("Estados Unidos", 38.9, -77.0, 5))
    graph.insert_vertex("Japón", Aeropuerto("Japón", 35.6, 139.7, 3))
    graph.insert_vertex("Jamaica", Aeropuerto("Jamaica", 18.0, -76.8, 2))


# b. cada arista representa un viaje de un aeropuerto a otro, en cada una de esta puede haber más de un vuelo, de los cuales se conoce: hora de salida, hora de arribo, nombre de la em-
# presa, costo del pasaje –considere que todos los pasajes cuestan lo mismo–, duración del
#viaje y distancia en km;

def cargar_vuelos(graph):

    # =====================================================
    # Argentina ↔ Brasil
    # =====================================================
    vuelos_AB = [
        Vuelo("08:00", "11:00", "LATAM", 500, 3, 2200),
        Vuelo("18:00", "21:00", "Aerolíneas", 500, 3, 2200)
    ]

    graph.insert_edge("Argentina", "Brasil", 2200)

    posA = graph.search("Argentina", "value")
    for edge in graph[posA].edges:
        if edge.value == "Brasil":
            edge.other_values = vuelos_AB

    posB = graph.search("Brasil", "value")
    for edge in graph[posB].edges:
        if edge.value == "Argentina":
            edge.other_values = vuelos_AB


    # =====================================================
    # Brasil ↔ Estados Unidos
    # =====================================================
    vuelos_BE = [
        Vuelo("06:00", "16:00", "Delta", 1500, 10, 6800)
    ]

    graph.insert_edge("Brasil", "Estados Unidos", 6800)

    posB = graph.search("Brasil", "value")
    for edge in graph[posB].edges:
        if edge.value == "Estados Unidos":
            edge.other_values = vuelos_BE

    posE = graph.search("Estados Unidos", "value")
    for edge in graph[posE].edges:
        if edge.value == "Brasil":
            edge.other_values = vuelos_BE


    # =====================================================
    # Estados Unidos ↔ Francia
    # =====================================================
    vuelos_EF = [
        Vuelo("13:00", "22:00", "Air France", 1200, 9, 6200)
    ]

    graph.insert_edge("Estados Unidos", "Francia", 6200)

    posE = graph.search("Estados Unidos", "value")
    for edge in graph[posE].edges:
        if edge.value == "Francia":
            edge.other_values = vuelos_EF

    posF = graph.search("Francia", "value")
    for edge in graph[posF].edges:
        if edge.value == "Estados Unidos":
            edge.other_values = vuelos_EF


    # =====================================================
    # Francia ↔ Alemania (FALTABA)
    # =====================================================
    vuelos_FA = [
        Vuelo("09:00", "11:00", "Lufthansa", 300, 2, 900)
    ]

    graph.insert_edge("Francia", "Alemania", 900)

    posF = graph.search("Francia", "value")
    for edge in graph[posF].edges:
        if edge.value == "Alemania":
            edge.other_values = vuelos_FA

    posAlem = graph.search("Alemania", "value")
    for edge in graph[posAlem].edges:
        if edge.value == "Francia":
            edge.other_values = vuelos_FA


    # =====================================================
    # Alemania ↔ Grecia
    # =====================================================
    vuelos_AG = [
        Vuelo("07:00", "09:30", "Aegean", 400, 2.5, 1800)
    ]

    graph.insert_edge("Alemania", "Grecia", 1800)

    posAlem = graph.search("Alemania", "value")
    for edge in graph[posAlem].edges:
        if edge.value == "Grecia":
            edge.other_values = vuelos_AG

    posG = graph.search("Grecia", "value")
    for edge in graph[posG].edges:
        if edge.value == "Alemania":
            edge.other_values = vuelos_AG


    # =====================================================
    # Grecia ↔ Tailandia
    # =====================================================
    vuelos_GT = [
        Vuelo("22:00", "10:00", "Thai Airways", 1100, 12, 7500)
    ]

    graph.insert_edge("Grecia", "Tailandia", 7500)

    posG = graph.search("Grecia", "value")
    for edge in graph[posG].edges:
        if edge.value == "Tailandia":
            edge.other_values = vuelos_GT

    posT = graph.search("Tailandia", "value")
    for edge in graph[posT].edges:
        if edge.value == "Grecia":
            edge.other_values = vuelos_GT


    # =====================================================
    # Japón ↔ China
    # =====================================================
    vuelos_JC = [
        Vuelo("10:00", "14:30", "China Air", 700, 4.5, 2100)
    ]

    graph.insert_edge("Japón", "China", 2100)

    posJ = graph.search("Japón", "value")
    for edge in graph[posJ].edges:
        if edge.value == "China":
            edge.other_values = vuelos_JC

    posC = graph.search("China", "value")
    for edge in graph[posC].edges:
        if edge.value == "Japón":
            edge.other_values = vuelos_JC


    # =====================================================
    # Jamaica ↔ Estados Unidos
    # =====================================================
    vuelos_JE = [
        Vuelo("09:00", "13:00", "JetBlue", 450, 4, 2400)
    ]

    graph.insert_edge("Jamaica", "Estados Unidos", 2400)

    posJm = graph.search("Jamaica", "value")
    for edge in graph[posJm].edges:
        if edge.value == "Estados Unidos":
            edge.other_values = vuelos_JE

    posE = graph.search("Estados Unidos", "value")
    for edge in graph[posE].edges:
        if edge.value == "Jamaica":
            edge.other_values = vuelos_JE


# e. calcular el camino más corto desde el aeropuerto de Argentina a Tailandia considerando
# los siguientes criterios:
# I. menor distancia,
# II. menor duración de tiempo,
# III. menor costo,
# IV. menor número de escalas.
def camino_corto_criterios(graph):

    criterios = ["distancia", "duracion", "costo", "escalas"]
    resultados = {}

    for criterio in criterios:

        # Cambiar los pesos según criterio
        for vertex in graph:
            for edge in vertex.edges:

                vuelos = edge.other_values   # lista de vuelos

                if criterio == "distancia":
                    edge.weight = vuelos[0].distancia     

                elif criterio == "duracion":
                    edge.weight = vuelos[0].duracion       

                elif criterio == "costo":
                    edge.weight = vuelos[0].costo        

                elif criterio == "escalas":
                    edge.weight = 1               


        # Ejecutar Dijkstra
        path = graph.dijkstra("Argentina")

        # Reconstruir camino a Tailandia
        destino = "Tailandia"
        peso_total = None
        camino_completo = []

        while path.size() > 0:
            value = path.pop()

            if value[0] == destino:
                if peso_total is None:
                    peso_total = value[1]

                camino_completo.append(value[0])
                destino = value[2]

        camino_completo.reverse()

        resultados[criterio] = {
            "camino": camino_completo,
            "valor_total": peso_total
        }

    return resultados

# f. determinar todos los aeropuertos a los que se puede arribar desde Grecia de manera direc-
# ta o indirecta.      
def aeropuertos_alcanzables_desde_grecia(graph):
    inicio = "Grecia"
    visitados = []
    cola = [inicio]

    while cola:
        actual = cola.pop(0)

        if actual not in visitados:
            visitados.append(actual)

            pos = graph.search(actual, "value")
            if pos is not None:
                for edge in graph[pos].edges:
                    destino = edge.value
                    if destino not in visitados:
                        cola.append(destino)

    # Eliminamos Grecia
    visitados.remove(inicio)

    print("Aeropuertos alcanzables desde Grecia:")
    for aeropuerto in visitados:
        print("-", aeropuerto)

    return visitados


#MAIN:
cargar_aeropuertos(grafo)
cargar_vuelos(grafo)
# grafo.show()
print()
print("Camino mas corto desde el aeropuerto de Argentina a Tailandia considerandolos siguientes criterios (I. menor distancia, II. menor duración de tiempo,III. menor costo, IV. menor número de escalas):\n")
print(camino_corto_criterios(grafo))
print()
aeropuertos_alcanzables_desde_grecia(grafo)
