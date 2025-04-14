#5. Desarrollar una función que permita convertir un número romano en un número decimal.
def roman_decimal(char):
    match char.upper():
            case 'I': return 1
            case 'V': return 5
            case 'X': return 10
            case 'L': return 50
            case 'C': return 100
            case 'D': return 500
            case 'M': return 1000

def roman(string):
    if not string: # Si la cadena esta vacia
        return 0
    else:
        decimal = roman_decimal(string[0])
        if len(string) > 1:
            if decimal < roman_decimal(string[1]):
                return -decimal + roman(string[1:])
    return decimal + roman(string[1:]) # Llama la cadena a partir del 2° caracter
        
print(roman('mmxxv'))