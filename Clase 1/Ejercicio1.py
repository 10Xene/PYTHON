# 1. Crea una función para detectar si un numero o texto es palindromo/capicúa

def es_palindromo(texto):
    # Convertimos el texto a minúsculas y eliminamos espacios para compararlo correctamente
    texto = texto.replace(" ", "").lower()
    
    # Usamos un bucle para comparar los caracteres
    longitud = len(texto)
    for i in range(longitud // 2):
        if texto[i] != texto[longitud - 1 - i]:
            return False  # Si los caracteres no coinciden, no es palíndromo
    
    return True  # Si el bucle termina sin encontrar diferencias, es palíndromo

# Pedimos al usuario que ingrese un texto o número
entrada = input("Introduce un número o palabra para verificar si es palíndromo: ")

# Verificamos si la entrada es palíndromo y mostramos el resultado
if es_palindromo(entrada):
    print(f"'{entrada}' True.")
else:
    print(f"'{entrada}' False.")
