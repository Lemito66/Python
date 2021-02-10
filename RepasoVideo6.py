def suma(numero_Uno,numero_Dos):
    operacion_Suma=numero_Uno+numero_Dos
    
    return operacion_Suma

def resta(numero_Uno,numero_Dos):
    operacion_resta=numero_Uno-numero_Dos
    
    return operacion_resta
def multiplicacion(numero_Uno,numero_Dos):
    operacion_multiplicacion=numero_Uno*numero_Dos
    
    return operacion_multiplicacion
def division(numero_Uno,numero_Dos):
    operacion_division=numero_Uno/numero_Dos
    
    return operacion_division


resultado_suma=suma(5,7)
resultado_resta=resta(5,7)
resultado_multiplicacion=multiplicacion(5,7)
resultado_division=division(5,7)

print("El resultado de la suma es: ")
print(resultado_suma)    
print("El resultado de la resta es: ")
print(resultado_resta)
print("El resultado de la multiplicacion es: ")
print(resultado_multiplicacion)
print("El resultado de la division es: ")
print(resultado_division)
    