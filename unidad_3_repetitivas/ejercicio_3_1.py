DIA_LUNES = "1"
DIA_MARTES = "2"

turnoL1 = ""
turnoL2 = ""
turnoL3 = ""
turnoL4 = ""

turnoM1 = ""
turnoM2 = ""
turnoM3 = ""

print("\n** Ejercicio 3 — Agenda de Turnos **\n")

operador = ""
while not operador.isalpha():
    operador = input("Operador (solo letras): ").strip()

while True:
    opcion = ""
    while not opcion.isdigit():
        opcion = input(f"""
Hola {operador.capitalize()}:

1. Reservar turno 
2. Cancelar turno
3. Ver agenda del día 
4. Ver resumen general 
5. Cerrar sistema

Ingrese una opción: """).strip()

    while int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Ingrese una opción: ").strip()
        while not opcion.isdigit():
            opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        dia = ""
        while not dia.isdigit():
            dia = input("""
1- Lunes
2- Martes
3- Volver

Opción: """).strip()

        while int(dia) < 1 or int(dia) > 3:
            dia = input("Opción: ").strip()
            while not dia.isdigit():
                dia = input("Opción: ").strip()

        if dia == "3":
            continue

        paciente = ""
        while not paciente.isalpha():
            paciente = input("Paciente (solo letras): ").strip()

        paciente = paciente.lower()

        if dia == "1":
            if paciente == turnoL1 or paciente == turnoL2 or paciente == turnoL3 or paciente == turnoL4:
                print("El paciente ya tiene turno ese día")
            elif turnoL1 == "":
                turnoL1 = paciente
                print("Reserva exitosa")
            elif turnoL2 == "":
                turnoL2 = paciente
                print("Reserva exitosa")
            elif turnoL3 == "":
                turnoL3 = paciente
                print("Reserva exitosa")
            elif turnoL4 == "":
                turnoL4 = paciente
                print("Reserva exitosa")
            else:
                print("No hay turnos disponibles")

        elif dia == "2":
            if paciente == turnoM1 or paciente == turnoM2 or paciente == turnoM3:
                print("El paciente ya tiene turno ese día")
            elif turnoM1 == "":
                turnoM1 = paciente
                print("Reserva exitosa")
            elif turnoM2 == "":
                turnoM2 = paciente
                print("Reserva exitosa")
            elif turnoM3 == "":
                turnoM3 = paciente
                print("Reserva exitosa")
            else:
                print("No hay turnos disponibles")

    elif opcion == "2":
        dia = ""
        while not dia.isdigit():
            dia = input("""
1- Lunes
2- Martes
3- Volver

Opción: """).strip()

        while int(dia) < 1 or int(dia) > 3:
            dia = input("Opción: ").strip()
            while not dia.isdigit():
                dia = input("Opción: ").strip()

        if dia == "3":
            continue

        paciente = ""
        while not paciente.isalpha():
            paciente = input("Paciente: ").strip()

        paciente = paciente.lower()

        if dia == "1":
            if paciente == turnoL1:
                turnoL1 = ""
                print("Turno cancelado")
            elif paciente == turnoL2:
                turnoL2 = ""
                print("Turno cancelado")
            elif paciente == turnoL3:
                turnoL3 = ""
                print("Turno cancelado")
            elif paciente == turnoL4:
                turnoL4 = ""
                print("Turno cancelado")
            else:
                print("El paciente no tiene turno")

        elif dia == "2":
            if paciente == turnoM1:
                turnoM1 = ""
                print("Turno cancelado")
            elif paciente == turnoM2:
                turnoM2 = ""
                print("Turno cancelado")
            elif paciente == turnoM3:
                turnoM3 = ""
                print("Turno cancelado")
            else:
                print("El paciente no tiene turno")

    elif opcion == "3":
        dia = ""
        while not dia.isdigit():
            dia = input("""
1- Lunes
2- Martes
3- Volver

Opción: """).strip()

        while int(dia) < 1 or int(dia) > 3:
            dia = input("Opción: ").strip()
            while not dia.isdigit():
                dia = input("Opción: ").strip()

        if dia == "3":
            continue

        if dia == "1":
            print(f"Turno 1: {turnoL1.capitalize() if turnoL1 else '(libre)'}")
            print(f"Turno 2: {turnoL2.capitalize() if turnoL2 else '(libre)'}")
            print(f"Turno 3: {turnoL3.capitalize() if turnoL3 else '(libre)'}")
            print(f"Turno 4: {turnoL4.capitalize() if turnoL4 else '(libre)'}")

        elif dia == "2":
            print(f"Turno 1: {turnoM1.capitalize() if turnoM1 else '(libre)'}")
            print(f"Turno 2: {turnoM2.capitalize() if turnoM2 else '(libre)'}")
            print(f"Turno 3: {turnoM3.capitalize() if turnoM3 else '(libre)'}")

    elif opcion == "4":
        totalLunes = 0
        if turnoL1: totalLunes += 1
        if turnoL2: totalLunes += 1
        if turnoL3: totalLunes += 1
        if turnoL4: totalLunes += 1

        totalMartes = 0
        if turnoM1: totalMartes += 1
        if turnoM2: totalMartes += 1
        if turnoM3: totalMartes += 1

        total = totalLunes + totalMartes

        if totalLunes == totalMartes:
            diaMax = "Empate"
        elif totalLunes > totalMartes:
            diaMax = "Lunes"
        else:
            diaMax = "Martes"

        dispLunes = 4 - totalLunes
        dispMartes = 3 - totalMartes

        print(f"""
Total turnos:
Lunes: {totalLunes}
Martes: {totalMartes}
Total: {total}

Día con más turnos: {diaMax}

Disponibles:
Lunes: {dispLunes}
Martes: {dispMartes}
""")

    elif opcion == "5":
        break