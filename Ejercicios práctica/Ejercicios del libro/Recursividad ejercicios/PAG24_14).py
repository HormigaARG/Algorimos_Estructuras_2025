#14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.
def suma_digitos(digito):
    if (digito==0): 
        return 0
    else:
        ultimo = digito % 10
        return ultimo + suma_digitos(digito//10)  # Va quitando un dígito por llamada
print(f"La suma de dígitos del 123 es: {suma_digitos(266)}")