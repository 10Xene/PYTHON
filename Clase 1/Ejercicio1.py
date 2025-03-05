# 1. Crea una función para detectar si un numero o texto es palindromo/capicúa

def es_palindromo(valor):
    """
    Función que verifica si un número o texto es palíndromo/capicúa.
    
    Parámetro:
        valor (int, str): Número o cadena de texto a evaluar.

    Retorna:
        bool: True si es palíndromo, False en caso contrario.
    """
    valor_str = str(valor)  # Convertimos el valor a cadena
    return valor_str == valor_str[::-1]  # Comparamos con su versión invertida

# Ejemplos de uso
print(es_palindromo("radar"))  # True
print(es_palindromo("python"))  # False
print(es_palindromo(12321))  # True
print(es_palindromo(12345))  # False
