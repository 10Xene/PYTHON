def convertBinaryToDecimal():
    numeroBinario = input("Introduce un número binario: ")
    
    # Verificación de entrada válida
    if not all(digito in '01' for digito in numeroBinario):
        return "Error: Introduce solo dígitos 0 y 1."

    resultado = 0
    for digito in numeroBinario:
        resultado = resultado * 2 + int(digito)

    return resultado  # No es necesario convertir a str

print(convertBinaryToDecimal())  # Llamada a la función
