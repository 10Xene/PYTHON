def convertDecimalToHexadecimal():
    numeroDecimal = input("Introduce un número decimal: ")
    numeroTratar = int(numeroDecimal)
    resultado = ""
    caracteresHexadecimales = "0123456789ABCDEF"
    while numeroTratar > 0:
        resultado = caracteresHexadecimales[numeroTratar % 16] + resultado
        numeroTratar = numeroTratar // 16
    return