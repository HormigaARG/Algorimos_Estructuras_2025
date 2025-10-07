# 18. La armería de la base Starkiller, central de la primera orden, almacena los registros de los re-
# portes de fallos en armas de las tropas de sus principales generales –Kylo Ren, general Hux y
# capitana Phasma–. Para dicha labor, se solicita desarrollar un algoritmo que permita resolver
# las siguientes tareas:
# a. se debe registrar el nombre del general a cargo de la misión, fecha de la misión –a los fines
# del ejercicio considere como máximo 20 fechas de misiones–, código de blaster generado
# de manera aleatoria –de 8 dígitos y no puede estar repetido–, estado del blaster (si falló
# o no) y el tipo de soldado que portaba el blaster –Imperial Stromtrooper, Imperial Scout
# Trooper, Imperial Death Trooper, Sith Trooper o First Order Stromtrooper–;

# b. debe generar y cargar al menos 10 000 registros;

from binarytree import BinaryTree
from lista_reportes import reportes

# Creamos un árbol solo para los códigos de blaster
arbol_blaster = BinaryTree()

def cargar_reportes(arbol_codigos, reportes):
    for rep in reportes:
        arbol_codigos.insert(rep.codigo_blaster, rep)

# c. determinar el total de armas que fallaron por general
def fallos_por_general(arbol):
    def contar_fallos(nodo, contador):
        if nodo is not None:
            reporte = nodo.other_values
            if reporte.fallo:
                general = reporte.general
                if general not in contador:
                    contador[general] = 0
                contador[general] += 1
            
            contar_fallos(nodo.left, contador)
            contar_fallos(nodo.right, contador)
    
    if arbol.root is not None:
        contador_fallos = {}
        contar_fallos(arbol.root, contador_fallos)
        
        print("Cantidad de armas falladas por general:")
        for general in contador_fallos:
            cantidad = contador_fallos[general]
            print(f"- {general}: {cantidad}")


# d. indicar la cantidad y tipo de soldado de las misiones de Kylo Ren;
# def misiones_kylo_ren(arbol):
#     def buscar_misiones(nodo, resultados):
#         if nodo is not None:
#             reporte = nodo.other_values
#             # Verificar si es una misión de Kylo Ren
#             if reporte.general == "Kylo Ren":
#                 mision = {
#                     'tipo_soldado': reporte.tipo_soldado,
#                     'fallo': reporte.fallo,
#                     'arma': reporte.arma  # si existe este campo
#                 }
#                 resultados.append(mision)
            
#             buscar_misiones(nodo.left, resultados)
#             buscar_misiones(nodo.right, resultados)
    
#     if arbol.root is not None:
#         todas_misiones = []
#         buscar_misiones(arbol.root, todas_misiones)
        
#         # Contar por tipo de soldado
#         contador = {}
#         for mision in todas_misiones:
#             tipo = mision['tipo_soldado']
#             if tipo not in contador:
#                 contador[tipo] = 0
#             contador[tipo] += 1
        
#         print("Misiones de Kylo Ren:")
#         print(f"Total de misiones: {len(todas_misiones)}")
#         print("\nDistribución por tipo de soldado:")
#         for tipo_soldado in contador:
#             print(f"- {tipo_soldado}: {contador[tipo_soldado]} misiones")


# e. determinar cuántos Sith Troopers salieron en misiones y a cuantos les fallaron los blasters;
def sith_troopers_misiones(arbol):
    def __contar_troopers(nodo):
        if nodo is not None:
            # Contadores del nodo actual
            troopers_actual = 0
            fallos_actual = 0

            # Chequeo del nodo actual
            reporte = nodo.other_values
            if reporte.tipo_soldado == "Sith Trooper":
                troopers_actual = 1
                if reporte.fallo:
                    fallos_actual = 1

            # Recorro recursivamente los subárboles
            izq_troopers, izq_fallos = __contar_troopers(nodo.left)
            der_troopers, der_fallos = __contar_troopers(nodo.right)

            # Devuelvo la suma total
            return (troopers_actual + izq_troopers + der_troopers, 
                    fallos_actual + izq_fallos + der_fallos)
        else:
            # Caso base: nodo vacío
            return (0, 0)

    # Llamada inicial desde la raíz
    if arbol.root is not None:
        return __contar_troopers(arbol.root)
    else:
        print("El árbol está vacío")
        
# f. listar los códigos de los blasters de las misiones de una determinada fecha, indicando ade-
# más el porcentaje de armas que fallaron;
def blasters_por_fecha_y_porcentaje_arbol(arbol, fecha_buscada):
    
    # [0] = total_misiones_en_fecha
    # [1] = misiones_con_fallo
    contadores = [0, 0] 
    
    print(f"Análisis de misiones para la fecha {fecha_buscada}: ")
    print("Códigos de los blasters en misión:")

    def _recorrer_y_filtrar(nodo, contadores_lista):
        if nodo is None:
            return

        reporte = nodo.other_values
        
        if reporte.fecha == fecha_buscada:
            
            # Incrementamos el total de misiones
            contadores_lista[0] += 1
            print(f"- {reporte.codigo_blaster}")

            # Contar los fallos
            if reporte.fallo:
                contadores_lista[1] += 1
        
        _recorrer_y_filtrar(nodo.left, contadores_lista)
        _recorrer_y_filtrar(nodo.right, contadores_lista)

    if arbol.root is not None:
        _recorrer_y_filtrar(arbol.root, contadores)
        
    total_misiones_en_fecha = contadores[0]
    misiones_con_fallo = contadores[1]

    if total_misiones_en_fecha == 0:
        print("(No se encontraron misiones en esa fecha en el árbol.)")
        return
    
    
    porcentaje_fallo = (misiones_con_fallo / total_misiones_en_fecha) * 100
    
    print(f"Total de misiones reportadas: {total_misiones_en_fecha}")
    print(f"Misiones con fallo de arma: {misiones_con_fallo}")
    print(f"Porcentaje de armas que fallaron: {porcentaje_fallo:.2f}%")


# g. mostrar los datos del blaster código “75961380” si fue utilizado en alguna misión.
def buscar_codigo(arbol):
    nodo=arbol.search("75961380")
    
    if nodo:
        print("Se encontro el codigo del blaster 75961380, aqui sus datos: ")
        print(nodo.other_values)
    else:
        print("No se encontro ese numero de blaster.")
        
        
# MAIN
contador_troopers_mision = 0
contador_troopers_fallo = 0
cargar_reportes(arbol_blaster, reportes)
fallos_por_general(arbol_blaster)
print()
total_troopers, total_fallos = sith_troopers_misiones(arbol_blaster)
print("Estadísticas de Sith Troopers:")
print(f"Total en misiones: {total_troopers}")
print(f"Con fallos de blaster: {total_fallos}")
print()
blasters_por_fecha_y_porcentaje_arbol(arbol_blaster,2024)
print()
buscar_codigo(arbol_blaster)

