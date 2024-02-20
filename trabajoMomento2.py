# Variables para acumular totales
total_guajira = 0
total_chicamocha = 0
total_llanos = 0
total_adultos = 0
total_ninos = 0
total_general = 0

# Ciclo para ingresar cotizaciones
while True:
    # Solicitar información del cliente
    nombre_cliente = input("Ingrese el nombre del cliente (o 'fin' para finalizar): ")

    # Verificar si se debe finalizar el proceso
    if nombre_cliente.lower() == 'fin':
        break

    destino = input("Ingrese el destino (Guajira, Chicamocha o Llanos Orientales): ")
    personas_adultas = int(input("Ingrese el número de personas adultas: "))
    personas_ninos = int(input("Ingrese el número de niños: "))

    # Calcular el subtotal
    if destino.lower() == 'guajira':
        subtotal = 1450000 * personas_adultas + 870000 * personas_ninos
        total_guajira += subtotal
    elif destino.lower() == 'chicamocha':
        subtotal = 1600000 * personas_adultas + 960000 * personas_ninos
        total_chicamocha += subtotal
    elif destino.lower() == 'llanos':
        subtotal = 1200000 * personas_adultas + 720000 * personas_ninos
        total_llanos += subtotal
    else:
        print("Destino no válido. Por favor, ingrese un destino válido.")
        continue  # Vuelve al inicio del bucle

    # Acumular totales generales
    total_adultos += personas_adultas
    total_ninos += personas_ninos
    total_general += subtotal

    # Imprimir cotización
    print("\nCotización:")
    print(f"Nombre Cliente: {nombre_cliente}")
    print(f"Nombre del destino: {destino}")
    print(f"Nro Personas Adultas: {personas_adultas}")
    print(f"Nro Niños: {personas_ninos}")
    print(f"Subtotal: {subtotal}\n")

# Imprimir resultados finales
print("\nResultados Finales:")
print(f"Cantidad de personas que viajan para la Guajira: {total_adultos}")
print(f"Cantidad de personas que viajan para Cañón del Chicamocha: {total_ninos}")
print(f"Cantidad de personas que viajan para los llanos orientales: {total_adultos + total_ninos}")
print(f"Total de dinero de los viajes para la Guajira: {total_guajira}")
print(f"Total de dinero de los viajes para Cañón del Chicamocha: {total_chicamocha}")
print(f"Total de dinero de los viajes para los llanos orientales: {total_llanos}")
print(f"Total de personas Adultas: {total_adultos}")
print(f"Total de niños: {total_ninos}")
print(f"Total de dinero de todos los destinos: {total_general}")

