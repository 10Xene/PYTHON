def convertBinaryToDecimal(numeroBinario):
    # Asegurarse de que el número está en str
    numeroTratar = str(numeroBinario)
    # Inicializar el resultado
    resultado = 0
    # Convertir de binario a decimal
    for digito in numeroTratar:
        resultado = resultado * 2 + int(digito)
    return str(resultado)

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

def convertHexadecimalToBinary(numeroHexadecimal):
    # Asegurarse de que el número está en str
    numeroTratar = numeroHexadecimal.upper()
    # Tabla de caracteres hexadecimales a binarios
    caracteresBinarios = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    # Inicializar el resultado
    resultado = ""
    # Convertir de hexadecimal a binario
    for digito in numeroTratar:
        resultado += caracteresBinarios[digito]
    return resultado
