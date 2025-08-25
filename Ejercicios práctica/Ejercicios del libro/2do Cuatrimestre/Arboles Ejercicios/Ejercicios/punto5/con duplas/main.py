from binarytree import BinaryTree
from lista_personajes import personajes

arbol_personajes= BinaryTree()


#A
def cargar_personajes(arbol, personajes):
    for pj in personajes:
        arbol.insert(pj.nombre, pj.es_villano)

#B) listar los villanos ordenados alfabéticamente 
def mostrar_villanos_orden(arbol):
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.other_values == True:
                print(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)


#C) mostrar todos los superhéroes que empiezan con C
def mostrar_superheroes_C(arbol):
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            # si NO es villano y empieza con "C"
            if not nodo.other_values and nodo.value.startswith("C"):
                print(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)

#D) determinar cuántos superhéroes hay el árbol
def cantidad_SH(arbol):
    def inOrder(nodo):
        if nodo is not None:
            return (not nodo.other_values) + inOrder(nodo.left) + inOrder(nodo.right) #(not node.other_values es para aquellos que NO son villanos)
        else:
            return 0  #si el nodo es None retornar cero

    if arbol.root is not None:
        return inOrder(arbol.root)
    else:
        return 0
        


#E) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre
def modificar_doctor_strange(arbol):
    pos = arbol.search("Doctor Strange")
    if pos is not None:
        pos.value = "Doctor Stephen Strange"
        print("Nombre de Doctor Strange modificado a Doctor Stephen Strange.")
    else:
        print("Doctor Strange no se encontró en el árbol.")
    
    
# F) listar los superhéroes ordenados de manera descendente
def mostrar_SH_descendente(arbol):
    def postOrder(nodo):
        if nodo is not None:
            postOrder(nodo.right)  # Recorre la rama derecha
            # Solo si el nodo no es un villano, se imprime su nombre
            if not nodo.other_values:
                print(nodo.value)
            postOrder(nodo.left)   # Recorre la rama izquierda

    if arbol.root is not None:
        postOrder(arbol.root)
        
# G. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
def generarBosque(arbol):
    treeHero_local = BinaryTree()
    treeVillan_local = BinaryTree()

    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            
            if node.other_values: # condicional si es villano (true)
                treeVillan_local.insert(node.value, node.other_values)
            else:
                treeHero_local.insert(node.value, node.other_values)
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return treeHero_local, treeVillan_local


# I. determinar cuántos nodos tiene cada árbol;
def contarNodosArbol(arbol):
    def inOrder(node):
        if node is None:
            return 0
        return 1 + inOrder(node.left) + inOrder(node.right)
    
    return inOrder(arbol.root)
        

#MAIN
cargar_personajes(arbol_personajes, personajes)
print("Lista villanos ordenados alfabéticamente: ")
mostrar_villanos_orden(arbol_personajes)
print()
print("Todos los superhéroes que empiezan con C: ")
mostrar_superheroes_C(arbol_personajes)
print()
print(f"La cantidad de superhéroes que hay en el árbol es de: {cantidad_SH(arbol_personajes)}")
print()
modificar_doctor_strange(arbol_personajes)
print()
print("Lista superheroes ordenados de manera descendente: ")
mostrar_SH_descendente(arbol_personajes)
print()
# GENERAR BOSQUE
treeHero, treeVillan = generarBosque(arbol_personajes)
print()
print("Cantidad de superhéroes en el bosque: ", contarNodosArbol(treeHero))
print("Cantidad de villanos en el bosque: ", contarNodosArbol(treeVillan))
print()
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Superhéroes (DEL BOSQUE) ordenados alfabéticamente:")
treeHero.in_order()
print()
print("Villanos (DEL BOSQUE) ordenados alfabéticamente:")
treeVillan.in_order()