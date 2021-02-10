def suma(numero_uno,numero_dos):
	operacion_suma=numero_uno+numero_dos
	return operacion_suma
def resta(numero_uno,numero_dos):
	operacion_resta=numero_uno - numero_dos
	return operacion_resta

def multiplicacion(numero_uno,numero_dos):
	operacion_multiplicacion=	numero_uno*numero_dos
	return operacion_multiplicacion

def division(numero_uno,numero_dos):
	operacion_division= numero_uno/numero_dos
	return operacion_division
			

resultado_suma=suma(5,7)
resultado_resta=resta(5,7)
resultado_multiplicacion=multiplicacion(5,7)
resultado_division=division(5,7)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)