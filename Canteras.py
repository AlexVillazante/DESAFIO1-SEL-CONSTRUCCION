import numpy as np

# Definir la matriz de coeficientes
A = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])

# Definir el vector de resultados
b = np.array([4800, 5810, 5690])

# Calcular la inversa de la matriz
A_inv = np.linalg.inv(A)

# Mostrar la matriz inversa
print("La inversa de la matriz A es:")
print(A_inv)

# Multiplicamos la inversa de la matriz y la matriz de resultados
x = np.matmul(A_inv,b)
# Mostrar el resultado
print('Los metros cúbicos que se deben extraer de cada cantera son:')
print(x)
