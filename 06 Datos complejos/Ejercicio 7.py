'''
Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

'''

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107, 108}

# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", aprobados_ambos)

# Estudiantes que aprobaron solo uno de los dos
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno de los dos:", aprobados_solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
aprobados_totales = parcial1.union(parcial2)
print("Aprobaron al menos un parcial:", aprobados_totales)
