#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
#def planteamiento: a*producto(a,b-1) -> si b==0: entonces es cero
def producto_recursivo(a,b):
    if b==1:
        return a
    elif b>0: #Si b es positivo, sumamos a, b veces
        return a * producto_recursivo(a,b-1) 
    
resultado=producto_recursivo(5,2)
print(resultado)
    