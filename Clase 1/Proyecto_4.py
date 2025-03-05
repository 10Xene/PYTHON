def convertHexadecimalToBinary():
    numeroHexadecimal = input("Introduce un número hexadecimal: ").upper()

    caracteresBinarios = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    resultado = ""

    # Verificación de entrada válida
    for digito in numeroHexadecimal:
        if digito not in caracteresBinarios:
            return "Error: Introduce un número hexadecimal válido."

        resultado += caracteresBinarios[digito]

    return resultado

print(convertHexadecimalToBinary())  # Corrección: llamada a la función
