from binarytree import BinaryTree
from lista_personajes import personajes

arbol_personajes= BinaryTree()
arbol_superheroes = BinaryTree()
arbol_villanos = BinaryTree()


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
# def cantidad_SH(arbol):
#     def inOrder(nodo):
#         if nodo is not None:
#             return (not nodo.other_values) + inOrder(nodo.left) + inOrder(nodo.right) #(not node.other_values es para aquellos que NO son villanos)
#         else:
#             return 0  #si el nodo es None retornar cero

#     if arbol.root is not None:
#         return inOrder(arbol.root)
#     else:
#         return 0

def cantidad_SH(self):
    def __contarNodosArbol(nodo):
        cantidad = 0
        if nodo is not None:
            if not nodo.other_values: #si NO es villano se acumula
                cantidad += 1
            cantidad += __contarNodosArbol(nodo.left)
            cantidad += __contarNodosArbol(nodo.right)

        return cantidad

    total = 0
    if self.root is not None:
        total = __contarNodosArbol(self.root)
    
    return total
        


#E) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre
def modificar_doctor_strange(arbol):
    arbol.proximity_search("Dr") #nos va a listar los nombres que comienzan con Dr.
    name= input("Ingrese el nombre mal cargado para eliminar: ") # de todos esos nombres elegimos el que vamos a eliminar.
    value, other_value = arbol.delete(name) 
    
    if value is not None:
        fix_name = input("Ingrese el nuevo nombre asi queda bien cargado: ")
        other_value = fix_name
        arbol.insert(fix_name, other_value)
        
    print("Verificamos como quedo (despues de acomodar a Dr Strange): ")
    arbol.proximity_search("Dr")
    

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
def generarBosque(arbol, arbol_SH, arbol_VI):

    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            
            if node.other_values: # condicional si es villano (true)
                arbol_VI.insert(node.value, node.other_values)
            else:
                arbol_SH.insert(node.value, node.other_values)
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    return arbol_SH, arbol_VI


# I. determinar cuántos nodos tiene cada árbol;
#OTRA MANERA:
# def contarNodosArbol(arbol):
#     def inOrder(node):
#         if node is None:
#             return 0
#         return 1 + inOrder(node.left) + inOrder(node.right)
    
#     return inOrder(arbol.root)

def contarNodosArbol(self):
    def __contarNodosArbol(nodo):
        cantidad = 0
        if nodo is not None:
            cantidad += 1
            cantidad += __contarNodosArbol(nodo.left)
            cantidad += __contarNodosArbol(nodo.right)

        return cantidad

    total = 0
    if self.root is not None:
        total = __contarNodosArbol(self.root)
    
    return total
        

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
print("Modificar Dr Strange: ")
modificar_doctor_strange(arbol_personajes)
print()
print("Lista superheroes ordenados de manera descendente: ")
mostrar_SH_descendente(arbol_personajes)
print()
# GENERAR BOSQUE
generarBosque(arbol_personajes, arbol_superheroes, arbol_villanos)
print()
print("Cantidad de superhéroes en el bosque: ", contarNodosArbol(arbol_superheroes))
print("Cantidad de villanos en el bosque: ", contarNodosArbol(arbol_villanos))
print()
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Superhéroes (DEL BOSQUE) ordenados alfabéticamente:")
arbol_superheroes.in_order()
print()
print("Villanos (DEL BOSQUE) ordenados alfabéticamente:")
arbol_villanos.in_order()