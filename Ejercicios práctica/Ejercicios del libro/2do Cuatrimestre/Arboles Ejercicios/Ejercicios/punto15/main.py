# 15. Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas
# a un archivo que contiene personajes de la saga de Star Wars, de los cuales se sabe su nombre,
# altura y peso. Además deberá contemplar los siguientes requerimientos:

from binarytree import BinaryTree
from personaje import Personaje
from lista_personajes import personajes

arbol_personajes= BinaryTree()

#a. en el árbol se almacenara solo el nombre del personaje, además de todo lo otro
def cargar_personajes(arbol, personajes):
    for pj in personajes:
        arbol.insert(pj.nombre, pj)
        
# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo
# de baja;
def cargar_nuevo_personaje(arbol):
    print("--- CARGAR NUEVO PERSONAJE ---")
    nombre = input("Nombre del personaje: ")
    altura = float(input("Altura (en cm): "))
    peso = float(input("Peso (en kg): "))
    
    nuevo_personaje = Personaje(nombre, altura, peso)
    arbol.insert(nombre, nuevo_personaje)
    print(f"Personaje '{nombre}' cargado exitosamente!")

# b.2. Modificar personaje existente
def modificar_personaje(arbol):
    print("--- MODIFICAR PERSONAJE ---")
    nombre = input("Nombre del personaje a modificar: ")
    
    nodo = arbol.search(nombre)
    if nodo is None:
        print(f"Personaje '{nombre}' no encontrado.")
        return
    
    personaje = nodo.other_values
    print(f"Datos actuales: {personaje}")
    
    print("¿Qué campo desea modificar?")
    print("1. Nombre")
    print("2. Altura")
    print("3. Peso")
    print("4. Todos los campos")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        nuevo_nombre = input("Nuevo nombre: ")
        # Para cambiar el nombre, necesitamos eliminar y reinsertar
        arbol.delete(nombre)
        personaje.nombre = nuevo_nombre
        arbol.insert(nuevo_nombre, personaje)
        print("Nombre modificado exitosamente!")
        
    elif opcion == "2":
        nueva_altura = float(input("Nueva altura (en cm): "))
        personaje.altura = nueva_altura
        print("Altura modificada exitosamente!")
        
    elif opcion == "3":
        nuevo_peso = float(input("Nuevo peso (en kg): "))
        personaje.peso = nuevo_peso
        print("Peso modificado exitosamente!")
        
    elif opcion == "4":
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_altura = float(input("Nueva altura (en cm): "))
        nuevo_peso = float(input("Nuevo peso (en kg): "))
        
        # Eliminar el viejo e insertar el nuevo
        arbol.delete(nombre)
        personaje.nombre = nuevo_nombre
        personaje.altura = nueva_altura
        personaje.peso = nuevo_peso
        arbol.insert(nuevo_nombre, personaje)
        print("Todos los campos modificados exitosamente!")

# b.3. Dar de baja personaje
def dar_de_baja_personaje(arbol):
    print("--- DAR DE BAJA PERSONAJE ---")
    nombre = input("Nombre del personaje a eliminar: ")
    
    valor, datos = arbol.delete(nombre)
    if valor is not None:
        print(f"Personaje '{valor}' eliminado exitosamente!")
        print(f"Datos eliminados: {datos}")
    else:
        print(f"Personaje '{nombre}' no encontrado.")

# c. mostrar toda la información de Yoda y Boba Fett;
def mostrar_yoda_boba_fett(arbol):
    print("--- INFORMACIÓN DE YODA Y BOBA FETT ---")
    
    yoda = arbol.search("Yoda")
    boba_fett = arbol.search("Boba Fett")
    
    if yoda is not None:
        print(f"Yoda: {yoda.other_values}")
    else:
        print("Yoda no encontrado en el árbol.")
    
    if boba_fett is not None:
        print(f"Boba Fett: {boba_fett.other_values}")
    else:
        print("Boba Fett no encontrado en el árbol.")
        
# d. mostrar un listado ordenado alfabéticamente de los personajes que miden más de 1 metro;   
def listar_altos(arbol):
    print("--- PERSONAJES QUE MIDEN MÁS DE 1 METRO ---")
    
    def in_order(root):
        if root is not None:
            in_order(root.left)
            if root.other_values.altura > 100:
                print(f"{root.value}: {root.other_values.altura}cm")
            in_order(root.right)
    
    if arbol.root is not None:
        in_order(arbol.root)

# e. mostrar un listado ordenado alfabéticamente de los personajes que pesan menos de 75 ki-
# los;
def listar_livianos(arbol):
    print("--- PERSONAJES QUE PESAN MENOS DE 75 KG ---")
    
    def in_order(root):
        if root is not None:
            in_order(root.left)
            if root.other_values.peso < 75:
                print(f"{root.value}: {root.other_values.peso}kg")
            in_order(root.right)
            
    if arbol.root is not None:
        in_order(arbol.root)  
        
#MAIN:
def mostrar_menu():
    print("\n" + "="*50) #sirve para crear separadores visuales
    print("SISTEMA DE GESTIÓN DE PERSONAJES STAR WARS")
    print("="*50)
    print("a. Mostrar árbol completo (in-order)")
    print("b. Cargar nuevo personaje")
    print("c. Modificar personaje existente")
    print("d. Dar de baja personaje")
    print("e. Mostrar información de Yoda y Boba Fett")
    print("f. Listar personajes que miden más de 1 metro")
    print("g. Listar personajes que pesan menos de 75 kg")
    print("h. Salir")
    print("="*50)

# MAIN
def main():
    # Cargar personajes iniciales
    cargar_personajes(arbol_personajes, personajes)
    print("Personajes cargados exitosamente!")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == "a":
            print("\n--- ÁRBOL COMPLETO (IN-ORDER) ---")
            arbol_personajes.in_order()
            
        elif opcion == "b":
            cargar_nuevo_personaje(arbol_personajes)
            
        elif opcion == "c":
            modificar_personaje(arbol_personajes)
            
        elif opcion == "d":
            dar_de_baja_personaje(arbol_personajes)
            
        elif opcion == "e":
            mostrar_yoda_boba_fett(arbol_personajes)
            
        elif opcion == "f":
            listar_altos(arbol_personajes)
            
        elif opcion == "g":
            listar_livianos(arbol_personajes)
            
        elif opcion == "h":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()
