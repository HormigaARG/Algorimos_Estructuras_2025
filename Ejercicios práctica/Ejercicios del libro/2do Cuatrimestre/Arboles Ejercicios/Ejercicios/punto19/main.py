# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;

from binarytree import BinaryTree
from lista_criaturas import criaturas

arbol_criaturas = BinaryTree()

def cargar_criaturas(arbol, criaturas):
    for criatu in criaturas:
        arbol.insert(criatu.nombre, criatu)

# b. se debe permitir cargar una breve descripción sobre cada criatura;
def cargar_descripcion(arbol, nombre, descripcion):
    nodo = arbol.search(nombre)
    if nodo is not None:
        nodo.other_values.descripcion = descripcion
        print(f"Descripción de {nombre} actualizada.")
    else:
        print(f"No se encontró la criatura {nombre}.")        


#c. mostrar toda la información de la criatura Talos;
def mostrar_info(arbol):
    nodo = arbol.search("Talos")
    if nodo is not None:
        personaje = nodo.other_values
        print(f"- {personaje}")
    else:
        print("Talos no se encontró en el árbol.") 

# e. listar las criaturas derrotadas por Heracles;
def mostrar_criaturas(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.other_values.derrotado_por == "Heracles":
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)


# f. listar las criaturas que no han sido derrotadas;
def mostrar_criaturas_no_derrotadas(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.other_values.derrotado_por == None:
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)


# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
def mostrar_nodos(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value == "Cerbero" or node.value == "Toro de Creta" or  node.value == "Cierva Cerinea" or node.value == "Jabalí de Erimanto":
                node.other_values.capturada="Heracles"
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)

# i. se debe permitir búsquedas por coincidencia;
def busqueda_por_coincidencia(arbol, cadena):
    print(f"Búsqueda por coincidencia para '{cadena}':")
    arbol.proximity_search(cadena)
     
# j. eliminar al Basilisco y a las Sirenas;
def eliminar_criaturas(arbol, criatura):
    valor_eliminado, otros_valores = arbol.delete(criatura) #La funcion delete del árbol ya se encarga de buscar y eliminar el nodo.
    
    if valor_eliminado is not None:
        print(f"La criatura {criatura} se ha eliminado exitosamente.")
    else:
        print(f"No se encontró a la criatura {criatura}.")
        
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
def modificar_nodo(arbol):
    nodo = arbol.search("Aves del Estínfalo")
    
    if nodo is not None:
        # Si no tiene derrotado_por, asigno a Heracles
        if nodo.other_values.derrotado_por is None:
            nodo.other_values.derrotado_por = "Heracles"
        
        # Agrego la información a la descripción
        nodo.other_values.descripcion += " Heracles derrotó a varias de estas aves." #Agrego esta parte a la descripcion
        
        print("Aves del Estínfalo actualizadas correctamente.")
    else:
        print("No se encontraron las Aves del Estínfalo.")
        
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
def modificar_criatura(arbol):
    # Buscar y eliminar la criatura original
    valor_eliminado, datos_eliminados = arbol.delete("Ladón") #La funcion delete del árbol ya se encarga de buscar y eliminar el nodo.
    
    if valor_eliminado is not None:
        # Modificar el nombre en los datos de la criatura
        datos_eliminados.nombre = "Dragón Ladón"
        
        # Insertar la criatura con el nuevo nombre
        arbol.insert("Dragón Ladón", datos_eliminados)
        print("Nombre de la criatura Ladón modificado exitosamente.")
    else:
        print("No se encontró la criatura Ladón.")
    
    print("Verificando como quedó (después de modificar):")
    nodo_verificado = arbol.search("Dragón Ladón")
    if nodo_verificado is not None:
        print(f"Encontrado: {nodo_verificado.value}")
    else:
        print("No se encontró la criatura con el nuevo nombre.")
        
        
# n. muestre las criaturas capturadas por Heracles.
def mostrar_criaturas_capturadas(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.other_values.capturada == "Heracles":
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)
        
    
#MAIN
cargar_criaturas(arbol_criaturas, criaturas)
# a. listado inorden de las criaturas y quienes la derrotaron;
print("Listado de todas las criaturas en In-Orden y quienes la derrotaron, (toda la info):")
arbol_criaturas.in_order()
print()
cargar_descripcion(arbol_criaturas, "Esfinge", "Criatura con cuerpo de Leon") #elijo manualmente una criatura
print()
print("Toda la informacion de la criatura Talos: ")
mostrar_info(arbol_criaturas)
print()
print("Criaturas derrotadas por Heracles: ")
mostrar_criaturas(arbol_criaturas)
print()
print("Criaturas que no han sido derrotadas: ")
mostrar_criaturas_no_derrotadas(arbol_criaturas)
print()
print("Criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto cambiando a atrapados por Heracles: ")
mostrar_nodos(arbol_criaturas)
print()
eliminar_criaturas(arbol_criaturas,"Basilisco")
eliminar_criaturas(arbol_criaturas, "Sirenas")
print()
modificar_nodo(arbol_criaturas)
print()
modificar_criatura(arbol_criaturas)
print()
# m. realizar un listado por nivel del árbol;
print("Listado por nivel del árbol: ")
arbol_criaturas.by_level()
print()
print("Criaturas capturadas por Heracles: ")
mostrar_criaturas_capturadas(arbol_criaturas)




