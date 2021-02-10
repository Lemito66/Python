'''lista=["Emill",5,6,8,"Jorge"]
print(lista[-2])

nueva_tupla=tuple(lista)
print(nueva_tupla)

'''
tupla=("Emill","Jorge","Manuel",5)
mi_nombre,otro_nombre,tercero,numero=tupla
print(mi_nombre)

nueva_lista_antes_era_tupla=list(tupla)
print(nueva_lista_antes_era_tupla[-1])

numero_uno=input("Ingrese el primer número: ")
numero_dos=input("Ingrese el segundo número: ")

if numero_uno>numero_dos:
    print("El número: " + numero_uno +" es mayor al número: "+numero_dos)
elif numero_dos>numero_uno:
    print("El número: " + numero_dos +" es mayor al número: "+numero_uno)
else:
    print("El número: "+numero_uno+" es igual que el número: "+ numero_dos)

    


    