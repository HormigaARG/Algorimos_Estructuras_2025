N=4
t_vector=[0] * N

notas=t_vector

def inicializar_vector(nota):
    for i in range(0,N):
        nota[i]=0

def cargar_vector(nota):
    for i in range(0,N):
        nota[i]=float(input(f"Ingrese la nota {i}: "))

def promedio(nota):
    prom=0
    for i in range(0,N):
        prom=prom + nota[i]
    return (prom/N)
    
        
#BEGIN
inicializar_vector(notas)
cargar_vector(notas)
print()
print(f"El promedio de notas del estudiante es: {promedio(notas)}")


#END.