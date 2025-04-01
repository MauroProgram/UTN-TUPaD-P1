# Programa que ofrece un menú de opciones para transformar el nombre ingresado por el usuario.

# Solicita al usuario que ingrese su nombre y lo almacena como una cadena en la variable 'nombre'.
nombre = input("Por favor, ingrese su nombre")

# Pide al usuario que elija una opción (1, 2 o 3) y muestra las opciones en líneas separadas usando '\n'.
# La entrada se guarda como una cadena en la variable 'opcion'.
opcion = input(" y una opcion: \n-1\n-2\n-3 ")

# Compara si la opción ingresada es "1"; si es así, convierte el nombre a mayúsculas y lo imprime.
if opcion == "1":
    print(nombre.upper())  # Transforma todo el nombre a mayúsculas, como "PEDRO".

# Si la opción no es "1", verifica si es "2"; en ese caso, convierte el nombre a minúsculas y lo imprime.
elif opcion == "2":
    print(nombre.lower())  # Transforma todo el nombre a minúsculas, como "pedro".

# Si no es "1" ni "2", comprueba si es "3"; entonces, pone la primera letra de cada palabra en mayúscula.
elif opcion == "3":
    print(nombre.title())  # Convierte el nombre a formato título, como "Pedro" o "Juan Perez".

# Si ninguna de las opciones anteriores coincide (no es "1", "2" ni "3"), muestra un mensaje de error.
else:
    print("Elige una opcion correcta: 1,2 o 3")  # Indica que la entrada no es válida y sugiere las opciones correctas.