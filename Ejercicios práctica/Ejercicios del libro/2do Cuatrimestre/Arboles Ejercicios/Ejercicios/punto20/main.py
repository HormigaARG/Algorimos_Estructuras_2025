# 20. Ahora resuelva las siguientes consultas mostrando toda la información de los libros correspondiente:


from binarytree import BinaryTree
from lista_libros import libros


arbol_titulo = BinaryTree()
arbol_ISBN = BinaryTree()
arbol_autores = BinaryTree()
arbol_categoria = BinaryTree()
arbol_pagina = BinaryTree()

def cargar_libros(arbol_titu, arbol_isbn, arbol_auto, arbol_cate, arbol_pag, libros):
    for libro in libros:
        arbol_titu.insert(libro.titulo, libro)
        arbol_isbn.insert(libro.isbn, libro)
        arbol_cate.insert(libro.categoria, libro)
        arbol_auto.insert(libro.autor, libro)
        arbol_pag.insert(libro.paginas, libro)

# a. los libros de los autores Tanenbaum, Connolly, Rowling, Riordan, Morgan Kass;          
def libro_autores(arbol, autor):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value == autor:
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)
   
# b. mostrar los libros de “minería de datos”, “algoritmos” y “bases de datos”;    
def libro_categoria(arbol, categoria):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value == categoria:
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)
    
# c. mostrar los libros de más de 873 páginas;
def libro_paginas(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            if node.value > 873:
                print(f"- {node.other_values}")
            inOrder(node.right)
    
    if arbol.root is not None:
        inOrder(arbol.root)     
        
        
# d. mostrar los datos del libro ISBN 9789504967453;
def busqueda_libro(arbol):
    nodo = arbol.search("9789504967453")
    if nodo:
        print(f"Se encontro el libro con ISBN 9789504967453, aqui sus datos: ")
        print(nodo.other_values)
    else:
        print("No se encontro ese ISBN en los libros.")
   
# e. mostrar el autor del libro “los 100”.     
def mostrar_autor(arbol):
    nodo = arbol.search("Los 100")
    if nodo:
        print(f"Se encontro el libro Los 100, aqui su autor: {(nodo.other_values.autor)}")
    else:
        print("No se encontro ese titulo en los libros.")
  
#MAIN:
cargar_libros(arbol_titulo, arbol_ISBN, arbol_autores, arbol_categoria, arbol_pagina, libros)
print("Libro del autor Tanembaum:")
libro_autores(arbol_autores,"Tanenbaum")
print()
print("Libro del autor Connolly:")
libro_autores(arbol_autores,"Connolly")
print()
print("Libro del autor Rowling:")
libro_autores(arbol_autores,"Rowling")
print()
print("Libro del autor Riordan:")
libro_autores(arbol_autores,"Riordan")
print()
print("Libro del autor Morgan Kass:")
libro_autores(arbol_autores,"Morgan Kass")
print()
print()
print("Libros de la categoria Mineria de Datos:")
libro_categoria(arbol_categoria,"Minería de Datos")
print()
print("Libros de la categoria Algoritmos:")
libro_categoria(arbol_categoria,"Algoritmos")
print()
print("Libros de la categoria Bases de datos:")
libro_categoria(arbol_categoria,"Bases de Datos")
print()
print()
print("Libros de mas de 873 paginas: ")
libro_paginas(arbol_pagina)
print()
busqueda_libro(arbol_ISBN)
print()
mostrar_autor(arbol_titulo)

