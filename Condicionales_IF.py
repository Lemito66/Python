""" print("Bienvenidos a mi programa de cambio de moneda")
nota=input("Ingresa la nota: ")

def calificacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion
print(calificacion(int(nota)))  """





nota=input("Ingrese la nota: ")


def notas(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion
print(notas(int(nota)))