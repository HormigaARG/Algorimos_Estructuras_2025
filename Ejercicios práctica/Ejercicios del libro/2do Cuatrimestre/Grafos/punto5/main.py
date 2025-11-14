# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
# sarios para resolver las tareas, listadas a continuación:

#h. debe utilizar un grafo no dirigido.

from graph import Graph
from tarea import Tarea

red = Graph(is_directed=False)


# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
# dor, router, switch, impresora;
def crear_red():
       
    # Crear vértices usando la clase Tarea
    red.insert_vertex("Red Hat", Tarea("Red Hat", "notebook"))
    red.insert_vertex("Debian", Tarea("Debian", "notebook"))
    red.insert_vertex("Arch", Tarea("Arch", "notebook"))
    red.insert_vertex("Manjaro", Tarea("Manjaro", "pc"))
    red.insert_vertex("Fedora", Tarea("Fedora", "pc"))
    red.insert_vertex("Impresora", Tarea("Impresora", "impresora"))
    red.insert_vertex("Guarani", Tarea("Guarani", "servidor"))
    red.insert_vertex("Switch1", Tarea("Switch1", "switch"))
    red.insert_vertex("Switch2", Tarea("Switch2", "switch"))
    red.insert_vertex("MongoDB", Tarea("MongoDB", "servidor"))
    red.insert_vertex("Ubuntu", Tarea("Ubuntu", "pc"))
    red.insert_vertex("Mint", Tarea("Mint", "pc"))
    red.insert_vertex("Router1", Tarea("Router1", "router"))
    red.insert_vertex("Router2", Tarea("Router2", "router"))
    red.insert_vertex("Router3", Tarea("Router3", "router"))
    red.insert_vertex("Parrot", Tarea("Parrot", "pc"))
    
    # Establecer conexiones
    conexiones = [
        ("Ubuntu", "Switch1", 18),
        ("Impresora", "Switch1", 22),
        ("Mint", "Switch1", 80),
        ("Debian", "Switch1", 17),
        ("Switch1", "Router1", 29),
        ("Router1", "Router2", 37),
        ("Router1", "Router3", 43),
        ("Router2", "Router3", 50),
        ("Router2", "Guarani", 9),
        ("Router2", "Red Hat", 25),
        ("Router3", "Switch2", 61),
        ("Switch2", "Fedora", 3),
        ("Switch2", "Arch", 56),
        ("Switch2", "Manjaro", 40),
        ("Switch2", "Parrot", 12),
        ("Switch2", "MongoDB", 5)
    ]
    
    for origen, destino, peso in conexiones:
        red.insert_edge(origen, destino, peso)
    
    return red


# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
def barridos_desde_notebooks(red):
    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        print()
        print(f"BARRIDO EN PROFUNDIDAD DESDE: {notebook}")
        red.deep_sweep(notebook)
        print()
        print(f"BARRIDO EN AMPLITUD DESDE: {notebook}")
        red.amplitude_sweep(notebook)
        print()

# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
def camino_corto_a_impresora(red):
    equipos = ["Manjaro", "Red Hat", "Fedora"]
    destino = "Impresora"
    
    print(f"CAMINO MÁS CORTO A IMPRESORA: ")
    
    for equipo in equipos:
        print(f"Desde {equipo} a Impresora")
        
        # Obtener el camino más corto usando Dijkstra
        path = red.dijkstra(equipo)
        
        # Reconstruir camino específico a Impresora
        peso_total = None
        camino_completo = []
        
        # Volcar a una lista temporal
        temp_stack = []
        while path.size() > 0:
            temp_stack.append(path.pop())
        
        # Buscar el destino en los resultados
        for value in temp_stack:
            if value[0] == destino:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                # Reconstruir camino hacia atrás
                current = value[2]
                while current is not None:
                    camino_completo.insert(0, current)
                    found = False
                    for v in temp_stack:
                        if v[0] == current:
                            current = v[2]
                            found = True
                            break
                    if not found:
                        break
                break
        
        if camino_completo:
            print(f"Camino: {' -> '.join(camino_completo)}")
            print(f"Costo total: {peso_total}")
        else:
            print("No se encontró camino")


# d. encontrar el árbol de expansión mínima;
def arbol_expansion_minima(red):
    expansion_tree = red.kruskal("Router1")
    
    print("Árbol de Expansión Mínima del Router 1:")
    aristas = expansion_tree.split(';')
    peso_total = 0
    
    for arista in aristas:
        origen, destino, peso = arista.split('-')
        peso_num = int(peso)
        peso_total += peso_num
        print(f"  {origen} -- {destino} (peso: {peso})")
    
    print(f"Peso total del árbol: {peso_total}")

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
def camino_corto_pc_a_guarani(red):
    pcs = ["Manjaro", "Fedora", "Ubuntu", "Mint", "Parrot"]
    destino = "Guarani"
    
    mejor_pc = None
    mejor_costo = float('inf')
    mejor_camino = []
    
    for pc in pcs:
        path = red.dijkstra(pc)
        
        # Buscar camino a Guarani
        temp_list = []
        while path.size() > 0:
            temp_list.append(path.pop())
        
        for valor in temp_list:
            nombre_vertice = valor[0]
            costo = valor[1]
            
            if nombre_vertice == destino:
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_pc = pc
                    # Reconstruir camino
                    camino = [destino]
                    actual = valor[2]
                    while actual is not None:
                        camino.insert(0, actual)
                        for v in temp_list:
                            if v[0] == actual:
                                actual = v[2]
                                break
                    mejor_camino = camino
                break
    
    print(f"PC con camino más corto a Guarani: {mejor_pc}")
    print(f"Camino: {' -> '.join(mejor_camino)}")
    print(f"Costo total: {mejor_costo}")

# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
def camino_corto_switch1_a_mongodb(red):
    computadoras_switch1 = ["Ubuntu", "Mint", "Debian"]
    destino = "MongoDB"
    
    mejor_computadora = None
    mejor_costo = float('inf')
    mejor_camino = []
    
    for comp in computadoras_switch1:
        path = red.dijkstra(comp)
        
        # Buscar camino a MongoDB
        temp_list = []
        while path.size() > 0:
            temp_list.append(path.pop())
        
        for valor in temp_list:
            nombre_vertice = valor[0]
            costo = valor[1]
            
            if nombre_vertice == destino:
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_computadora = comp
                    # Reconstruir camino
                    camino = [destino]
                    actual = valor[2]
                    while actual is not None:
                        camino.insert(0, actual)
                        for v in temp_list:
                            if v[0] == actual:
                                actual = v[2]
                                break
                    mejor_camino = camino
                break
    
    print(f"Computadora del Switch1 con camino más corto a MongoDB: {mejor_computadora}")
    print(f"Camino: {' -> '.join(mejor_camino)}")
    print(f"Costo total: {mejor_costo}")


# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
def cambiar_conexion_impresora(red):
    # Eliminar conexión actual de la impresora con Switch1
    red.delete_edge("Impresora", "Switch1", 'value')
    
    # Agregar nueva conexión de la impresora con Router2
    red.insert_edge("Impresora", "Router2", 15)
    
    print("Conexión cambiada: Impresora ahora conectada a Router2")
    
    #lo llamo on la nueva conexion
    barridos_desde_notebooks(red)

#MAIN:
crear_red()
red.show()
print()
barridos_desde_notebooks(red)
print()
camino_corto_a_impresora(red)
print()
arbol_expansion_minima(red)
print()
camino_corto_pc_a_guarani(red)
print()
camino_corto_switch1_a_mongodb(red)
print()
cambiar_conexion_impresora(red)