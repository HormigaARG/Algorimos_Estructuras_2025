# 4. Un empresa de telefonía celular dispone de la información de sus antenas, de las cuales se
# conoce: su ubicación (latitud y longitud), código de identificación, velocidad de transferencia
# en megabytes/segundos, y además las antenas a las que transmite y las distancias a cada una de
# estas. Implementar un algoritmo que permita resolver los siguientes requerimientos:

from graph import Graph
from antena import Antena

# a. utilizar un grafo no dirigido;
grafo = Graph(is_directed=False) 


# b. cargar la información de antenas y la relación con las demás;
def cargar_antenas(graph):
    graph.insert_vertex("TGK783", Antena("TGK783", -32.5, -68.5, 180))
    graph.insert_vertex("MZACAPITAL", Antena("MZACAPITAL", -32.89, -68.83, 250))
    graph.insert_vertex("MSNCAPITAL", Antena("MSNCAPITAL", -27.37, -55.89, 190))
    graph.insert_vertex("NQN100", Antena("NQN100", -38.95, -68.06, 210))
    graph.insert_vertex("SLT220", Antena("SLT220", -24.78, -65.41, 170))
    
def cargar_conexiones(graph):
    graph.insert_edge("MZACAPITAL", "SLT220", 450) #MZA: MENDOZA
    graph.insert_edge("SLT220", "MSNCAPITAL", 820) #MSN: MISIONES
    graph.insert_edge("MZACAPITAL", "NQN100", 460)
    graph.insert_edge("NQN100", "MSNCAPITAL", 1500)
    graph.insert_edge("MZACAPITAL", "TGK783", 100)
    graph.insert_edge("SLT220","TGK783", 145)


# c. determinar el tamaño del grafo;
def determinar_tamano_grafo(graph):
    cantidad_vertices = len(graph) #PD: ME PARECE QUE NO SE REFIERE A LA CANTIDAD DE VERTICES, PORQUE ESO SERIA EL ORDEN DEL VERTICE (PERO LO CALCULO POR LAS DUDAS)

    # como es grafo NO dirigido, contamos cada arista solo 1 vez
    cantidad_aristas = 0
    for vertex in graph:
        cantidad_aristas += len(vertex.edges)

    # como el grafo NO es dirigido se cargan aristas duplicadas (A–B y B–A)
    cantidad_aristas //= 2
    print(f"Cantidad de vértices: {cantidad_vertices}")
    print(f"Cantidad de aristas: {cantidad_aristas}")

# d. determinar el camino más corto para transmitir desde la antena ubicada en la capital de
# Mendoza a la antena ubicada en la capital de Misiones, utilizando el algoritmo de Dijkstra;      
def camino_corto(graph):
    path = graph.dijkstra('MZACAPITAL')
    destination = 'MSNCAPITAL'
    peso_total = None
    camino_completo = []

    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()
    print(f'El camino mas corto de la antena de Mendoza al de la antena de Misiones es: {"-".join(camino_completo)} con un costo de {peso_total}')

# e. encontrar el árbol de expansión mínimo del grafo, utilizando Prim o Kruskal;
#Lo hago con Kruskal porque es el único que dimos

def arbol_expansion_minima(graph, vertice): #<-------- NO ME ANDA EL PUNTO E) NO SE PORQUE
    expansion_tree = graph.kruskal(vertice)

    peso_total = 0
    print(f"Árbol de expansión mínima de {vertice}")

    for edge in expansion_tree.split(';'):
        partes = edge.split('-')

        # Ignorar entradas inválidas
        if len(partes) != 3:
            continue

        origin, destination, weight = partes
        print(f"Origen: {origin} - Destino: {destination} - Peso: {weight}")

        peso_total += int(weight)

    print(f"\nPeso total del árbol: {peso_total}")

# f. determinar si la antena con código “TGK-783” existe, de ser así mostrar toda su información.
def determinar_antena(graph):
    codigo = "TGK783"

    pos = graph.search(codigo, "value")   # busca el vértice por su código

    if pos is not None:
        print(f"La antena con codigo {codigo} existe. Información completa:")
        print(graph[pos].other_values)    # muestra el objeto Antena
    else:
        print(f"La antena con código {codigo} no existe en el grafo.")


#MAIN:
cargar_antenas(grafo)
cargar_conexiones(grafo)
# grafo.show()
determinar_tamano_grafo(grafo)
print()
camino_corto(grafo)
print()
arbol_expansion_minima(grafo,"MZACAPITAL") #elijo a cualquiera
print()
determinar_antena(grafo)



