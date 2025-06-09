# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.

from list_ import List
from queue import Queue
from lista_personajes import personajes
from personaje import order_by_nombre, order_by_nombre_real, order_by_año_aparicion

list_personajes = List()
villanosAparicion_queue= Queue()

def cargar_personajes(list_pj, personajes):
    for pj in personajes:
        list_pj.append(pj)

def ordenarCriterios(list_pj):
    list_pj.add_criterion("nombre", order_by_nombre)
    list_pj.add_criterion("nombre_real", order_by_nombre_real)
    list_pj.add_criterion("año_aparicion",order_by_año_aparicion)
    
# Determinar en que posicion esta The Thing y Rocket Raccoon.
def mostrarPosicion(list_pj):
    indice1=list_pj.search("The Thing", "nombre")
    indice2=list_pj.search("Rocket Raccoon", "nombre")
    
    if indice1:
        print(f"{list_pj[indice1].nombre}, se encuentra en la posicion: {indice1}")
    else:
        print("No se encontro al personaje The Thing.")
        
    if indice2:
        print(f"{list_pj[indice2].nombre}, se encuentra en la posicion: {indice2}")
    else:
        print("No se encontro al personaje Rocket Raccoon.")
        
# Listar todos los villanos de la lista.
def determinarVillano(list_pj):
    for personaje in list_pj:
        if personaje.es_villano:
            print(f"{personaje.nombre}, es villano?: {personaje.es_villano}")
            
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
def villanosAparicion1980(list_pj, villanos_queue):
    for personaje in list_pj:
        if personaje.es_villano and personaje.año_aparicion<1980:
            villanos_queue.arrive(personaje)
            
# Listar los superheores que comienzan con  Bl, G, My, y W.
def mostrarSHletra(list_pj):
    encontrado=False
    for personaje in list_pj:
        if not personaje.es_villano and personaje.nombre.startswith(("Bl", "G", "My", "W")):
            encontrado=True
            print(personaje)
            
    if not encontrado:
        print("No se encontro a ningun personaje que comienzan con  Bl, G, My, y W")

# Listado de superheroes ordenados por fecha de aparación.
def mostrarSuperHeroes(list_pj):
    for personajes in list_pj:
        print(f"{personajes.nombre}, año aparicion: {personajes.año_aparicion}")

# Modificar el nombre real de Ant Man a Scott Lang.
def cambiarNombre(list_pj):
    indice=list_pj.search("Ant Man", "nombre")
    if indice:
        list_pj[indice].nombre_real="Scott Lang"
        print("Nombre real de Ant Man modificado: ")
        print(f"Nombre: {list_pj[indice].nombre}, Nombre Real: {list_pj[indice].nombre_real}")
    else:
        print("No se encontro al personaje Ant Man.")
        
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
def mostrarPersonajesBiografia(list_SH):
    encontrado=False
    
    for personaje in list_SH:
        biografia = personaje.biografia
        if ("time-traveling" in biografia) or ("suit" in biografia):
            encontrado=True
            print(f"{personaje.nombre}, biografia: {personaje.biografia}")
    
    if not encontrado:
        print("No se encontro personajes que en su biografia incluyan la palabra time-traveling o suit.")
   
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
def eliminarPersonajesEspecificos(list_pj):
    eliminado1 = list_pj.delete_value("Electro", "nombre")
    if eliminado1:
        print("Eliminado:", eliminado1)
    else:
        print("No se encontro al personaje Electro")
        

    eliminado2 = list_pj.delete_value("Baron Zemo", "nombre")
    if eliminado2:
        print("Eliminado:", eliminado2)
    else:
        print("No se encontro al personaje Baron Zemo.")
 
  
#CUERPO PRINCIPAL
ordenarCriterios(list_personajes)
cargar_personajes(list_personajes, personajes)
list_personajes.sort_by_criterion("nombre")
print("Lista ordenada manera ascendente por nombre de los personajes:")
list_personajes.show()
print()
mostrarPosicion(list_personajes)
print()
print("Muestro todos los villanos de la lista: ")
determinarVillano(list_personajes)
print()
print("Villanos en los cuales aparecieron antes de 1980:")
villanosAparicion1980(list_personajes,villanosAparicion_queue)
villanosAparicion_queue.show()
print()
print("Los superheores que comienzan con  Bl, G, My, y W son: ")
mostrarSHletra(list_personajes)
print()
print("Listado de personajes ordenado por nombre real de manera ascendente de los personajes: ")
list_personajes.sort_by_criterion("nombre_real")
list_personajes.show()
print()
print("Listado de superheroes ordenados por fecha de aparicion: ")
list_personajes.sort_by_criterion("año_aparicion")
mostrarSuperHeroes(list_personajes)
print()
cambiarNombre(list_personajes)
print()
print("Personajes que en su biografia incluyan la palabra time-traveling o suit: ")
mostrarPersonajesBiografia(list_personajes)
print()
eliminarPersonajesEspecificos(list_personajes)