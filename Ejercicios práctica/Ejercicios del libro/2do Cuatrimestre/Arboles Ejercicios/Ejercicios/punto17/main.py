# 17. Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada
# (890 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/
# tipos, para el cual debemos construir tres árboles para acceder de manera eficiente a los datos
# almacenados en el archivo, contemplando lo siguiente:


from binarytree import BinaryTree
from lista_pokemons import pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

def cargar_pokemons(arbol_nom, arbol_num,arbol_tip, pokemons):
    for pokemon in pokemons:
        arbol_nom.insert(pokemon.nombre, pokemon)
        # por número
        arbol_num.insert(pokemon.numero, pokemon)
        # por tipo (si tiene 2 tipos lo insertamos en ambos)
        for tipo in pokemon.tipos:
            arbol_tip.insert(tipo, pokemon)
            
            
# b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último,
# la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los
# Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
def buscar_pokemon_numero(numero):
    nodo = arbol_numero.search(numero)
    if nodo:
        print("Se encontro el pokemon numero 25!, aqui sus datos: ")
        print(nodo.other_values)
    else:
        print("No se encontro ese numero de pokemon.")
        
def buscar_pokemon_nombre(arbol, nombre_parcial):
    print(f"Pokémons que contienen '{nombre_parcial}':")
    arbol.proximity_search(nombre_parcial)


# c. mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego,
# planta y eléctrico;
def mostrar_por_tipo(arbol,tipo):
    def __buscar(root):
        if root is not None:
            __buscar(root.left)
            if root.value == tipo:
                print(root.other_values.nombre)
            __buscar(root.right)
            
    if arbol.root is not None:
        __buscar(arbol_tipo.root)

# e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;                 
def pokemones_debiles(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            
            for debilidad in node.other_values.debilidades:
                if debilidad in ["Jolteon", "Lycanroc", "Tyrantrum"]:
                    print(f"- {node.other_values}")
                    break #necesito si o si usar el break porque sino no lo corta
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

# f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
def contar_tipos_pokemon(arbol):
    conteo_tipos = {}
    
    # Recorremos el árbol para llenar el diccionario con los conteos
    def in_orden(node):
        if node is not None:
            in_orden(node.left)
            
            tipo = node.value
            if tipo in conteo_tipos:
                conteo_tipos[tipo] += 1
            else:
                conteo_tipos[tipo] = 1
                
            in_orden(node.right)
            
    if arbol.root is not None:
        in_orden(arbol.root)

    # Ahora mostramos los resultados del diccionario
    print("Conteo de Pokémons por tipo:")
    
    for tipo in conteo_tipos:
        cantidad = conteo_tipos[tipo]
        print(f"- Tipo {tipo}: {cantidad}")

#MAIN
# a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
cargar_pokemons(arbol_nombre, arbol_numero, arbol_tipo, pokemons)
# d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un
# listado por nivel por nombre;
print("Arbol en orden de nombre: ")
arbol_nombre.in_order()
print()
print("Arbol en orden de numero: ")
arbol_numero.in_order()
print()
print("Arbol por nivel de Nombre: ")
arbol_tipo.by_level()
print()
buscar_pokemon_numero(25) #le pongo un numero yo nomas
print()
buscar_pokemon_nombre(arbol_nombre,"Bul") #le pongo un nombre yo nomas
print()
print("Pokemones de tipo agua: ")
mostrar_por_tipo(arbol_tipo, "Agua") #lo elijo yo nomas
print("Pokemones de tipo fuego: ")
mostrar_por_tipo(arbol_tipo, "Fuego") #lo elijo yo nomas
print("Pokemones de tipo planta: ")
mostrar_por_tipo(arbol_tipo, "Planta") #lo elijo yo nomas
print("Pokemones de tipo electrico: ")
mostrar_por_tipo(arbol_tipo, "Eléctrico") #lo elijo yo nomas
print()
print("Todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum: ")
pokemones_debiles(arbol_nombre)
print()
contar_tipos_pokemon(arbol_tipo)


