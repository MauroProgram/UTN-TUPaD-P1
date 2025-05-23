# Funciones
def calcular_imc(peso, altura):
    return peso / altura ** 2

# Programa principal
peso = int(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en centimetros: "))
print(f"Tu índice de masa corporal es: {calcular_imc(peso, altura)}")