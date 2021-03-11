import math

def derivada(x,ordenFuncion):
    mat=math.e
    deltaX=1*(mat**-5)
    y=0
    termino_Uno=funcion_Evaluar(x+deltaX)
    termino_Dos=funcion_Evaluar(x-deltaX)
    termino_Division=2*deltaX   
    y=(termino_Uno-termino_Dos)/termino_Division
    print(round(y))
    return y
def Funcion(x,orden,deltaX):
    if(orden!=0):
        termino_Uno=funcion_Evaluar(x+deltaX)
        termino_Dos=funcion_Evaluar(x-deltaX)
        termino_Division=2*deltaX
        # x=(termino_Uno-termino_Dos)/termino_Division
        # orden=orden-1
        return (Funcion(x+deltaX,orden-1,deltaX)-Funcion(x-deltaX,orden-1,deltaX))/termino_Division
    elif(orden==0):
        y= funcion_Evaluar(x)
    return y
    
def funcion_Evaluar(x):
    y=0
    y=2*x**4
    return y

x=float(input("Ingrese el numero el valor de x: \n"))
ordenFuncion=int(input("Ingrese el orden de la derivada: \n"))

mat=math.e
deltaX=1*(mat**-5)

# derivada(x,ordenFuncion)
y=Funcion(x,ordenFuncion,deltaX)
print("La respuesta es: " +str(y))




