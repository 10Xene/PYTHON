def convertDecimalToHexadecimal():
    numeroDecimal = input("Introduce un número decimal: ")

    # Verificación de entrada válida
    if not numeroDecimal.isdigit():
        return "Error: Introduce un número decimal válido."

    numeroTratar = int(numeroDecimal)

    # Manejo del caso especial 0
    if numeroTratar == 0:
        return "0"

    resultado = ""
    caracteresHexadecimales = "0123456789ABCDEF"

    while numeroTratar > 0:
        resultado = caracteresHexadecimales[numeroTratar % 16] + resultado
        numeroTratar = numeroTratar // 16

    return resultado  # Ahora retorna el resultado correctamente

print(convertDecimalToHexadecimal())  # Corrección: llamada a la función
