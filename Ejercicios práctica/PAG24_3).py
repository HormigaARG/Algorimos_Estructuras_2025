#def planteamiento: a+producto(a,b-1) -> si b==0: entonces es cero
def producto_recursivo(a,b):
    if b==0:
        return 0
    elif b>0: #Si b es positivo, sumamos a, b veces
        return a + producto_recursivo(a,b-1) 
    else:    #Si b es negativo, llamamos a la funcion para el valor positivo y cambiamos el signo
        return -producto_recursivo(a,-b)
    
resultado=producto_recursivo(5,2)
print(resultado)
    