from graph import Graph
from random import sample, choice, randint

grafo= Graph(is_directed=True)

#Grafo con 15 vertices distintos (numeros entre 1 y 100)
valores= sample(range(1, 101), 15)


#insertar vertices con valores unicos
def insertar_vertices(grafo, valores):
    for valor in valores:
        grafo.insert_vertex(valor)

#insertar aristas
def insertar_aristas(grafo, valores):
    
    for i in range(30):
        origen = choice(valores)
        destino = choice(valores)
        peso = randint(1, 100)
        
        grafo.insert_edge(origen, destino, peso)
        
        
#a. primero eliminar los vértices que hayan quedado desconectados, es decir, que ningún otro vértice tenga una arista que lo apunte y que de él no salga ninguna arista;
def eliminar_vertices_desconectados(grafo):
    vertices_a_eliminar = []
    
    for vertice in grafo:
        # Condición 1: Que de él no salga ninguna arista
        aristas_salientes = len(vertice.edges) == 0
        
        # Condición 2: Que ningún otro vértice tenga una arista que lo apunte
        tiene_aristas_entrantes = False
        for otro_vertice in grafo:
            if otro_vertice != vertice:  # No comparar con sí mismo
                for arista in otro_vertice.edges:
                    if arista.value == vertice.value:
                        tiene_aristas_entrantes = True
                        break
                if tiene_aristas_entrantes:
                    break
        
        # Si NO tiene aristas salientes Y NO tiene aristas entrantes
        if aristas_salientes and not tiene_aristas_entrantes:
            vertices_a_eliminar.append(vertice.value)
    
    # Eliminar
    for vertice_valor in vertices_a_eliminar:
        resultado = grafo.delete_vertex(vertice_valor, 'value')
        if resultado is not None:
            print(f"Vértice {vertice_valor} eliminado (desconectado)")
        else:
            print(f"No se pudo eliminar el vértice {vertice_valor}")
    
    return vertices_a_eliminar

#b. determinar el nodo con mayor cantidad de aristas que salen de él, puede ser más de uno;
def nodo_mayor_aristas_salientes(grafo):
    
    if len(grafo) == 0:
        print("El grafo está vacío")
        return []
    
    max_aristas = 0
    vertices_con_max_aristas = []
    
    for vertice in grafo:
        cantidad_aristas = len(vertice.edges)
        
        if cantidad_aristas > max_aristas:
            # Nuevo máximo encontrado
            max_aristas = cantidad_aristas
            vertices_con_max_aristas = [vertice.value]
        elif cantidad_aristas == max_aristas:
            # Mismo máximo, agregar a la lista
            vertices_con_max_aristas.append(vertice.value)
    
    return vertices_con_max_aristas, max_aristas

#c. determinar el nodo con mayor cantidad de aristas que llegan a él, puede ser más de uno;
def vertices_con_mas_aristas_entrantes(grafo):
    if not grafo:
        return [], 0

    # Contar aristas entrantes para cada vértice
    aristas_entrantes = {}  # diccionario de {valor_vertice: cantidad_aristas_entrantes}

    # Inicializar contadores
    for vertice in grafo:
        aristas_entrantes[vertice.value] = 0

    # Contar aristas entrantes
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.value in aristas_entrantes:
                aristas_entrantes[arista.value] += 1

    # Encontrar el máximo
    max_entrantes = max(aristas_entrantes.values())
    vertices_max = []

    for vertice, count in aristas_entrantes.items():
        if count == max_entrantes:
            vertices_max.append(vertice)

    return vertices_max, max_entrantes

# f. determinar cuántos vértices tienen un arista a sí mismo, es decir, un ciclo directo;
def vertices_con_ciclo_directo(grafo):
    vertices_con_ciclo = []
    
    for vertice in grafo:
        # Verificar si alguna arista del vértice apunta a sí mismo
        for arista in vertice.edges:
            if arista.value == vertice.value:
                vertices_con_ciclo.append(vertice.value)
                break  # Solo necesitamos encontrar una arista de ciclo
    
    return vertices_con_ciclo

# g. determinar la arista más larga, indicando su origen, destino y valor –puede ser más de una.
def arista_mas_larga(grafo):
    if not grafo:
        return []
    
    max_peso = 0
    aristas_maximas = []
    
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.weight > max_peso:
                # Nuevo máximo encontrado
                max_peso = arista.weight
                aristas_maximas = [(vertice.value, arista.value, arista.weight)]
            elif arista.weight == max_peso:
                # Mismo máximo, agregar a la lista
                aristas_maximas.append((vertice.value, arista.value, arista.weight))
    
    return aristas_maximas, max_peso

#MAIN:
insertar_vertices(grafo, valores)
vertices_iniciales = len(grafo)
print(f"Vértices iniciales: {vertices_iniciales}")
insertar_aristas(grafo, valores)
print("Los vertices con sus respectivas aristas: ")
grafo.show()
print()
print("Vertices desconectados que son eliminados directamente: ")
vertices_eliminados = eliminar_vertices_desconectados(grafo)

vertices_finales = len(grafo)

if vertices_eliminados:
    print(f"Se eliminaron {len(vertices_eliminados)} vértices: {vertices_eliminados}")
else:
    print("No se encontraron vértices completamente desconectados")
    
print()
vertices_max, cantidad_max = nodo_mayor_aristas_salientes(grafo)
if vertices_max:
    if len(vertices_max) == 1:
        print(f"El vértice {vertices_max[0]} tiene la mayor cantidad de aristas salientes")
        print(f"Cantidad: {cantidad_max} aristas")
    else:
        print(f"Los vértices {vertices_max} tienen la mayor cantidad de aristas salientes")
        print(f"Cantidad: {cantidad_max} aristas cada uno")
print()
vertices_maximos, cantidad = vertices_con_mas_aristas_entrantes(grafo)

print(f"Vertices con mayor cantidad de aristas que llegan a él: {vertices_maximos}")
print(f"Cantidad de aristas entrantes: {cantidad}")
print()

vertices_ciclo = vertices_con_ciclo_directo(grafo)
print(f"Vértices con ciclo directo: {len(vertices_ciclo)}")
print(f"Vértices: {vertices_ciclo}")
print()
aristas_max, peso_max = arista_mas_larga(grafo)
print(f"Arista más larga (peso): {peso_max} ({(len(aristas_max))} aristas)")

print()
#e. contar cuantos vértice componen el grafo, dado que se genera aleatoriamente y se eliminan los vértices que quedan desconectados;
print(f"Vértices iniciales: {vertices_iniciales}")
print(f"Vértices eliminados: {len(vertices_eliminados)}")
print(f"Vértices finales: {vertices_finales}")



