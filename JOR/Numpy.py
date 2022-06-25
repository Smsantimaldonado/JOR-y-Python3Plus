import numpy as np

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array1 = np.array(lista1, dtype=object)
print(lista1)
print(array1)
print(type(array1))

lista2 = [lista1, lista1, 10, 11]
array2 = np.array(lista2, dtype=object)
print(lista2)
print(array2)

lista3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array3 = np.array(lista3, dtype=object)
print(lista3)
print(array3)

array4 = np.arange(2, 25, 2)
print(array4)

matrizCeros = np.zeros((4, 5), dtype=object)
print(matrizCeros)

print(np.linspace(2, 4, 3))

print(np.random.randn(2, 6, 10))

array5 = np.random.randint(1, 900, 100)
print(array5)
maximo = array5.max()
print(f'El máximo es {maximo}')
posmax = array5.argmax()
print(f'La posicion es {posmax}')

print(array1)
array6 = array1.copy()
print(array6)
array6[2] = 890
print(array1)
print(array6)

array7 = np.random.randint(1, 100, 12)
print(array7)
matriz = array7.reshape(3, 4)
print(matriz)

print(matriz[:][1])
print(matriz[:][:1])
print(matriz[:][0])
print(matriz[0])

print(matriz[:, 1])
print(matriz[:, :1])
print(matriz[:, 0])
print(matriz[0])

print(matriz[1][1])
print(matriz[:][1])

print(matriz[1, 1])

print(matriz)
print(matriz[:, 1])
print(matriz[:][1])

print(np.max(matriz))
print(np.argmax(matriz))

condicion = matriz > 10
print(condicion)
print(matriz[condicion])
