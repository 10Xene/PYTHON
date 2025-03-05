def convertDecimalToBinary():
    numeroDecimal = input("Introduce un número decimal: ")
    numeroTratar = int(numeroDecimal)
    resultado = ""
    while numeroTratar > 0:
        resultado = str(numeroTratar % 2) + resultado
        numeroTratar = numeroTratar // 2
    return resultado
print(convertDecimalToBinary)