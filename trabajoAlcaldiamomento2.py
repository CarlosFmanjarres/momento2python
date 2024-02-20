# Inicializar variables para acumular totales
total_estrato1 = 0
total_estrato2 = 0
total_sin_hijos = 0
total_hasta_2_hijos = 0
total_3_o_mas_hijos = 0
total_general = 0

# Bucle para ingresar datos
while True:
    print("\nDesea ingresar Datos")
    opcion = input("1. Si  2. No: ")

    # Verificar si se debe finalizar el proceso
    if opcion != '1':
        break

    # Solicitar información del beneficiario
    estrato = int(input("Ingrese el estrato (1 o 2): "))
    hijos = int(input("Ingrese el número de hijos: "))

    # Calcular el monto del bono según la tabla
    if hijos == 0:
        monto_bono = 16500 if estrato == 1 else 21500
    elif hijos <= 2:
        monto_bono = 21000 if estrato == 1 else 26000
    else:
        monto_bono = 30000

    # Acumular totales por estrato y categoría de hijos
    if estrato == 1:
        total_estrato1 += 1
    else:
        total_estrato2 += 1

    if hijos == 0:
        total_sin_hijos += 1
    elif hijos <= 2:
        total_hasta_2_hijos += 1
    else:
        total_3_o_mas_hijos += 1

    total_general += monto_bono

# Imprimir resultados finales
print("\nResultados Finales:")
print(f"Cantidad de personas del estrato 1: {total_estrato1}")
print(f"Cantidad de personas del estrato 2: {total_estrato2}")
print(f"Total de dinero entregado al estrato 1: {total_estrato1 * total_general}")
print(f"Total de dinero entregado al estrato 2: {total_estrato2 * total_general}")
print(f"Cantidad de personas que no tienen hijos: {total_sin_hijos}")
print(f"Cantidad de personas que tienen hasta 2 hijos: {total_hasta_2_hijos}")
print(f"Cantidad de personas que tienen 3 o más hijos: {total_3_o_mas_hijos}")
print(f"Total de dinero entregado a los beneficiarios que no tienen hijos: {total_sin_hijos * 16500}")
print(f"Total de dinero entregado a los beneficiarios que tienen hasta 2 hijos: {total_hasta_2_hijos * 21000}")
print(f"Total de dinero entregado a los beneficiarios que tienen 3 o más hijos: {total_3_o_mas_hijos * 30000}")
print(f"Total pagado por los bonos: {total_general}")


