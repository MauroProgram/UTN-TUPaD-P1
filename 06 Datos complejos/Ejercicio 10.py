'''
Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
'''

# Diccionario original: países como claves, capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Canadá": "Ottawa",
    "Japón": "Tokio"
}

# Creamos un nuevo diccionario vacío para almacenar la relación inversa
capitales_paises = {}

# Iteramos sobre el diccionario original
for pais, capital in paises_capitales.items():
    # Asignamos la capital como clave y el país como valor en el nuevo diccionario
    capitales_paises[capital] = pais

# Imprimimos ambos diccionarios para ver el resultado
print("--- Diccionario Original (País: Capital) ---")
print(paises_capitales)

print("\n--- Nuevo Diccionario (Capital: País) ---")
print(capitales_paises)