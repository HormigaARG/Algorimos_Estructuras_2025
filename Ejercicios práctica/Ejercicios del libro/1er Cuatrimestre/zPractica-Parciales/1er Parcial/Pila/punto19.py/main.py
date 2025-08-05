# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
# treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from stack import Stack
from Pelicula import Pelicula

peliculas_stack= Stack()


peliculas=[
    Pelicula("Spiderman X", "Marvel Studios", 2014),
    Pelicula("Avengers: Infinity War", "Marvel Studios", 2018),
    Pelicula("Doctor Strange", "Marvel Studios", 2016),
    Pelicula("Locuras", "Marvel Studios", 2016),
    Pelicula("Interstellar", "Paramount Pictures", 2014),
]

def cargarPila(peli_stack,peliculas):
    for peli in peliculas:
        peli_stack.push(peli)
        
        
#A    
def mostrarPeliculas2014(peli_stack):
    aux_stack=Stack()
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        
        if peli.año==2014:
            print(f"{peli.titulo}")
    
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())
        
#B
def cantidadPeliculas2018(peli_stack):
    aux_stack=Stack()
    c_contador=0
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        
        if peli.año==2018:
            c_contador+=1
    
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())   
        
    return c_contador   

#C. mostrar las películas de Marvel Studios estrenadas en el año 2016.
def mostrarPeliculasMarvel2016(peli_stack):
    aux_stack=Stack()
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        
        if peli.estudio=="Marvel Studios" and peli.año==2016:
            print(f"{peli}")
    
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())





#CP
cargarPila(peliculas_stack,peliculas)
print("Peliculas estrenadas en el año 2014: ")
mostrarPeliculas2014(peliculas_stack)
print()
contadorPelis2018=cantidadPeliculas2018(peliculas_stack)
print(f"La cantidad de películas que se estrenaron en el año 2018 es: {contadorPelis2018}")
print()
print("Películas de Marvel Studios estrenadas en el año 2016: ")
mostrarPeliculasMarvel2016(peliculas_stack)
