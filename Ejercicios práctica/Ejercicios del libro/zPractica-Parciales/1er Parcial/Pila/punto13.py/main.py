# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:

# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;
from stack import Stack
from trajeIronMan import TrajeIronMan

trajes_stack = Stack()

trajes=[
    TrajeIronMan("Mark I", "Iron Man (2008)", "Dañado"),
    TrajeIronMan("Mark XLIV (Hulkbuster)", "Iron Man 2 (2010)", "Impecable"),
    TrajeIronMan("Mark XLIV (Hulkbuster)", "Avengers Infinity War (2018)", "Destruido"),
    TrajeIronMan("Spider Man X1000", "Spider-Man: Homecoming", "Dañado"),
    TrajeIronMan("Capitan America F250", "Capitan America: Civil War", "Impecable"),       
]

def cargarPila (traje_stack,trajes):
    for traje in trajes:
        traje_stack.push(traje)
        
        
#a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#demás mostrar el nombre de dichas películas;
def determinarModelo(traje_stack):
    encontrado=False
    aux_stack=Stack()
    while trajes_stack.size()>0:
        traje=trajes_stack.pop()
        aux_stack.push(traje)
        
        if traje.modelo=="Mark XLIV (Hulkbuster)":
            encontrado=True
            print(f"Si, fue utilizado en la pelicula: {traje.pelicula}")
            
    if not encontrado:
        print("No, el modelo no fue utilizado en ninguna de las peliculas.")
        
    while aux_stack.size()>0:
        traje_stack.push(aux_stack.pop())
   
   
#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
def modelosDañados(traje_stack): 
    aux_stack=Stack()
    while trajes_stack.size()>0:
        traje=trajes_stack.pop()
        aux_stack.push(traje)
        
        if traje.estado=="Dañado":
            print(f"{traje.modelo}")
            
    while aux_stack.size()>0:
        traje_stack.push(aux_stack.pop())
        
#c. eliminar los modelos de los trajes destruidos mostrando su nombre;

def eliminarModelos(traje_stack):
    aux_stack=Stack()
    
    while trajes_stack.size()>0:
        traje=trajes_stack.pop()
        
        if traje.estado=="Destruido":
            print(f"{traje.modelo}")
        else:
            aux_stack.push(traje)
            
    while aux_stack.size()>0:
        traje_stack.push(aux_stack.pop())
      
#e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
#repetidos en una misma película;     
def agregarModelo(traje_stack):
    aux_stack=Stack()
    modelo_duplicado=False
    
    while traje_stack.size()>0:
        traje=traje_stack.pop()
        aux_stack.push(traje)
        
        if traje.modelo=="Mark LXXXLV" and traje.pelicula=="Avengers Endgame (2019)":
            modelo_duplicado=True
            
    if not modelo_duplicado:
        nuevoTraje=TrajeIronMan("Mark LXXXLV", "Avengers Endgame (2019)", "Impecable")
        aux_stack.push(nuevoTraje)
        
        
    while aux_stack.size()>0:
        traje_stack.push(aux_stack.pop())
        
#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#“Capitan America: Civil War”.
def mostrarNombresTrajes(traje_stack):
    aux_stack = Stack()
    while traje_stack.size() > 0:
        traje = traje_stack.pop()
        aux_stack.push(traje)
        if traje.pelicula in ("Spider-Man: Homecoming", "Capitan America: Civil War"):
            print(f"{traje.modelo}")
            
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())
        
        
#CP
cargarPila(trajes_stack,trajes)
print("El traje Mark XLIV (Hulkbuster) fue utilizado en algunas de la peliculas?:")
determinarModelo(trajes_stack)
print()
print("Modelos que quedaron dañados: ")
modelosDañados(trajes_stack)
print()
print("Eliminando modelos de los trajes destruidos mostrando su nombre: ")
eliminarModelos(trajes_stack)
print()
agregarModelo(trajes_stack)
print("Lista modificada despues de agregar el modelo Mark LXXXV: ")
trajes_stack.show()
print()
print("Trajes utilizados en las películas Spider-Man: Homecoming y Capitan America: Civil War: ")
mostrarNombresTrajes(trajes_stack)