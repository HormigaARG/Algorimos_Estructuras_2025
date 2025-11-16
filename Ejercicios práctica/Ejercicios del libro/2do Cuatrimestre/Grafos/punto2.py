# 2. Sobre el siguiente dígrafo implementar los algoritmos necesarios para resolver las tareas que
# se presentan a continuación:

from graph import Graph



grafo = Graph(is_directed=True)

# a. represéntelo como arreglo de listas de adyacencias y lista de listas de adyacencia (SOLO TENDRIA QUE CARGARLO NOMAS, PORQUE STO NO DIMOS);
def insertar_vertex(graph):
    graph.insert_vertex('A')
    graph.insert_vertex('B')
    graph.insert_vertex('C')
    graph.insert_vertex('D')
    graph.insert_vertex('E')
    
# b. cargue el valor de las etiquetas de todas las aristas;
def insertas_aristas(graph):
    graph.insert_edge('A', 'B', 6)
    graph.insert_edge('A', 'C', 3)
    graph.insert_edge('A', 'E', 8)
    graph.insert_edge('B', 'C', 2)
    graph.insert_edge('C', 'B', 2)
    graph.insert_edge('C', 'D', 5)
    graph.insert_edge('D', 'D', 4)
    graph.insert_edge('E', 'D', 9)
    graph.insert_edge('E', 'B', 15)
    
# c. encuentre el árbol de expansión mínima, para este punto considere el grafo como no dirigido;
def arbol_expansion_minima(graph, vertice):
    expansion_tree = graph.kruskal(vertice)

    peso_total = 0
    for edge in expansion_tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"Origin: {origin} - Destination: {destination}")
        peso_total += int(weight)
    print(f"Peso total: {peso_total}")

# d. agregue un arco de E hasta C;
def agregar_arista(graph):
    graph.insert_edge("E","C",20)
    print("Arco de E->C agregado correctamente")



# e. encuentre el camino más corto de A hasta D.
def camino_corto(graph):
    path = graph.dijkstra('A')
    destination = 'D'
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
    print(f'El camino mas corto de A hasta D es: {"-".join(camino_completo)} con un costo de {peso_total}')
    
#MAIN:
insertar_vertex(grafo)
insertas_aristas(grafo)
# grafo.show()
print()
print("Arbol de expasion minima: ")
arbol_expansion_minima(grafo,"A")
print()
agregar_arista(grafo)
camino_corto(grafo)

