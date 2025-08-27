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


#D. mostrar toda la información de Yoda y Luke Skywalker;
def mostrar_info(arbol, nombre):
    nodo = arbol.search(nombre)
    if nodo is not None:
        personaje = nodo.other_values
        print(f"- {personaje}")
    else:
        print(f"{nombre} no se encontró en el árbol.")
        
#E. mostrar todos los Jedi con ranking “Jedi Master”;   
def mostrar_todos_JediMaster(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value == "Jedi Master":
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)
        
#E) PREGUNTAR DUDA ACA (SI LO QUIERO HACER CON EL MENSAJE DE QUE NO ENCONTRO NINGUN JEDI CON ESE RANKING), PORQUE UTLIZA NONLOCAL??) 
# def mostrar_todos_JediMaster(arbol):
#     encontrado = False
#     def inOrder(node):
#         nonlocal encontrado
#         if node is not None:
#             inOrder(node.left)
#             if node.value == "Jedi Master":
#                 print(f"- {node.other_values}")
#                 encontrado = True
#             inOrder(node.right)
#     if arbol.root is not None:
#         inOrder(arbol.root)
#     if not encontrado:
#         print("Jedi no se encontró en el árbol o no se encontro con el ranking Jedi Master.")
        
#F. listar todos los Jedi que utilizaron sabe de luz color verde;
def mostrar_jedi_sable(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if "Verde" in node.other_values.color_sable:
                print(f"- {node.other_values}")
            inOrder(node.right)
    if arbol.root is not None:
        inOrder(arbol.root)
        
#G. listar todos los Jedi cuyos maestros están en el archivo;

#H. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
def mostrar_todos_Jedi_Especie(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value == "Togruta" or node.value == "Cerean":
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)
        
#I. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
def mostrar_Letra_Contiene(arbol):
    def inOrder(nodo):
        if nodo is not None:
            inOrder(nodo.left)
            if nodo.value.startswith("A") or "-" in nodo.value:
                print(nodo.value)
            inOrder(nodo.right)

    if arbol.root is not None:
        inOrder(arbol.root)


#MAIN
cargar_personajes(arbol_personajes, personajes)
arbol_nombre, arbol_ranking, arbol_especie = generarBosque(arbol_personajes)
#B. realizar un barrido inorden del árbol por nombre y ranking;
print()
print("Barrido (IN-ORDEN) del arbol por nombre: ")
arbol_nombre.in_order()
print("Barrido (IN-ORDEN) del arbol por ranking: ")
arbol_ranking.in_order()
print()
#C. realizar un barrido por nivel de los árboles por ranking y especie;
print("Barrido (BY-LEVEL) del arbol por ranking: ")
arbol_ranking.by_level()
print("Barrido (BY-LEVEL) del arbol por especie: ")
arbol_especie.by_level()
print()
print("Toda la información de Yoda y Luke Skywalker: ")
mostrar_info(arbol_personajes, "Yoda")
mostrar_info(arbol_personajes, "Luke Skywalker")
print()
print("Todos los Jedi con ranking (Jedi Master): ")
mostrar_todos_JediMaster(arbol_ranking)
print()
print("Todos los Jedi que utilizaron sabe de luz color verde: ")
mostrar_jedi_sable(arbol_personajes)
print()
print("Todos los Jedi de especie “Togruta” o “Cerean”: ")
mostrar_todos_Jedi_Especie(arbol_especie)
print()
print("Listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.")
mostrar_Letra_Contiene(arbol_personajes)

