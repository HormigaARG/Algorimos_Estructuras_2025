# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

from graph import Graph
from maravilla import Maravilla

# f. deberá utilizar un grafo no dirigido.
grafo = Graph(is_directed=False) 

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
def cargar_maravillas(graph):

    # ==== Maravillas Arquitectónicas ====
    graph.insert_vertex("Gran Muralla China",
        Maravilla("Gran Muralla China", "China", "arquitectonica"))

    graph.insert_vertex("Petra",
        Maravilla("Petra", "Jordania", "arquitectonica"))

    graph.insert_vertex("Cristo Redentor",
        Maravilla("Cristo Redentor", "Brasil", "arquitectonica"))

    graph.insert_vertex("Machu Picchu",
        Maravilla("Machu Picchu", "Perú", "arquitectonica"))

    graph.insert_vertex("Chichén Itzá",
        Maravilla("Chichén Itzá", "México", "arquitectonica"))

    graph.insert_vertex("Coliseo Romano",
        Maravilla("Coliseo Romano", "Italia", "arquitectonica"))

    graph.insert_vertex("Taj Mahal",
        Maravilla("Taj Mahal", "India", "arquitectonica"))

    # ==== Maravillas Naturales ====
    graph.insert_vertex("Amazonas",
        Maravilla("Amazonas", ["Brasil", "Perú", "Colombia"], "natural"))

    graph.insert_vertex("Bahía de Ha-Long",
        Maravilla("Bahía de Ha-Long", "Vietnam", "natural"))

    graph.insert_vertex("Cataratas del Iguazú",
        Maravilla("Cataratas del Iguazú", ["Brasil", "Argentina"], "natural"))

    graph.insert_vertex("Montaña de la Mesa",
        Maravilla("Montaña de la Mesa", "Sudáfrica", "natural"))

    graph.insert_vertex("Jeju",
        Maravilla("Jeju", "Corea del Sur", "natural"))

    graph.insert_vertex("Río Subterráneo de Puerto Princesa",
        Maravilla("Río Subterráneo de Puerto Princesa", "Filipinas", "natural"))

    graph.insert_vertex("Parque Nacional de Komodo",
        Maravilla("Parque Nacional de Komodo", "Indonesia", "natural"))

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
def cargar_conexiones(graph):

    # ==== ARQUITECTÓNICAS ====

    graph.insert_edge("Gran Muralla China", "Petra", 4200)
    graph.insert_edge("Gran Muralla China", "Cristo Redentor", 17600)
    graph.insert_edge("Gran Muralla China", "Machu Picchu", 17700)
    graph.insert_edge("Gran Muralla China", "Chichén Itzá", 13200)
    graph.insert_edge("Gran Muralla China", "Coliseo Romano", 8100)
    graph.insert_edge("Gran Muralla China", "Taj Mahal", 3800)

    graph.insert_edge("Petra", "Cristo Redentor", 11200)
    graph.insert_edge("Petra", "Machu Picchu", 13400)
    graph.insert_edge("Petra", "Chichén Itzá", 12200)
    graph.insert_edge("Petra", "Coliseo Romano", 2400)
    graph.insert_edge("Petra", "Taj Mahal", 4200)

    graph.insert_edge("Cristo Redentor", "Machu Picchu", 3300)
    graph.insert_edge("Cristo Redentor", "Chichén Itzá", 7000)
    graph.insert_edge("Cristo Redentor", "Coliseo Romano", 9000)
    graph.insert_edge("Cristo Redentor", "Taj Mahal", 14000)

    graph.insert_edge("Machu Picchu", "Chichén Itzá", 4200)
    graph.insert_edge("Machu Picchu", "Coliseo Romano", 10400)
    graph.insert_edge("Machu Picchu", "Taj Mahal", 17100)

    graph.insert_edge("Chichén Itzá", "Coliseo Romano", 9400)
    graph.insert_edge("Chichén Itzá", "Taj Mahal", 14800)

    graph.insert_edge("Coliseo Romano", "Taj Mahal", 6600)


    # ==== NATURALES ====

    graph.insert_edge("Amazonas", "Bahía de Ha-Long", 16100)
    graph.insert_edge("Amazonas", "Cataratas del Iguazú", 3000)
    graph.insert_edge("Amazonas", "Montaña de la Mesa", 9500)
    graph.insert_edge("Amazonas", "Jeju", 16500)
    graph.insert_edge("Amazonas", "Río Subterráneo de Puerto Princesa", 17500)
    graph.insert_edge("Amazonas", "Parque Nacional de Komodo", 15700)

    graph.insert_edge("Bahía de Ha-Long", "Cataratas del Iguazú", 17800)
    graph.insert_edge("Bahía de Ha-Long", "Montaña de la Mesa", 12200)
    graph.insert_edge("Bahía de Ha-Long", "Jeju", 2600)
    graph.insert_edge("Bahía de Ha-Long", "Río Subterráneo de Puerto Princesa", 1600)
    graph.insert_edge("Bahía de Ha-Long", "Parque Nacional de Komodo", 3000)

    graph.insert_edge("Cataratas del Iguazú", "Montaña de la Mesa", 7800)
    graph.insert_edge("Cataratas del Iguazú", "Jeju", 18200)
    graph.insert_edge("Cataratas del Iguazú", "Río Subterráneo de Puerto Princesa", 19300)
    graph.insert_edge("Cataratas del Iguazú", "Parque Nacional de Komodo", 17400)

    graph.insert_edge("Montaña de la Mesa", "Jeju", 14400)
    graph.insert_edge("Montaña de la Mesa", "Río Subterráneo de Puerto Princesa", 13500)
    graph.insert_edge("Montaña de la Mesa", "Parque Nacional de Komodo", 11100)

    graph.insert_edge("Jeju", "Río Subterráneo de Puerto Princesa", 3100)
    graph.insert_edge("Jeju", "Parque Nacional de Komodo", 4700)

    graph.insert_edge("Río Subterráneo de Puerto Princesa", "Parque Nacional de Komodo", 1900)

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
def arbol_expansion_minima_por_tipo(graph):

    # Agrupar vértices por tipo
    arquitectonicas = []
    naturales = []

    for vertex in graph:
        if vertex.other_values.tipo == "arquitectonica":
            arquitectonicas.append(vertex.value)
        else:
            naturales.append(vertex.value)

    # ---- FUNCION AUXILIAR PARA IMPRIMIR MST ----
    def imprimir_mst(vertice_inicial, tipo):
        print(f"\nÁrbol de expansión mínima para maravillas {tipo}:")
        print(f"(Usando como raíz: {vertice_inicial})\n")

        expansion_tree = graph.kruskal(vertice_inicial)

        peso_total = 0

        for edge in expansion_tree.split(";"):
            partes = edge.split("-")
            # Validamos que la arista tenga formato correcto
            if len(partes) != 3:
                continue

            origin, destination, weight = partes
            print(f"{origin} -- {destination}  (peso: {weight})")
            peso_total += int(weight)

        print(f"Peso total del árbol ({tipo}): {peso_total}\n")

    # ---- Ejecutar para cada tipo ----

    # Arquitectónicas
    if arquitectonicas:
        imprimir_mst(arquitectonicas[0], "ARQUITECTÓNICAS")

    # Naturales
    if naturales:
        imprimir_mst(naturales[0], "NATURALES")

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
def paises_con_ambos_tipos(graph):

    paises = {}   # Ej: {"Perú": ["arquitectonica","natural"]}

    # Recorremos todos los vértices del grafo
    for vertex in graph:

        maravilla = vertex.other_values      # Objeto Maravilla
        tipo = maravilla.tipo                # arquitectonica o natural
        pais_info = maravilla.paises         # puede ser string o lista

        # Si el país es string lo convertimos en lista
        if isinstance(pais_info, str):
            lista_paises = [pais_info]
        else:
            lista_paises = pais_info

        # Para cada país de la maravilla
        for pais in lista_paises:

            if pais not in paises:
                paises[pais] = set()

            paises[pais].add(tipo)

    # Ahora buscamos países con AMBOS tipos
    paises_final = []

    for pais, tipos in paises.items():
        if "arquitectonica" in tipos and "natural" in tipos:
            paises_final.append(pais)

    # Mostrar resultado
    if paises_final:
        print("Países que tienen maravillas ARQUITECTÓNICAS y NATURALES:")
        for p in paises_final:
            print(" -", p)
    else:
        print("Ningún país tiene maravillas de ambos tipos.")

    return paises_final

