

###########   Ejercicio de agencia de viajes   ###########



# Inicializar variables para acumular totales
total_guajira = 0
total_chicamocha = 0
total_llanos = 0
total_adultos = 0
total_ninos = 0
total_general = 0

# Bucle para ingresar cotizaciones
Repetir
    #Solicitar información del cliente
    Imprimir "Ingrese el nombre del cliente (o 'fin' para finalizar): "
    Leer nombre_cliente

    # Verificar si se debe finalizar el proceso
    Si nombre_cliente en minúsculas es igual a 'fin' entonces
        Salir del bucle
    Fin Si

    # Solicitar información adicional del cliente
    Imprimir "Ingrese el destino (Guajira, Chicamocha o Llanos Orientales): "
    Leer destino
    Imprimir "Ingrese el número de personas adultas: "
    Leer personas_adultas
    Imprimir "Ingrese el número de niños: "
    Leer personas_ninos

    # Calcular el subtotal según el destino
    Según destino en minúsculas Hacer
        Caso 'guajira':
            subtotal = 500 * personas_adultas + 250 * personas_ninos
            total_guajira += subtotal
        Fin Caso

        Caso 'chicamocha':
            subtotal = 700 * personas_adultas + 350 * personas_ninos
            total_chicamocha += subtotal
        Fin Caso

        Caso 'llanos':
            subtotal = 600 * personas_adultas + 300 * personas_ninos
            total_llanos += subtotal
        Fin Caso

        De Otro Modo:
            Imprimir "Destino no válido. Por favor, ingrese un destino válido."
            Continuar  // Vuelve al inicio del bucle
    Fin Según

    # Acumular totales generales
    total_adultos += personas_adultas
    total_ninos += personas_ninos
    total_general += subtotal

    # Imprimir cotización
    Imprimir "\nCotización:"
    Imprimir "Nombre Cliente:", nombre_cliente
    Imprimir "Nombre del destino:", destino
    Imprimir "Nro Personas Adultas:", personas_adultas
    Imprimir "Nro Niños:", personas_ninos
    Imprimir "Subtotal:", subtotal, "\n"

Mientras Verdadero

# Imprimir resultados finales
Imprimir "\nResultados Finales:"
Imprimir "Cantidad de personas que viajan para la Guajira:", total_adultos
Imprimir "Cantidad de personas que viajan para Cañón del Chicamocha:", total_ninos
Imprimir "Cantidad de personas que viajan para los llanos orientales:", total_adultos + total_ninos
Imprimir "Total de dinero de los viajes para la Guajira:", total_guajira
Imprimir "Total de dinero de los viajes para Cañón del Chicamocha:", total_chicamocha
Imprimir "Total de dinero de los viajes para los llanos orientales:", total_llanos
Imprimir "Total de personas Adultas:", total_adultos
Imprimir "Total de niños:", total_ninos
Imprimir "Total de dinero de todos los destinos:", total_general


#####   ejercicio de estratos para la alcaldía  #####

Inicializar variables:
total_estrato1 = 0
total_estrato2 = 0
total_sin_hijos = 0
total_hasta_2_hijos = 0
total_3_o_mas_hijos = 0
total_general = 0

Repetir:
    Imprimir "Desea ingresar Datos 1. Si 2. No"
    Leer opcion

    Si opcion no es igual a '1' entonces
        Salir del bucle

    #Solicitar información del beneficiario
    Imprimir "Ingrese el estrato (1 o 2):"
    Leer estrato
    Imprimir "Ingrese el número de hijos:"
    Leer hijos

    # Calcular el monto del bono según la tabla
    Si hijos es igual a 0 entonces
        monto_bono = 16500 si estrato es igual a 1, de lo contrario, 21500
    Sino, si hijos es menor o igual a 2 entonces
        monto_bono = 21000 si estrato es igual a 1, de lo contrario, 26000
    Sino
        monto_bono = 30000

    # Acumular totales por estrato y categoría de hijos
    Si estrato es igual a 1 entonces
        Incrementar total_estrato1 en 1
    Sino
        Incrementar total_estrato2 en 1

    Si hijos es igual a 0 entonces
        Incrementar total_sin_hijos en 1
    Sino, si hijos es menor o igual a 2 entonces
        Incrementar total_hasta_2_hijos en 1
    Sino
        Incrementar total_3_o_mas_hijos en 1

    Incrementar total_general por monto_bono

Imprimir resultados finales:
Imprimir "Cantidad de personas del estrato 1:", total_estrato1
Imprimir "Cantidad de personas del estrato 2:", total_estrato2
Imprimir "Total de dinero entregado al estrato 1:", total_estrato1 * total_general
Imprimir "Total de dinero entregado al estrato 2:", total_estrato2 * total_general
Imprimir "Cantidad de personas que no tienen hijos:", total_sin_hijos
Imprimir "Cantidad de personas que tienen hasta 2 hijos:", total_hasta_2_hijos
Imprimir "Cantidad de personas que tienen 3 o más hijos:", total_3_o_mas_hijos
Imprimir "Total de dinero entregado a los beneficiarios que no tienen hijos:", total_sin_hijos * 16500
Imprimir "Total de dinero entregado a los beneficiarios que tienen hasta 2 hijos:", total_hasta_2_hijos * 21000
Imprimir "Total de dinero entregado a los beneficiarios que tienen 3 o más hijos:", total_3_o_mas_hijos * 30000
Imprimir "Total pagado por los bonos:", total_general
