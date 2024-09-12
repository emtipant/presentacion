# Matriz bidimensional
matriz = [
    [5, 2, 8],
    [1, 9, 3],
    [4, 7, 6]
]

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)


# Función para ordenar una fila específica utilizando QuickSort
def ordenar_fila_quicksort(matriz, fila):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)

    matriz[fila] = quicksort(matriz[fila])
    return matriz


# Ordenar la fila 1 de la matriz
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila_quicksort(matriz, fila_a_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)