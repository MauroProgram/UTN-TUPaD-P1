'''
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
'''

def gestionar_agenda():
    """
    Gestiona una agenda donde las claves son tuplas (día, hora) y los valores son eventos.
    Permite agregar eventos y consultar actividades en un día y hora específicos.
    """
    agenda = {} # Diccionario para almacenar los eventos

    while True:
        print("\n--- Gestión de Agenda ---")
        print("1. Agregar un evento")
        print("2. Consultar evento por día y hora")
        print("3. Mostrar todos los eventos")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            while True:
                try:
                    dia = input("Ingrese el día (ej. 'Lunes', 'Martes', etc.): ").strip().capitalize()
                    if not dia:
                        raise ValueError("El día no puede estar vacío.")

                    hora_str = input("Ingrese la hora (formato HH:MM, ej. 10:30): ").strip()
                    if not hora_str or len(hora_str) != 5 or hora_str[2] != ':':
                        raise ValueError("Formato de hora inválido. Use HH:MM.")

                    # Validar si los componentes de la hora son números
                    horas = int(hora_str[:2])
                    minutos = int(hora_str[3:])

                    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
                        raise ValueError("Hora o minutos fuera de rango.")

                    evento = input("Ingrese la descripción del evento: ").strip()
                    if not evento:
                        raise ValueError("La descripción del evento no puede estar vacía.")

                    clave = (dia, hora_str) # Crea la tupla como clave
                    if clave in agenda:
                        print(f"Ya existe un evento programado para el {dia} a las {hora_str}: '{agenda[clave]}'.")
                        confirmar = input("¿Desea sobrescribirlo? (s/n): ").lower()
                        if confirmar != 's':
                            print("Operación cancelada.")
                            break # Sale del bucle de agregar evento para volver al menú principal

                    agenda[clave] = evento
                    print(f"Evento '{evento}' agregado para el {dia} a las {hora_str}.")
                    break # Sale del bucle de agregar evento si todo es válido

                except ValueError as e:
                    print(f"Error al ingresar los datos: {e}. Intente de nuevo.")

        elif opcion == '2':
            while True:
                try:
                    dia_consulta = input("Ingrese el día a consultar (ej. 'Lunes'): ").strip().capitalize()
                    if not dia_consulta:
                        raise ValueError("El día no puede estar vacío.")

                    hora_consulta_str = input("Ingrese la hora a consultar (formato HH:MM, ej. 10:30): ").strip()
                    if not hora_consulta_str or len(hora_consulta_str) != 5 or hora_consulta_str[2] != ':':
                        raise ValueError("Formato de hora inválido. Use HH:MM.")

                    # Validar si los componentes de la hora son números
                    horas_cons = int(hora_consulta_str[:2])
                    minutos_cons = int(hora_consulta_str[3:])

                    if not (0 <= horas_cons <= 23 and 0 <= minutos_cons <= 59):
                        raise ValueError("Hora o minutos fuera de rango.")

                    clave_consulta = (dia_consulta, hora_consulta_str)
                    if clave_consulta in agenda:
                        print(f"Para el {dia_consulta} a las {hora_consulta_str} tenés: '{agenda[clave_consulta]}'.")
                    else:
                        print(f"No hay ningún evento programado para el {dia_consulta} a las {hora_consulta_str}.")
                    break # Sale del bucle de consulta si todo es válido

                except ValueError as e:
                    print(f"Error al ingresar los datos: {e}. Intente de nuevo.")

        elif opcion == '3':
            if agenda:
                print("\n--- Todos los Eventos Programados ---")
                # Ordenar los eventos por día y luego por hora para una mejor visualización
                eventos_ordenados = sorted(agenda.items())
                for (dia, hora), evento in eventos_ordenados:
                    print(f"- {dia} a las {hora}: {evento}")
            else:
                print("La agenda está vacía. ¡Agregá algunos eventos!")

        elif opcion == '4':
            print("Saliendo de la agenda. ¡Que tengas un buen día!")
            break

        else:
            print("Opción no válida. Por favor, ingresá un número del 1 al 4.")

# Ejecutar la función de gestión de agenda
if __name__ == "__main__":
    gestionar_agenda()