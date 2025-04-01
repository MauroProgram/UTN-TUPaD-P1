# Programa para determinar si un estudiante aprueba o desaprueba según su calificación.

# Solicita la calificación al usuario y la convierte a un número decimal (float).
nota = float(input("Por favor, ingrese su calificación (0 a 10): "))

# Verifica si la nota es suficiente para aprobar (mayor o igual a 6).
if nota >= 6:
    print(f"Aprobado con una calificación de {nota}.")
# Verifica si la nota es negativa, lo cual no es válido.
elif nota < 0:
    print("La calificación no puede ser negativa. Ingrese un valor válido.")
# Verifica si la nota está fuera del rango superior (mayor a 10).
elif nota > 10:
    print("La calificación no puede ser mayor a 10. Ingrese un valor válido.")
# Cubre las notas entre 0 y 5.99, indicando que el estudiante desaprobó.
else:
    print(f"Desaprobado con una calificación de {nota}.")