# 2. Escribe una función que reciba una lista de números y un número objetivo. La función debe devolver cuántas veces aparece el número.

def contar_apariciones(lista, objetivo):
    # Usamos el método count para contar las apariciones del número objetivo en la lista
    return lista.count(objetivo)

# Pedimos al usuario que ingrese una lista de números (como una cadena de texto)
entrada_lista = input("Introduce una lista de números separados por espacios: ")
# Convertimos la entrada en una lista de números
lista_numeros = [int(num) for num in entrada_lista.split()]

# Pedimos al usuario que ingrese el número objetivo
objetivo = int(input("Introduce el número objetivo a buscar: "))

# Llamamos a la función y mostramos el resultado
resultado = contar_apariciones(lista_numeros, objetivo)
print(f"El número {objetivo} aparece {resultado} veces en la lista.")
