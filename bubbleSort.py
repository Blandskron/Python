def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del arreglo
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorrer el arreglo desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
example_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(example_array)
print(sorted_array)
