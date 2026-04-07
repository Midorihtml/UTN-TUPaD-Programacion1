print("\n** Ejercicio 1 — Caja del Kiosco **\n")

cliente = input("Ingrese su nombre (sólo letras): ").strip().capitalize()
while not cliente.isalpha():
    cliente = input("Nombre inválido. Ingrese su nombre (sólo letras): ").strip().capitalize()

cantidadProductos = input("Ingrese la cantidad de productos a comprar: ").strip()
while not cantidadProductos.isdigit() or int(cantidadProductos) < 1:
    cantidadProductos = input("Cantidad inválida. Ingrese la cantidad de productos a comprar: ").strip()

cantidadProductos = int(cantidadProductos)

DESCUENTO = 0.1
total = 0
totalDescuento = 0
ahorro = 0

output = f"\n\nCliente: {cliente}\nCantidad de productos: {cantidadProductos}\n"

i = 0
while i < cantidadProductos:
    precio = input(f"Ingrese el precio del producto #{i+1}: ").strip()
    while not precio.isdigit() or int(precio) < 1:
        precio = input(f"Precio inválido. Ingrese el precio del producto #{i+1}: ").strip()

    precio = int(precio)

    hasDescuento = input("Producto con descuento (S/N): ").strip().upper()
    while hasDescuento != "S" and hasDescuento != "N":
        hasDescuento = input("Valor inválido. Producto con descuento (S/N): ").strip().upper()

    total += precio

    output += f"Producto {i+1} - Precio: {precio} Descuento (S/N): {'s' if hasDescuento == 'S' else 'n'}\n"

    if hasDescuento == "S":
        ahorro += precio * DESCUENTO
        precio = precio - (precio * DESCUENTO)

    totalDescuento += precio

    i += 1

promedio = totalDescuento / cantidadProductos

output += f"\nTotal sin descuentos: ${total:.2f}\nTotal con descuentos: ${totalDescuento:.2f}\nAhorro: ${ahorro:.2f}\nPromedio por producto: ${promedio:.2f}"

print(output)