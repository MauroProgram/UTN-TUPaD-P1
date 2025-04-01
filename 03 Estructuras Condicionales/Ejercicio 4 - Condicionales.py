# Programa para categorizar a una persona según su edad.

# Solicita la edad al usuario y la convierte a entero.
edad = int(input("Por favor, ingrese su edad: "))

# Clasifica la edad en categorías, empezando por los rangos más altos.
if edad >= 30:
    print("Tú eres un adulto.")
elif edad >= 18:  #Para ver si es mayor de edad
    print("Tú eres un joven.")
elif edad >= 12:  #Para ver si es un adolescente
    print("Tú eres un adolescente.")
elif edad >= 0:  # Asegura que la edad no sea negativa.
    print("Tú eres un niño.")
else: #Aseguramos valores correctos
    print("Error: La edad no puede ser negativa.")