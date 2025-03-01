def convertBinaryToDecimal(numeroBinario):
    # Asegurarse de que el número esté en str
    numeroTratar = str(numeroBinario)
    # Convertir el número binario a decimal
    resultado = int(numeroTratar, 2)
    
    return resultado