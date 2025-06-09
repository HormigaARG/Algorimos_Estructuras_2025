# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can- tidad de torneos ganados, 
# cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade- más la lista de sus Pokémons, 
# de los cuales se sabe: nombre, nivel, tipo y subtipo. 
# Se pide resolverlas siguientes actividades utilizando lista de lista implementando las funciones necesarias: 

from list_ import List
from entrenadores_pokemon import Entrenador, Pokemon, order_by_nombre

list_entrenadores = List()

entrenadores = [
    Entrenador("Lucia", 5, 10, 30),
    Entrenador("Carlos", 3, 7, 25),
    Entrenador("Laura", 4, 5, 20),
    Entrenador("Luis", 2, 12, 15),
    Entrenador("Ana", 6, 8, 40),
    Entrenador("Pedro", 1, 6, 10),
]

pokemons = [
    Pokemon("Pikachu", 50, "Eléctrico", "Ninguno", "Lucia"),
    Pokemon("Blastoise", 80, "Fuego", "Volador", "Lucia"),
    Pokemon("Squirtle", 35, "Agua", "Ninguno", "Carlos"),
    Pokemon("Bulbasaur", 40, "Planta", "Veneno", "Laura"),
    Pokemon("Bulbasaur", 70, "Fantasma", "Veneno", "Laura"),
    Pokemon("Machamp", 65, "Lucha", "Ninguno", "Luis"),
    Pokemon("Tyrantrum", 25, "Normal", "Hada", "Ana"),
    Pokemon("Eevee", 30, "Normal", "Ninguno", "Ana"),
    Pokemon("Pikachu", 55, "Roca", "Tierra", "Pedro"),
    Pokemon("Dragonite", 90, "Dragón", "Volador", "Pedro"),
]

def cargarEntrenador(list_coach, entrenadores):
    for coach in entrenadores:
        list_coach.append(coach)
    
def cargarPokemon(list_coach, pokemons):
    for pokemon in pokemons:
        for coach in list_coach:
            if coach.nombre == pokemon.nombreEntrenador:
                coach.pokemones.append(pokemon)
                
def ordenarCriterios(list_coach):
    list_coach.add_criterion("nombre", order_by_nombre)

def ordenarNombres(list_coach):
    list_coach.sort_by_criterion("nombre")
                
# a. obtener la cantidad de Pokémons de un determinado entrenador;
def obtenerCantidadPokemonesEspecifico(list_coach):
    c_contador=0
    for coach in list_coach:
        for pokemon in coach.pokemones:
            if coach.nombre=="Luis":
                c_contador+=1
    
    return c_contador

# b. listar los entrenadores que hayan ganado más de tres torneos; 
def mostrarEntrenadores(list_coach):
    for coach in list_coach:
        if coach.cantTorneosGanados>3:
            print(f"{coach.nombre}")
            
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados; 
def PokemonCoachMayor(list_coach):
    max_nivel=0
    max_torneos=0
    for coach in list_coach:
        if coach.cantTorneosGanados>max_torneos:
            max_torneos=coach.cantTorneosGanados
            nombreMayor=coach #Guardo el objeto entrenador, no el nombre.
            
    for pokemons in nombreMayor.pokemones:
        if pokemons.nivel>max_nivel:
            max_nivel=pokemons.nivel
            pokemonMayor=pokemons.nombre
                           
    print("El Pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados: ")
    print(f"Entrenador {nombreMayor.nombre}, Pokemon: {pokemonMayor}")
    
# d. mostrar todos los datos de un entrenador y sus Pokémons; 
def mostrarEntrenadorPokemon(list_coach):
    for coach in list_coach:
        if coach.nombre=="Pedro": #elijo a pedro por ejemplo
            print(f"T.ganados: {coach.cantTorneosGanados}, B.perdidas: {coach.cantBP}, B.ganadas: {coach.cantBG}")
            print("Pokemones: ")
            for pokemons in coach.pokemones:
                print(f"Nombre: {pokemons.nombre}, Nivel: {pokemons.nivel}, Tipo: {pokemons.tipo}, SubTipo: {pokemons.subtipo}")
                

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %; 
def entrenadoresPorcentaje79(list_coach):
    for coach in list_coach:
        totalBatallas=coach.cantBP + coach.cantBG
        Porcentaje=(coach.cantBG/totalBatallas)* 100
        if Porcentaje>79:
            print(f"{coach.nombre}, porcentaje: {Porcentaje}")
            
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo); 
def pokemonTipoSubtipo(list_coach):
    for coach in list_coach:
        for pokemon in coach.pokemones:
            if (pokemon.tipo=="Fuego") and (pokemon.subtipo=="Planta" or pokemon.subtipo=="Agua" or pokemon.subtipo=="Volador"):
                print(f"{coach.nombre}")                

#CP
cargarEntrenador(list_entrenadores, entrenadores)
cargarPokemon(list_entrenadores, pokemons)
ordenarCriterios(list_entrenadores)
ordenarNombres(list_entrenadores)
cantidadPokemones=obtenerCantidadPokemonesEspecifico(list_entrenadores)
print(f"La cantidad de pokemones de Luis es de: {cantidadPokemones} ")
print()
print("Entrenadores que hayan ganado mas de tres torneos: ")
mostrarEntrenadores(list_entrenadores)
print()
PokemonCoachMayor(list_entrenadores)
print()
print("Todos los datos de Pedro y sus Pokémons: ")
mostrarEntrenadorPokemon(list_entrenadores)
print()
print("Entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %: ")
entrenadoresPorcentaje79(list_entrenadores)
print()
print("Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo): ")
pokemonTipoSubtipo(list_entrenadores)




