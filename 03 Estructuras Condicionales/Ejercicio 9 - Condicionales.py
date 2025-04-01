# Programa para clasificar la magnitud de un terremoto según la escala de Richter.

# Solicita al usuario la magnitud del terremoto y la convierte a un número decimal (float).
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Evalúa si la magnitud es negativa, lo cual no es válido en la escala de Richter.
if magnitud < 0:
    print("Ese número no es propio de la escala Richter")
# Si no es negativa, clasifica la magnitud en las categorías según los rangos definidos.
elif magnitud < 3:
    print("Muy leve (imperceptible)")
# Verifica si la magnitud está entre 3 y 4 (incluye 3, excluye 4).
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
# Verifica si la magnitud está entre 4 y 5 (incluye 4, excluye 5).
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
# Verifica si la magnitud está entre 5 y 6 (incluye 5, excluye 6).
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
# Verifica si la magnitud está entre 6 y 7 (incluye 6, excluye 7).
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
# Si la magnitud es 7 o más, clasifica como extremo.
elif magnitud >= 7 and magnitud <= 10:
    print("Extremo (puede causar graves daños a gran escala)")
# Si la magnitud es mayor a 10, considera que no es típica de la escala Richter.
else:
    print("Ese número no es propio de la escala Richter")