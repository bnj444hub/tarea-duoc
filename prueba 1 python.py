entnino = 5500
entjov = 7000
entadult = 9000
totalnino = 0
totaljov = 0
total1 = 0
total2 = 0
total3 = 0
totaladult = 0
det = 1

while det == 1:
    try:
        resp = int(input("Ingrese tipo de entrada:\n1.- Niño (1 a 13 años)\n2.- Jóven (14 a 21 años)\n3.- Adulto (Mayor a 22)\nDigite: "))
        if resp == 1:
            total = entnino
            cantent = int(input(f"El precio de su entrada es de ${entnino} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantent
            totalnino += cantent
            print(f"======BOLETA======\nCategoría: Niño\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total1 += total
            print("Gracias por su compra, disfrute la función.")
        elif resp == 2:
            total = entjov
            cantent = int(input(f"El precio de su entrada es de ${entjov} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantent
            totaljov += cantent
            print(f"======BOLETA======\nCategoría: Jóven\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total2 += total
            print("Gracias por su compra, disfrute la función.")
        elif resp == 3:
            total = entadult
            cantent = int(input(f"El precio de su entrada es de ${entadult} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total *= cantent
            totaladult += cantent
            print(f"======BOLETA======\nCategoría: Adulto\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total3 += total
            print("Gracias por su compra, disfrute la función.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
            continue

        det = int(input("Desea realizar otra compra?\n1.- Si\n2.- No\nDigite: "))

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

totalent = totalnino + totaljov + totaladult
if totalent > 0:
    total_ventas = total1 + total2 + total3
    print(f"La cantidad de entradas de categoría \"Niño\" vendidas es: {totalnino} ({((totalnino * 100) // totalent)}% de las entradas totales.)")
    print(f"La cantidad de entradas de categoría \"Jóven\" vendidas es: {totaljov} ({((totaljov * 100) // totalent)}% de las entradas totales.)")
    print(f"La cantidad de entradas de categoría \"Adulto\" vendidas es: {totaladult} ({((totaladult * 100) // totalent)}% de las entradas totales.)")
    print(f"Total de ganancias del día: ${total_ventas} pesos")
    print("¡Gracias por su visita! Esperamos que disfrute de su experiencia en nuestro establecimiento.")
else:
    print("No se realizaron ventas hoy.")
