# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
# sarios para resolver las tareas, listadas a continuación:

#h. debe utilizar un grafo no dirigido.

from graph import Graph
from tarea import Tarea
import math

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
                  
def camino_corto_a_impresora(grafo):

    pcs = ["Manjaro", "Red Hat", "Fedora"]    
    resultados = {}   
    
    for pc in pcs:
        path = grafo.dijkstra(pc) #todos los caminos mas cortos a pc
        destination = 'Impresora'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0: #mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination: #chequea hasta que sea la impresora
                if peso_total is None:
                    peso_total = value[1] #añade el peso
                camino_completo.append(value[0]) #añade la impresora al camino
                destination = value[2] #añade el predecesor de la impresora y vuelve a hacer esto
        
        camino_completo.reverse() #Lo inverte para que sea de pc a impresora

        resultados[pc] = { #Aca construye el camino
            "camino": camino_completo,
            "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


# d. encontrar el árbol de expansión mínima;
def arbol_expansion_minima(red, vertice):
    expansion_tree = red.kruskal(vertice)

    peso_total = 0
    for edge in expansion_tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"Origin: {origin} - Destination: {destination}")
        peso_total += int(weight)
    print(f"Peso total: {peso_total}")

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;

def camino_corto_pc_a_guarani(grafo):
    pcs = ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"]    
    pc_mas_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf
    
    for pc in pcs:
        path = grafo.dijkstra(pc)
        destination = 'Guarani'
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

        # Solo guardar si es la más cercana
        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            pc_mas_cercana = pc
            mejor_resultado = {
                pc: {
                    "camino": camino_completo,
                    "distancia": peso_total
                }
            }
    
    return mejor_resultado if pc_mas_cercana else False

# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;

def camino_corto_switch1_a_mongodb(grafo):
    pcs = ["Ubuntu", "Mint"]    
    pc_mas_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf
    
    for pc in pcs:
        path = grafo.dijkstra(pc)
        destination = 'MongoDB'
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

        # Solo guardar si es la más cercana
        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            pc_mas_cercana = pc
            mejor_resultado = {
                pc: {
                    "camino": camino_completo,
                    "distancia": peso_total
                }
            }
    
    return mejor_resultado if pc_mas_cercana else False


# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
def cambiar_conexion_impresora(red):
    # Eliminar conexión actual de la impresora con Switch1
    red.delete_edge("Impresora", "Switch1", 'value')
    
    # Agregar nueva conexión de la impresora con Router2
    red.insert_edge("Impresora", "Router2", 15)
    
    #lo llamo de nuevo a la nueva conexion
    barridos_desde_notebooks(red)

        

#MAIN:
crear_red()
# red.show()
print()
barridos_desde_notebooks(red)
print()
print("Camino mas corto de cada uno (Manjaro, Red Hat, Fedora) hasta impresora:")
print(camino_corto_a_impresora(red))
print()
print("Arbol de expansion minima (importa siempre el peso) desde impresora por ejemplo:")
print(arbol_expansion_minima(red,"Impresora")) #aca eligo desde impresora por ejemplo
print()
resultado=camino_corto_pc_a_guarani(red)
print(f"El camino más corto hasta el servidor “Guaraní” entre las PCs es: {resultado}")
print()
resultado1=camino_corto_switch1_a_mongodb(red)
print(f"El camino mas corto indicar de las computadora del switch 01 al servidor “MongoDB” es: {resultado1}")
print()
print("Conexión cambiada: Impresora ahora conectada a Router2: ")
print(cambiar_conexion_impresora(red))