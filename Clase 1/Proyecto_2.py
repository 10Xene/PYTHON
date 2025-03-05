def convertDecimalToBinary():
    numeroDecimal = input("Introduce un número decimal: ")
    
    # Verificación de entrada válida
    if not numeroDecimal.isdigit():
        return "Error: Introduce un número decimal válido."

    numeroTratar = int(numeroDecimal)
    
    # Manejo del caso especial 0
    if numeroTratar == 0:
        return "0"

    resultado = ""
    while numeroTratar > 0:
        resultado = str(numeroTratar % 2) + resultado
        numeroTratar = numeroTratar // 2

    return resultado

print(convertDecimalToBinary())  # Corrección: llamar a la función
