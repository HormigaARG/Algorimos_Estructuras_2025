# 19. Desarrollar los algoritmos necesarios que permitan almacenar libros, de los cuales se conoce

# su título, ISBN, autores, editorial y cantidad páginas en un archivo, contemplando los siguien-
# tes requerimientos y tareas:

# a. utilizar el TDA archivo desarrollado en el capítulo V;
# b. deberá cargar al menos 100 libros;
# c. implementar tres árboles para manejar los índices de acceso, estos serán por título, ISBN y
# autores. En cada nodo del árbol se almacenará el campo clave correspondiente y la posi-
# ción en el archivo donde está el resto de la información;


from binarytree import BinaryTree
from lista_libros import libros


arbol_titulo = BinaryTree()
arbol_ISBN = BinaryTree()
arbol_autores = BinaryTree()

def cargar_libros(arbol_titu, arbol_isbn, arbol_auto, libros):
    for libro in libros:
        arbol_titu.insert(libro.titulo, libro)
        arbol_isbn.insert(libro.isbn, libro)
        #Autores como clave (si hay varios, cada uno se inserta)
        for autor in libro.autores.split(","):
            arbol_auto.insert(autor.strip(), libro)
        

    
    
# d. las búsquedas deberán ser de la siguiente manera:

# I. por exactitud en el árbol de ISBN,  
def busqueda_exatitud(arbol, isbn):
    nodo = arbol.search(isbn)
    if nodo:
        print(f"Se encontro el libro con ISBN {isbn}, aqui sus datos: ")
        print(nodo.other_values)
    else:
        print("No se encontro ese ISBN en los libros.")
 

# II. que esté contenido en el árbol de autores –es decir si son más de un autor y busco
# por uno debería encontrarlo–,
def busqueda_autor(arbol, autor):
    nodo = arbol.search(autor)
    if nodo:
        print(f"Se encontro el libro con autor {autor}, aqui sus datos: ")
        print(nodo.other_values)
    else:
        print("No se encontro ese autor en los libros.")


# III. por proximidad en el inicio del nombre en el árbol de título –si busco “Alg” debe-
# ría encontrar todos los libros cuyo nombres comienzan así–.
def busqueda_proximidad(arbol, nombre):
    print(f"Libros cuyo titulo comienza con {nombre}:")
    arbol.proximity_search(nombre)

        
#MAIN:
cargar_libros(arbol_titulo, arbol_ISBN, arbol_autores, libros)
print()
busqueda_exatitud(arbol_ISBN, "978-0307474728") #le pongo uno yo
print()
busqueda_autor(arbol_autores,"Rachael Lippincott") #le pongo yo nomas
print()
busqueda_proximidad(arbol_titulo,"Alg") #le pongo yo


