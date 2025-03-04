
def convertDecimalToHexadecimal(numeroDecimal):
    # Asegurarse de que el número está en str
    numeroTratar = int(numeroDecimal)
    # Inicializar el resultado
    resultado = ""
    # Tabla de caracteres hexadecimales
    caracteresHexadecimales = "0123456789ABCDEF"
    # Convertir de decimal a hexadecimal
    while numeroTratar > 0:
        resultado = caracteresHexadecimales[numeroTratar % 16] + resultado
        numeroTratar = numeroTratar // 16
    return resultado