# e. determinar si algún país tiene más de una maravilla del mismo tipo;
def paises_con_multiples_maravillas_mismo_tipo(graph):
    # Diccionario: {pais: {"arquitectonica": [], "natural": []}}
    paises = {}

    for vertex in graph:
        maravilla = vertex.other_values
        tipo = maravilla.tipo
        pais_info = maravilla.paises

        # Convertimos a lista si es string
        if isinstance(pais_info, str):
            lista_paises = [pais_info]
        else:
            lista_paises = pais_info

        # Registramos cada maravilla por país y tipo
        for pais in lista_paises:
            if pais not in paises:
                paises[pais] = {"arquitectonica": [], "natural": []}
            paises[pais][tipo].append(maravilla.nombre)

    # Buscamos países con más de una maravilla del mismo tipo
    resultado = {}
    for pais, tipos in paises.items():
        for tipo, lista in tipos.items():
            if len(lista) > 1:
                if pais not in resultado:
                    resultado[pais] = {}
                resultado[pais][tipo] = lista

    # Mostramos resultados
    if resultado:
        print("Países con más de una maravilla del mismo tipo:")
        for pais, tipos in resultado.items():
            for tipo, lista in tipos.items():
                print(f" - {pais} tiene {len(lista)} maravillas {tipo}: {', '.join(lista)}")
    else:
        print("No hay países con más de una maravilla del mismo tipo.")

    return resultado


#MAIN:
cargar_maravillas(grafo)
cargar_conexiones(grafo)
grafo.show()
print()
arbol_expansion_minima_por_tipo(grafo)
print()
paises_con_ambos_tipos(grafo)
print()
paises_con_multiples_maravillas_mismo_tipo(grafo)