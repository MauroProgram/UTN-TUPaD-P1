'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno

'''

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input("Ingrese la nota {}: ".format(j + 1))) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print("El promedio de {} es: {:.2f}".format(nombre, promedio))
