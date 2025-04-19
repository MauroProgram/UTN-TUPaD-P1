'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).

'''

# Inicializar la variable suma y el contador
suma = 0
contador = 0
# Utilizar un bucle for para pedir 100 números al usuario
for i in range(100):
    num = int(input("Ingrese un número entero: "))  # Pedir al usuario que ingrese un número
    suma += num  # Sumar el número actual a la suma total
    contador += 1  # Incrementar el contador de números ingresados
# Calcular la media
media = suma / contador  # Dividir la suma total entre el contador
# Imprimir la media
# (El resultado se redondea a 2 decimales para mayor claridad)
print("La media de los números ingresados es:", round(media, 2))  # Imprimir la media redondeada
