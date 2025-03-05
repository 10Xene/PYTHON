# 1. Crea una función para detectar si un numero o texto es palindromo/capicúa

def es_palindromo(valor):
    """
    Función que verifica si un número o texto es palíndromo/capicúa.
    
    Parámetro:
        valor (str): Cadena de texto a evaluar.

    Retorna:
        bool: True si es palíndromo, False en caso contrario.
    """
    valor_str = str(valor).replace(" ", "").lower()  # Convertimos a minúsculas y eliminamos espacios
    return valor_str == valor_str[::-1]  # Comparamos con su versión invertida

# Pedimos al usuario que introduzca un texto o número
entrada = input("Introduce una palabra o número: ")
if es_palindromo(entrada):
    print("Es un palíndromo/capicúa.")
else:
    print("No es un palíndromo/capicúa.")
