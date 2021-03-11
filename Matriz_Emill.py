
import numpy as np


A = np.array([[2,-1,1],
              [3,1,-2],
              [-1,2,5]])

B = np.array([[2],
              [9],
              [-5]])


casicero = 1e-15 


A = np.array(A,dtype=float) 


matrizAumentada  = np.concatenate((A,B),axis=1)
primeraMatriz = np.copy(matrizAumentada)


tamano = np.shape(matrizAumentada)
n = tamano[0]
m = tamano[1]

# Para cada fila en matrizAumentada
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna  = matrizAumentadas(matrizAumentada[i:,i])
    dondemax = np.argmax(columna)
    
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(matrizAumentada[i,:])
        matrizAumentada[i,:] = matrizAumentada[dondemax+i,:]
        matrizAumentada[dondemax+i,:] = temporal
segundaMatriz = np.copy(matrizAumentada)


for i in range(0,n-1,1): #eliminacion para adelante
    pivote   = matrizAumentada[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor  = matrizAumentada[k,i]/pivote
        matrizAumentada[k,:] = matrizAumentada[k,:] - matrizAumentada[i,:]*factor

# sustitución hacia atrás
ultfila = n-1
ultcolumna = m-1
X = np.zeros(n,dtype=float)

for i in range(ultfila,0-1,-1):
    suma = 0
    for j in range(i+1,ultcolumna,1):
        suma = suma + matrizAumentada[i,j]*X[j]
    b = matrizAumentada[i,ultcolumna]
    X[i] = (b-suma)/matrizAumentada[i,i]

X = np.transpose([X])


# SALIDA
print('Matriz aumentada:')
print(primeraMatriz)
print('Pivoteo parcial por filas')
print(segundaMatriz)
print('eliminación hacia adelante')
print(matrizAumentada)
print('solución: ')
print(X)