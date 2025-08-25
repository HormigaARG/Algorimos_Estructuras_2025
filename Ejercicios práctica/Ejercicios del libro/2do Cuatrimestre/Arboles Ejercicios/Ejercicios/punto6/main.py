from binarytree import BinaryTree
from lista_personajes import personajes

arbol_personajes= BinaryTree()



#A
def cargar_personajes(arbol, personajes):
    for pj in personajes:
        arbol.insert(pj.nombre, pj)
        
def generarBosque(arbol_general):
    arbol_nom = BinaryTree()
    arbol_ran = BinaryTree()
    arbol_esp = BinaryTree()

    def inOrder(node):
        if node is not None:
            inOrder(node.left)

            pj = node.other_values  # el objeto Personaje completo

            # por nombre
            arbol_nom.insert(pj.nombre, pj)
            
            # por ranking (puede haber varios)
            for r in pj.ranking:
                arbol_ran.insert(r, pj)

            #por especie
            arbol_esp.insert(pj.especie, pj)

            inOrder(node.right)

    if arbol_general.root is not None:
        inOrder(arbol_general.root)

    return arbol_nom, arbol_ran, arbol_esp


#MAIN
cargar_personajes(arbol_personajes, personajes)
arbol_nombre, arbol_ranking, arbol_especie = generarBosque(arbol_personajes)
# b. realizar un barrido inorden del árbol por nombre y ranking;
print()
print("Barrido (IN-ORDEN) del arbol por nombre: ")
arbol_nombre.in_order()
print("Barrido (IN-ORDEN) del arbol por ranking: ")
arbol_ranking.in_order()
print()

