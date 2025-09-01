# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

from binarytree import BinaryTree
import random 

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): 
    for i in range(10): #aca tuviera que ser 1000
        numero = random.randint(1, 8)  # rango arbitrario
        arbol.insert(numero)
        
        
# b. determinar si un número está cargado en el árbol o no;
def determinar_numero(arbol, numero):
    nodo = arbol.search(numero)
    if nodo:
        print(f"Se encontró el número {numero}.")
    else:
        print(f"No se encontró el número {numero}.")
        
# c. eliminar tres valores del árbol;
def eliminar_valores(arbol, numero1, numero2, numero3):
    numeros= [numero1, numero2, numero3]
    for num in numeros:
        eliminado, _ = arbol.delete(num) #con el _, ignoramos el other values
        if eliminado is not None:
            print(f"Se eliminó el número {eliminado}.")
        else:
            print(f"El número {num} no se encontró en el árbol.")
            
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
def altura(nodo):
    if nodo is None:
        return 0
    else:
        return 1 + max(altura(nodo.left), altura(nodo.right))
    
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
def determinar_ocurrencia(arbol, numero):
    def inOrden(nodo, numero_a_buscar):
        # Caso base: si el nodo es nulo, no hay ocurrencias
        if nodo is None:
            return 0
        
        conteo = 0
        
        # Si el valor del nodo actual coincide, suma 1 al conteo
        if nodo.value == numero_a_buscar:
            conteo += 1
            
        # Llama recursivamente a la función para los subárboles izquierdo y derecho
        conteo += inOrden(nodo.left, numero_a_buscar)
        conteo += inOrden(nodo.right, numero_a_buscar)
        
        return conteo

    # Llama a la función auxiliar con la raíz del árbol
    return inOrden(arbol.root, numero)

# f. contar cuántos números pares e impares hay en el árbol.
def contar_pares_impares(arbol):
    pares = 0
    impares = 0

    def inOrden(nodo):
        nonlocal pares, impares
        if nodo is not None:
            inOrden(nodo.left)
            if nodo.value % 2 == 0:
                pares += 1
            else:
                impares += 1  
            inOrden(nodo.right)

    if arbol.root is not None:
        inOrden(arbol.root)
    return pares, impares

        
#MAIN:
cargar_arbol(arbol_numeros)
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print("Barrido preorden: ")
arbol_numeros.pre_order()
print("Barrido inorden: ")
arbol_numeros.in_order()
print("Barrido postorden: ")
arbol_numeros.post_order()
print("Barrido por nivel: ")
arbol_numeros.by_level()
print()
determinar_numero(arbol_numeros, 3) #le pongo 3 nomas
print()
eliminar_valores(arbol_numeros, 3, 8, 9)
print()
subarbol_izquierdo = arbol_numeros.root.left
subarbol_derecho   = arbol_numeros.root.right
print(f"Altura del subárbol izquierdo: {altura(subarbol_izquierdo)}")
print(f"Altura del subárbol derecho: {altura(subarbol_derecho)}")
print()
cantidad_ocurrencias = determinar_ocurrencia(arbol_numeros, 8)
print(f"El número 8 aparece {cantidad_ocurrencias} vez/veces en el árbol.")
print()
pares, impares = contar_pares_impares(arbol_numeros)
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")



