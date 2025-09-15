from personajesData import Personaje, personajesMCU
from binarytree import BinaryTree

arbol = BinaryTree()

for character in personajesMCU:
    hero = Personaje(
        name = character[0],
        isVillano = character[1]
    )
    arbol.insert(hero.name, hero)

# b. listar los villanos ordenados alfabéticamente;
def orderVillanos(tree_):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            personaje = node.other_values
            if personaje.isVillano:
                print(node.value)
            inOrder(node.right)
    inOrder(tree_.root)


# c. mostrar todos los superhéroes que empiezan con C;
def namesC(tree_):
    def inOrder(node):
        if node is not None: # caso base: si el nodo es None, termina la rama
            inOrder(node.left) # llamada recursiva del nodo izquierdo
            personaje = node.other_values # para guardar el objeto del nodo
            if node.value.startswith("C") and not personaje.isVillano:
                print(node.value)
            inOrder(node.right) # llamada recursiva del nodo derecho
    inOrder(tree_.root) # recorrido de la raiz

# d. determinar cuántos superhéroes hay el árbol;
def nodeCounter(tree_):
    def inOrder(node):
        if node is None:
            return 0

        return 1  + inOrder(node.left) + inOrder(node.right)
    
    return inOrder(tree_.root)

# f. listar los superhéroes ordenados de manera descendente;
def orderDescendente(tree_):
    def order(node):
        if node is not None:
            order(node.right)
            personaje = node.other_values
            if not personaje.isVillano:
                print(node.value)
            order(node.left)
    order(tree_.root)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:

def generarBosque(tree_):
    treeHero_local = BinaryTree()
    treeVillan_local = BinaryTree()

    def recorrerArbol(node):
        if node is not None:
            recorrerArbol(node.left)
            personaje = node.other_values
            if personaje.isVillano:
                treeVillan_local.insert(node.value, personaje)
            else:
                treeHero_local.insert(node.value, personaje)
            recorrerArbol(node.right)

    recorrerArbol(tree_.root)

    return treeHero_local, treeVillan_local

# GENERAR BOSQUE
treeHero, treeVillan = generarBosque(arbol)

# I. determinar cuántos nodos tiene cada árbol;
def nodeCounterBosque(tree_):
    def inOrder(node):
        if node is None:
            return 0
        return 1 + inOrder(node.left) + inOrder(node.right)
    
    return inOrder(tree_.root)


print("Villanos ordenados alfabéticamente:")
orderVillanos(arbol)
print()
print("Superhéroes que empiezan con C: ")
namesC(arbol)
print()
print("Cantidad de personajes en el árbol: ", nodeCounter(arbol))
print()
print("Superhéroes listados de forma descendente:")
orderDescendente(arbol)
print()
print("Cantidad de superhéroes en el bosque: ", nodeCounterBosque(treeHero))
print("Cantidad de villanos en el bosque: ", nodeCounterBosque(treeVillan))
print()
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Superhéroes (DEL BOSQUE) ordenados alfabéticamente:")
treeHero.in_order()
print()
print("Villanos (DEL BOSQUE) ordenados alfabéticamente:")
treeVillan.in_order()