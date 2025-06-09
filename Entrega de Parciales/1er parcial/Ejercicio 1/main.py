# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.


# funcion recursiva para buscar, determinar si Capitan America esta en la lista.
def buscarCapitanAmerica(lista, buscado, indice=0):
    if indice >= len(lista):
        return False 
    if lista[indice] == buscado:
        return True
    else:
        return buscarCapitanAmerica(lista, buscado, indice + 1)

# funcion recursiva para listar los superheroes de la lista.
def mostrarSuperHeroes(lista, indice=0):
    if indice >= len(lista):
        return "" #si el indice (posicion) es mayor a el tamaño de la lista, devuelve vacio
    else:
        print(lista[indice]) #vamos imprimiendo uno por uno
        mostrarSuperHeroes(lista, indice + 1)



#CUERPO PRINCIPAL:
superheroes = [
    "Doctor Doom", "Magneto", "Loki", "Thanos", "Red Skull",
    "Green Goblin", "Doctor Octopus", "Venom", "Ultron", "Kingpin",
    "Hela","Capitan America","Galactus", "Taskmaster", "Baron Zemo"
]

encontrado = buscarCapitanAmerica(superheroes, "Capitan America")
print(f"Capitan America está en la lista?: {encontrado}")
print()
print("Listado de superhéroes:")
mostrarSuperHeroes(superheroes)

