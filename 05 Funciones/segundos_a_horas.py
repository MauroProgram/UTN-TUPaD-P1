'''
Crea un programa que reciba una cantidad de segundos como parametro y devuelva la cantidad de horas correspon dientes.

'''

#Funciones
def segundos_a_horas(segundos):
    return segundos / 3600

#Programa Principal
segundos = int(input("Ingrese una cantidad de segundos:"))
a_hora = segundos_a_horas(segundos)
print(a_hora)