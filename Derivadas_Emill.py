import math

def derivada(x,ordenFuncion):
    mat=math.e
    derivada_X=1*(mat**-5)
    y=0
    termino_Uno=funcion_Evaluar(x+derivada_X)
    termino_Dos=funcion_Evaluar(x-derivada_X)
    termino_Division=2*derivada_X   
    y=(termino_Uno-termino_Dos)/termino_Division
    print(round(y))
    return y
def funcion_Evaluar(x):
    y=0
    y=x**2-4
    return y

x=float(input("Ingrese el numero el valor de x: \n"))
ordenFuncion=int(input("Ingrese el orden de la derivada: \n"))

derivada(x,ordenFuncion)



