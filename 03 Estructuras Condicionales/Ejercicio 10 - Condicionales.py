# Programa para determinar la estación del año según el hemisferio, mes y día ingresados.

# Pide al usuario que indique si está en el Hemisferio Norte o Sur y guarda la respuesta como texto.
hemisferio = input("En que hemisferio te encuentras? Norte o Sur")

# Solicita el mes actual como texto, sin convertirlo a otro formato.
mes = input("Ingresa el mes actual")

# Pide el día del mes y lo convierte a número entero para compararlo.
dia = int(input("Que dia es hoy?"))


# Evalúa si el hemisferio ingresado es exactamente 'N' (Norte).
if hemisferio == 'N':
        # Determina si es invierno en el Hemisferio Norte:
        # - Desde el 21 de diciembre hasta el 20 de marzo.
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            print("Invierno")  # Imprime "Invierno" si se cumple esta condición.
        # Determina si es primavera:
        # - Desde el 21 de marzo hasta el 20 de junio.
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            print("Primavera")  # Imprime "Primavera" para este rango.
        # Determina si es verano:
        # - Desde el 21 de junio hasta el 20 de septiembre.
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            print("Verano")  # Imprime "Verano" para este rango.
        # Si no se cumple ninguna de las anteriores, asume otoño:
        # - Desde el 21 de septiembre hasta el 20 de diciembre.
        else:
            print("Otoño")  # Imprime "Otoño" 
# Si el hemisferio no es 'N', asume que es Hemisferio Sur.
else:  # Hemisferio Sur
        # Determina si es verano en el Hemisferio Sur:
        # - Desde el 21 de diciembre hasta el 20 de marzo.
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            print("Verano")  # Imprime "Verano" para este período.
        # Determina si es otoño:
        # - Desde el 21 de marzo hasta el 20 de junio.
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            print("Otoño")  # Imprime "Otoño"
        # Determina si es invierno:
        # - Desde el 21 de junio hasta el 20 de septiembre.
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            print("Invierno")  # Imprime "Invierno" para este rango.
        # Si no se cumple ninguna de las anteriores, asume primavera:
        # - Desde el 21 de septiembre hasta el 20 de diciembre.
        else:
            print( "Primavera")  # Imprime "Primavera" para el resto del año.