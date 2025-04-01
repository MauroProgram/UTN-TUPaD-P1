# Programa para verificar si el usuario es mayor de edad según su edad ingresada.

# Programa para verificar si el usuario es mayor de edad según su edad ingresada.

# Solicita la edad al usuario y convierte la entrada directamente a entero.
edad = int(input("Por favor, ingresa tu edad: "))

# Evalúa si la edad es mayor o igual a 18 para determinar si es mayor de edad.
if edad >= 18:
    print("Eres mayor de edad.")
# Verifica si el usuario ingresó un valor negativo.
elif edad < 0:
    print("La edad no puede ser negativa. Ingresa un valor válido.")
# Cubre edades entre 0 y 17, indicando que el usuario es menor de edad.
else:
    print("Eres menor de edad.")