# Programa para calcular moda, mediana y media de una lista aleatoria y determinar su sesgo.

# Importa funciones estadísticas y el módulo random para generar números.
from statistics import mode, median, mean
import random

# Crea una lista de 50 números enteros aleatorios entre 1 y 100.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula la moda, mediana y media de la lista y las almacena en variables.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Muestra la lista y los valores calculados para referencia.
print(f"Lista generada: {numeros_aleatorios}")
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")


# Compara los valores para determinar el sesgo según las definiciones dadas.
if media > mediana and mediana > moda:
    # Si la media es mayor que la mediana y esta mayor que la moda, hay sesgo positivo.
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    # Si la media es menor que la mediana y esta menor que la moda, hay sesgo negativo.
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    # Si la media, mediana y moda son iguales, no hay sesgo.
    print("Sin sesgo")
else:
    # Si no se cumple ninguna de las condiciones anteriores, indica que el sesgo no está definido claramente.
    print("Sesgo no determinado claramente")
