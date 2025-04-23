# Definición de funciones

def decimal_a_binario(decimal):
    # Función que convierte un número decimal (entero) a binario
    if decimal == 0:
        # Si el número es 0, devuelve directamente "0" como cadena
        return "0"
    binario = ""
    # Inicializa una cadena vacía para almacenar el número binario
    while decimal > 0:
        # Mientras el número sea mayor que 0, realiza la conversión
        binario = str(decimal % 2) + binario
        # Obtiene el residuo (0 o 1) al dividir entre 2 y lo agrega al inicio de la cadena
        decimal //= 2
        # Divide el número entre 2 (división entera) para continuar el proceso
    return binario
    # Devuelve la cadena que representa el número binario

def binario_a_decimal(binario):
    # Función que convierte un número binario (cadena de 0s y 1s) a decimal
    decimal = 0
    # Inicializa la variable para almacenar el número decimal
    potencia = 0
    # Inicializa un contador para la potencia de 2
    for digito in reversed(binario):
        # Recorre la cadena binaria de derecha a izquierda
        if digito == '1':
            # Si el dígito es 1, suma 2 elevado a la potencia actual
            decimal += 2 ** potencia
        potencia += 1
        # Incrementa la potencia para la siguiente posición
    return decimal
    # Devuelve el número decimal equivalente

# Programa principal
while True:
    # Ciclo infinito para mantener el menú activo hasta que el usuario decida salir
    print("\nSeleccione la conversión:")
    # Muestra un salto de línea y el título del menú
    print("1. Decimal a binario")
    # Opción 1: Convertir de decimal a binario
    print("2. Binario a decimal")
    # Opción 2: Convertir de binario a decimal
    print("3. Salir")
    # Opción 3: Terminar el programa

    opcion = input("Ingrese su opción: ")
    # Lee la opción ingresada por el usuario como una cadena

    if opcion == '1':
        # Si el usuario elige la opción 1
        decimal = int(input("Ingrese un número decimal entero: "))
        # Pide un número decimal y lo convierte a entero
        binario = decimal_a_binario(decimal)
        # Llama a la función para convertir el número a binario
        print(f"Binario: {binario}")
        # Muestra el resultado de la conversión
    elif opcion == '2':
        # Si el usuario elige la opción 2
        binario = input("Ingrese el número binario: ")
        # Pide una cadena que representa el número binario
        if all(digito in '01' for digito in binario):
            # Verifica que la cadena solo contenga 0s y 1s
            decimal = binario_a_decimal(binario)
            # Llama a la función para convertir el binario a decimal
            print(f"Decimal: {decimal}")
            # Muestra el resultado de la conversión
        else:
            # Si la entrada no es válida (contiene caracteres distintos a 0 o 1)
            print("Entry inválida. Por favor, ingrese un número binario válido.")
            # Muestra un mensaje de error
    elif opcion == '3':
        # Si el usuario elige la opción 3
        break
        # Rompe el ciclo while, terminando el programa
    else:
        # Si el usuario ingresa una opción no válida
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
        # Muestra un mensaje de error

print("Programa finalizado.")
# Al salir del ciclo, muestra un mensaje indicando que el programa ha terminado
