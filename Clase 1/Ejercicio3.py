# 3. Crea una función que reciba una lista de números y devuelva el valor máximo y mínimo de la lista.

def obtener_maximo_minimo(lista):
    # Usamos las funciones max() y min() para obtener el valor máximo y mínimo
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# Pedimos al usuario que ingrese una lista de números separados por espacios
entrada_lista = input("Introduce una lista de números separados por espacios: ")
# Convertimos la entrada en una lista de números
lista_numeros = [int(num) for num in entrada_lista.split()]

# Llamamos a la función para obtener el máximo y mínimo
maximo, minimo = obtener_maximo_minimo(lista_numeros)

# Mostramos el resultado
print(f"El valor máximo de la lista es: {maximo}")
print(f"El valor mínimo de la lista es: {minimo}")