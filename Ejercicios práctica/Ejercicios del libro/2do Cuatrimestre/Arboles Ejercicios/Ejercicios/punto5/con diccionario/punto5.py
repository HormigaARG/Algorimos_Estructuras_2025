from binarytree import BinaryTree
from super_heroes_data import superheroes

arbol_personajes= BinaryTree()


#A
def cargar_personajes(arbol, superheroes):
    for pj in superheroes:
        arbol.insert(pj['name'], pj["is_villain"])

#B) listar los villanos ordenados alfabéticamente 
def mostrar_villanos_orden(arbol):
    def __villanos_in_order(nodo):
        if nodo is not None:
            __villanos_in_order(nodo.left)
            if nodo.other_values is True: 
                print(nodo.value)
            __villanos_in_order(nodo.right)

    if arbol.root is not None:
        __villanos_in_order(arbol.root)


#C) mostrar todos los superhéroes que empiezan con C
def mostrar_superheroes_C(arbol):
    def __in_order(nodo):
        if nodo is not None:
            __in_order(nodo.left)
            # si NO es villano y empieza con "C"
            if not nodo.other_values and nodo.value.startswith("C"):
                print(nodo.value)
            __in_order(nodo.right)

    if arbol.root is not None:
        __in_order(arbol.root)

#D) determinar cuántos superhéroes hay el árbol
def cantidad_SH(arbol):
    c_superheroes=0
    def __cantidad_SH(nodo):
        nonlocal c_superheroes #solamente teniendo esto me deja que tenga un contador (lo busque)
        if nodo is not None:
            __cantidad_SH(nodo.left)
            # si NO es villano, al contador se le suma 1
            if not nodo.other_values:
                c_superheroes+=1
            __cantidad_SH(nodo.right)

    if arbol.root is not None:
        __cantidad_SH(arbol.root)
        
    return c_superheroes

#E) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre
def modificar_doctor_strange(arbol):
    pos = arbol.search("Dr Strange")
    if pos is not None:
        pos.value = "Doctor Stephen Strange"
        print("Nombre de Doctor Strange modificado a Doctor Stephen Strange.")
    else:
        print("Doctor Strange no se encontró en el árbol.")
    
    
# F) listar los superhéroes ordenados de manera descendente
def mostrar_SH_descendente(arbol):
    def __desc_order(nodo):
        if nodo is not None:
            __desc_order(nodo.right)  # Recorre la rama derecha
            # Solo si el nodo no es un villano, se imprime su nombre
            if not nodo.other_values:
                print(nodo.value)
            __desc_order(nodo.left)   # Recorre la rama izquierda

    if arbol.root is not None:
        __desc_order(arbol.root)
        

#MAIN
cargar_personajes(arbol_personajes, superheroes)
print("Lista villanos ordenados alfabéticamente: ")
mostrar_villanos_orden(arbol_personajes)
print()
print("Todos los superhéroes que empiezan con C: ")
mostrar_superheroes_C(arbol_personajes)
print()
c_superheroes=cantidad_SH(arbol_personajes)
print(f"La cantidad de superhéroes que hay en el árbol es de: {c_superheroes}")
print()
modificar_doctor_strange(arbol_personajes)
print()
print("LIsta superheroes ordenados de manera descendente: ")
mostrar_SH_descendente(arbol_personajes)