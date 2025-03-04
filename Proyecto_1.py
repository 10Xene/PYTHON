def convertBinaryToDecimal(numeroBinario):
    # Asegurarse de que el número está en str
    numeroTratar = str(numeroBinario)
    # Inicializar el resultado
    resultado = 0
    # Convertir de binario a decimal
    for digito in numeroTratar:
        resultado = resultado * 2 + int(digito)
    return str(resultado)


