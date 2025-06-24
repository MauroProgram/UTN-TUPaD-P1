'''
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''
def gestionar_stock_productos():
    """
    Gestiona el stock de productos usando un diccionario. Permite a los usuarios:
    - Consultar el stock de un producto existente.
    - Agregar unidades al stock de un producto existente.
    - Agregar un nuevo producto y su stock inicial.
    """
    productos = {} # Inicializa un diccionario vacío para almacenar los productos y su stock

    while True:
        print("\n--- Gestión de Stock de Productos ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Mostrar todos los productos y su stock")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            nombre_producto = input("Ingrese el nombre del producto a consultar: ").strip().title()
            if nombre_producto in productos:
                print(f"El stock de {nombre_producto} es: {productos[nombre_producto]} unidades.")
            else:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")

        elif opcion == '2':
            nombre_producto = input("Ingrese el nombre del producto al que desea agregar stock: ").strip().title()
            if nombre_producto in productos:
                try:
                    unidades_a_agregar = int(input(f"¿Cuántas unidades desea agregar a {nombre_producto}?: "))
                    if unidades_a_agregar > 0:
                        productos[nombre_producto] += unidades_a_agregar
                        print(f"Se agregaron {unidades_a_agregar} unidades a {nombre_producto}. Nuevo stock: {productos[nombre_producto]}.")
                    else:
                        print("Por favor, ingrese un número positivo de unidades.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para las unidades.")
            else:
                print(f"El producto '{nombre_producto}' no existe. Si desea agregarlo, use la opción 3.")

        elif opcion == '3':
            nombre_producto = input("Ingrese el nombre del nuevo producto: ").strip().title()
            if nombre_producto in productos:
                print(f"El producto '{nombre_producto}' ya existe. Use la opción 2 para agregar más unidades.")
            else:
                try:
                    stock_inicial = int(input(f"Ingrese el stock inicial para {nombre_producto}: "))
                    if stock_inicial >= 0:
                        productos[nombre_producto] = stock_inicial
                        print(f"Se agregó '{nombre_producto}' con un stock inicial de {stock_inicial} unidades.")
                    else:
                        print("El stock inicial no puede ser negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para el stock inicial.")

        elif opcion == '4':
            if productos:
                print("\n--- Stock Actual de Productos ---")
                for producto, stock in productos.items():
                    print(f"- {producto}: {stock} unidades")
            else:
                print("El inventario está vacío.")

        elif opcion == '5':
            print("Saliendo del programa de gestión de stock. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Ejecutar el programa de gestión de stock
if __name__ == "__main__":
    gestionar_stock_productos()