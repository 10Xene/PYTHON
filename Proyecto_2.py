def convertDecimalToBinary(numeroDecimal):
    # Asegurarse de que el número está en str
    numeroTratar = int(numeroDecimal)
    # Inicializar el resultado
    resultado = ""
    # Convertir de decimal a binario
    while numeroTratar > 0:
        resultado = str(numeroTratar % 2) + resultado
        numeroTratar = numeroTratar // 2
    return resultado
