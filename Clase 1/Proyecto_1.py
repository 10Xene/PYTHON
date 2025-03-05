def convertBinaryToDecimal():
    numeroBinario = input("Introduce un número binario: ")
    numeroTratar = str(numeroBinario)
    resultado = 0
    for digito in numeroTratar:
        resultado = resultado * 2 + int(digito)
        
    return str(resultado)
print(convertBinaryToDecimal)