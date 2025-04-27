'''
Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
'''

mi_lista = list(range(10,31,5))
primeros_dos = mi_lista[:2]
print(f"Los dos primeros números de la lista son: {primeros_dos}")  