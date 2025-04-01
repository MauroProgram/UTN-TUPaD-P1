# Determinar si una palabra termina o no con vocal

# Solicita al usuario una frase o palabra y la guarda como string
frase = input("Ingrese una frase o palabra")  # Quité los paréntesis innecesarios

# Calcula la longitud del string para encontrar la posición del último carácter
longitud = len(frase)

# Obtiene la última letra de la frase
ultima_letra = frase[longitud - 1]

# Convierte la última letra a minúscula y la guarda en una variable para usarla después
ultima_letra_minuscula = ultima_letra.lower()

# Verifica si la última letra (en minúscula) es una vocal (a, e, i, o, u)
if ultima_letra_minuscula == "a" or ultima_letra_minuscula == "e" or ultima_letra_minuscula == "i" or ultima_letra_minuscula == "o" or ultima_letra_minuscula == "u":
    print(frase + "!")  # Añade un signo de exclamación si termina en vocal
else:
    print(frase)  # Imprime la frase sin cambios si no termina en vocal