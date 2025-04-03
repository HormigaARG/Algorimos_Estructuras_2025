def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(f"El factorial del numero 5 es: {factorial(5)}")