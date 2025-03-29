# TRABAJO PRACTICO 1
# Nombre: Mauro Ezequiel Ponce
# Comision: 19
import math  # Importamos math para usar pi en el cálculo del círculo

#-----Ejercicio 1 -----
# Imprime un mensaje simple: "Hola Mundo!"
def ejercicio1():
    print("Hola Mundo!")

#---Ejercicio 2------
# Pide el nombre del usuario y lo saluda
def ejercicio2():
    nombre = input("Por favor, ingresa tu nombre: ")
    print(f"Hola {nombre}!")

#---Ejercicio 3------
# Pide nombre completo, edad y lugar de residencia, luego muestra un resumen
def ejercicio3():
    nombre = input("Hola, por favor, ingresa tu nombre completo: ")
    edad = input("Ahora, ingresa tu edad: ")
    hogar = input("Finalmente, ingresa tu lugar de residencia: ")
    print(f"Hola {nombre}, ahora mismo tienes {edad} y vives en {hogar}")

#---Ejercicio 4------
# Calcula el área y perímetro de un círculo a partir del radio ingresado
def ejercicio4():
    radio = float(input("Ahora ingresa el radio de un círculo: "))
    area = math.pi * radio ** 2  # Área: π * radio al cuadrado
    perimetro = 2 * math.pi * radio  # Perímetro: 2 * π * radio
    print(f"El área del círculo es {area:.2f} unidades cuadradas.")
    print(f"El perímetro del círculo es {perimetro:.2f} unidades.")

#---Ejercicio 5------
# Convierte minutos a horas dividiendo entre 60
def ejercicio5():
    minutos = int(input("Ingrese una cantidad de minutos: "))
    horas = minutos / 60  # Divide los minutos entre 60 para obtener horas
    print(f"{minutos} minutos equivale a {horas:.2f} horas")  # Muestra con 2 decimales

#---Ejercicio 6------
# Muestra la tabla de multiplicar de un número del 1 al 10
def ejercicio6():
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    resultado1 = numero * 1
    print(f"{numero} x 1 = {resultado1}")
    resultado2 = numero * 2
    print(f"{numero} x 2 = {resultado2}")
    resultado3 = numero * 3
    print(f"{numero} x 3 = {resultado3}")
    resultado4 = numero * 4
    print(f"{numero} x 4 = {resultado4}")
    resultado5 = numero * 5
    print(f"{numero} x 5 = {resultado5}")
    resultado6 = numero * 6
    print(f"{numero} x 6 = {resultado6}")
    resultado7 = numero * 7
    print(f"{numero} x 7 = {resultado7}")
    resultado8 = numero * 8
    print(f"{numero} x 8 = {resultado8}")
    resultado9 = numero * 9
    print(f"{numero} x 9 = {resultado9}")
    resultado10 = numero * 10
    print(f"{numero} x 10 = {resultado10}")

#---Ejercicio 7------
# Realiza suma, resta, multiplicación y división de dos números
def ejercicio7():
    num1 = int(input("Ingresa un número distinto de 0: "))
    num2 = int(input("Ingresa otro número distinto de 0: "))
    suma = num1 + num2  # Suma los dos números
    resta = num1 - num2  # Resta el segundo del primero
    multiplicacion = num1 * num2  # Multiplica ambos números
    division = num1 / num2  # Divide el primero por el segundo
    print(f"El resultado de SUMAR {num1} y {num2} es {suma}")
    print(f"El resultado de RESTAR {num1} y {num2} es {resta}")
    print(f"El resultado de MULTIPLICAR {num1} y {num2} es {multiplicacion}")
    print(f"El resultado de DIVIDIR {num1} y {num2} es {division:.2f}")  # 2 decimales para división

#---Ejercicio 8------
# Calcula el índice de masa corporal (IMC) con altura y peso
def ejercicio8():
    altura = float(input("Por favor, ingresa cuanto mides (en metros): "))
    peso = float(input("Por favor, ingresa cuanto pesas (en kg): "))
    imc = peso / (altura ** 2)  # IMC: peso dividido por altura al cuadrado
    print(f"Tu índice de masa corporal (IMC) es de {imc:.2f}")

#---Ejercicio 9------
# Convierte grados Celsius a Fahrenheit
def ejercicio9():
    celcius = float(input("Ingresa una temperatura en grados Celsius: "))
    fahrenheit = (9 / 5) * celcius + 32  # Fórmula: (9/5) * C + 32
    print(f"La conversión de {celcius} grados Celsius es de {fahrenheit:.2f} grados Fahrenheit")

#---Ejercicio 10------
# Calcula el promedio de tres números enteros
def ejercicio10():
    num1 = int(input("Ingresa un número entero: "))
    num2 = int(input("Ingresa otro número entero: "))
    num3 = int(input("Ingresa un tercer número entero: "))
    promedio = (num1 + num2 + num3) / 3  # Suma los 3 y divide entre 3
    print(f"El promedio de {num1}, {num2}, {num3} es de {promedio:.2f}")

# Ejecución de todos los ejercicios en orden
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
ejercicio8()
ejercicio9()
ejercicio10()