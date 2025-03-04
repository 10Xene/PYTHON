
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