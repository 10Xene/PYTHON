# Escribe un programa en Python que contenga funciones.

# Solo habrá que entregar un archivo único en formato .txt aunque las ejecuciones las realices en formato .py, 
# el archivo tiene que estar formado del siguiente modo: Miguel_Platón.txt

# definir las siguientes funciones:

# 1. ConvertBinaryToDecimal

# 2. ConvertDecimalToBinary

# 3. convertDecimalToHexadecimal

# 4. convertHexadecimalToBinary

#

def convertBinaryToDecimal(numeroBinario):
    # Asegurarse de que el número esté en str
    numeroTratar = str(numeroBinario)
    
    # Convertir el número binario a decimal
    resultado = int(numeroTratar, 2)
    
    return resultado

#

def convertDecimalToBinary(numeroDecimal):
    # Asegurarse de que el número esté en str
    numeroTratar = str(numeroDecimal)
    
    # Convertir el número decimal a binario
    resultado = bin(int(numeroTratar))[2:]
    
    return resultado

#

def convertDecimalToHexadecimal(numeroDecimal):
    # Asegurarse de que el número esté en str
    numeroTratar = str(numeroDecimal)
    
    # Convertir el número decimal a hexadecimal
    resultado = hex(int(numeroTratar))[2:]
    
    return resultado

#

def convertHexadecimalToBinary(numeroHexadecimal):
    # Asegurarse de que el número esté en str
    numeroTratar = str(numeroHexadecimal)
    
    # Convertir el número hexadecimal a decimal
    numeroDecimal = int(numeroTratar, 16)
    
    # Convertir el número decimal a binario
    resultado = bin(numeroDecimal)[2:]
    
    return resultado

#