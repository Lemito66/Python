def numeroMayor():
    print("Escoje uno de estos numeros")
    numeroUno=input("Ingrese el primer numero: ")
    numeroDos=input("Ingrese el segundo numero: ")
    if numeroUno > numeroDos:
        print("El numero "+ numeroUno +" es mayor al "+ numeroDos)
    elif numeroDos>numeroUno:
        print("El número "+ numeroDos+" es mayor al " + numeroUno)
    else:
        print("Son iguales")

def Lista():
    lista=[10,20,30,40,50,60,70]
    lista.extend([80])
    print(lista)

Lista()
numeroMayor()

