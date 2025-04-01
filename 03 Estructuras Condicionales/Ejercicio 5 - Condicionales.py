# Programa para validar que una contraseña tenga entre 8 y 14 caracteres.

# Solicita al usuario que ingrese una contraseña y la guarda como cadena.
password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

# Evalúa la longitud de la contraseña usando len() para verificar si está en el rango permitido.
if len(password) >= 8 and len(password) <= 14:
    # Si la longitud está entre 8 y 14 (incluyendo ambos), muestra un mensaje de éxito.
    print("Ha ingresado una contraseña correcta")
    #Si la longitud no cumple con el rango, pide al usuario ajustarse al requisito.
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 