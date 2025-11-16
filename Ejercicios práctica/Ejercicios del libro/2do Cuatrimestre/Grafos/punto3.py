# 3. Implementar un grafo no dirigido que permita cargar puertos y las aristas que conecten dichos
# puertos, que permita resolver las siguientes tareas:

from graph import Graph
grafo = Graph(is_directed=False)

# a. Insertar puertos (vértices)
def insertar_vertex(graph):
    # Puertos del sistema
    graph.insert_vertex("puerto Madero")
    graph.insert_vertex("puerto Lomas")
    graph.insert_vertex("puerto Belgrano")
    graph.insert_vertex("puerto Delta")
    graph.insert_vertex("puerto Rodas")
    graph.insert_vertex("puerto Sur")

# a. Insertar aristas con distancia entre puertos
def insertar_aristas(graph):
    # Conexiones con distancias en km (ejemplo)
    graph.insert_edge("puerto Madero", "puerto Lomas", 20)
    graph.insert_edge("puerto Madero", "puerto Belgrano", 15)
    graph.insert_edge("puerto Madero", "puerto Sur", 40)
    graph.insert_edge("puerto Belgrano", "puerto Delta", 18)
    graph.insert_edge("puerto Lomas", "puerto Delta", 22)
    graph.insert_edge("puerto Delta", "puerto Rodas", 30)
    graph.insert_edge("puerto Belgrano", "puerto Sur", 25)
    graph.insert_edge("puerto Sur", "puerto Rodas", 14)

# b. realizar un barrido en profundidad desde el primer puerto en el grafo;
def barrido_profundidad(graph):
    graph.deep_sweep("puerto Madero")
    
# c. determinar el camino más corto desde puerto Madero al puerto de Rodas;
def camino_corto(graph):
    path = graph.dijkstra('puerto Madero')
    destination = 'puerto Rodas'
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
    print(f'El camino mas corto de puerto Madero al puerto Rodas es: {"-".join(camino_completo)} con un costo de {peso_total}')

def eliminar_mayor_conexiones(grafo):
    if len(grafo) == 0:
        print("El grafo está vacío")
        return None

    max_aristas = -1
    puerto_max = None

    for vertex in grafo:
        cantidad = len(vertex.edges)
   
        if cantidad > max_aristas:
            max_aristas = cantidad
            puerto_max = vertex.value

    print(f"El puerto con más conexiones es: {puerto_max} ({max_aristas} aristas)")
    grafo.delete_vertex(puerto_max, 'value')
    print(f"Puerto '{puerto_max}' eliminado correctamente.")

#MAIN:
insertar_vertex(grafo)
insertar_aristas(grafo)
# grafo.show()
print("Barrido en profundidad desde el primer puerto en el grafo (puerto Madero):")
barrido_profundidad(grafo)
print()
camino_corto(grafo)
print()
eliminar_mayor_conexiones(grafo)


