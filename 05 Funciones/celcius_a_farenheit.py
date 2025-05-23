# Funciones
def celcius_a_farenheit(celcius):
    return (celcius * 9/5) + 32

# Programa principal
grados = float(input("Ingresa la temperatura en Celsius: "))
print(f"La conversión desde Celsius a Fahrenheit es: {celcius_a_farenheit(grados)}")                                                      