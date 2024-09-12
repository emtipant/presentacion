#Búsqueda en Arreglo Multidimensional
def buscar_en_arreglo(arreglo, valor_a_buscar):
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if arreglo[i][j] == valor_a_buscar:
                return f"El valor {valor_a_buscar} se encontró en la posición [{i}][{j}]"
    return f"El valor {valor_a_buscar} no se encontró en el arreglo"

arreglo = [
    [12, 24, 36],
    [48, 56, 64],
    [72, 80, 88]
]

valor_a_buscar = 56
resultado = buscar_en_arreglo(arreglo, valor_a_buscar)
print(resultado)
