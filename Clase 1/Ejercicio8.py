# 8. Crea una función que reciba un número entero y devuelva la suma de todos sus dígitos.

def calcular_promedio(lista):
    # Calculamos el promedio sumando todos los números y dividiendo entre la cantidad de elementos
    if len(lista) == 0:
        return 0  # Para evitar división por cero si la lista está vacía
    return sum(lista) / len(lista)

# Pedimos al usuario que ingrese una lista de números separados por espacios
entrada_lista = input("Introduce una lista de números separados por espacios: ")
# Convertimos la entrada en una lista de números
lista_numeros = [int(num) for num in entrada_lista.split()]

# Llamamos a la función para calcular el promedio
promedio = calcular_promedio(lista_numeros)

# Mostramos el resultado
print(f"El promedio de los números es: {promedio}")
