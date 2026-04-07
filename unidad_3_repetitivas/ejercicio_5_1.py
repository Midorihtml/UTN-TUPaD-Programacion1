MULTIPLICADOR_CRITICO = 1.5
salud_gladiador = 100
salud_enemigo = 100
ataque_basico = 12
ataque_pesado = 15
pociones = 3
turno_gladiador = True

print("\n** Ejercicio 5 — La Arena del Gladiador **\n")
print("--- BIENVENIDO A LA ARENA ---")

# Nombre del gladiador
nombreGladiador = input("Nombre del Gladiador: ").strip()
while not nombreGladiador.isalpha():
    print("Error: Solo letras")
    nombreGladiador = input("Nombre del Gladiador: ").strip()

nombreGladiador = nombreGladiador.capitalize()

print(f"\nGladiador: {nombreGladiador}")
print("\n=== INICIO DEL COMBATE ===")

# Loop principal
while salud_enemigo > 0 and salud_gladiador > 0:

    # Turno enemigo
    if not turno_gladiador:
        salud_gladiador -= ataque_basico
        print(f"¡El enemigo te atacó por {ataque_basico} de daño!")

        if salud_gladiador <= 0:
            break

        turno_gladiador = True
        print("=== NUEVO TURNO ===")

    # Estado
    print(f"{nombreGladiador} (HP {salud_gladiador}) vs Enemigo (HP {salud_enemigo}) | Pociones: {pociones}")

    # Menú validado
    opcion = ""
    while not opcion.isdigit():
        opcion = input("""
Elige una acción:

1. Ataque Pesado
2. Ráfaga Veloz
3. Curar

Opción: """).strip()

    # Validar rango
    while int(opcion) < 1 or int(opcion) > 3:
        print("Error: Opción fuera de rango")
        opcion = input("Opción: ").strip()
        while not opcion.isdigit():
            opcion = input("Opción: ").strip()

    if opcion == "1":
        damage = ataque_pesado
        if salud_enemigo < 20:
            damage = ataque_pesado * MULTIPLICADOR_CRITICO
            print("¡Golpe crítico!")

        salud_enemigo -= damage
        print(f"¡Atacaste por {damage} de daño!")
        turno_gladiador = False

    elif opcion == "2":
        print("¡Ráfaga de golpes!")
        for i in range(3):
            salud_enemigo -= 5
            print("Golpe por 5 de daño")

        turno_gladiador = False

    elif opcion == "3":
        if pociones > 0:
            salud_gladiador += 30
            if salud_gladiador > 100:
                salud_gladiador = 100

            pociones -= 1
            print("Salud restaurada +30")
        else:
            print("¡No quedan pociones!")

        turno_gladiador = False

if salud_enemigo <= 0:
    print("\n🏆 VICTORIA")
elif salud_gladiador <= 0:
    print("\n💀 DERROTA")