energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

cerraduras_forzadas = 0
MAX_CERRADURAS_FORZADAS = 3
MIN_CERRADURAS_ABIERTAS = 3
ENERGIA_BAJA = 40
STEPS_HACKEO_PANEL = 4

print("\n** Ejercicio 4 — La Bóveda **\n")

nombre_agente = ""
while not nombre_agente.isalpha():
    nombre_agente = input("Agente (solo letras): ").strip()

while True:

    estado_alarma = "ACTIVADA 🚨" if alarma else "DESACTIVADA"

    print(f"""
Bienvenido agente {nombre_agente.capitalize()}

Puertas abiertas: {cerraduras_abiertas}
Racha cerraduras forzadas: {cerraduras_forzadas}/{MAX_CERRADURAS_FORZADAS}
Energía: {energia} | Tiempo: {tiempo}
Alarma: {estado_alarma}

1. Forzar cerradura
2. Hackear panel
3. Descansar
4. Abandonar partida
""")

    opcion = ""
    while not opcion.isdigit():
        opcion = input("Ingrese una opción: ").strip()

    while int(opcion) < 1 or int(opcion) > 4:
        print("Opción fuera de rango")
        opcion = input("Ingrese una opción: ").strip()
        while not opcion.isdigit():
            opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        if energia - 20 < 0:
            print("Energía insuficiente")
        elif tiempo - 2 < 0:
            print("Tiempo insuficiente")
        else:
            energia -= 20
            tiempo -= 2

            if energia <= 0 or tiempo <= 0:
                print("\n💀 DERROTA")
                break

            if energia < ENERGIA_BAJA:
                print("Hay riesgo de alarma 🚨")

                numero = ""
                while not numero.isdigit():
                    numero = input("Ingresa un número (1-3): ").strip()

                while int(numero) < 1 or int(numero) > 3:
                    print("Número fuera de rango")
                    numero = input("Ingresa un número (1-3): ").strip()
                    while not numero.isdigit():
                        numero = input("Ingresa un número (1-3): ").strip()

                if int(numero) == 3:
                    alarma = True
                    print("Alarma activada 🚨🚨")
                    print("Puerta bloqueada 🔒")
                    print("No lograste abrir la cerradura")
                    continue

            cerraduras_forzadas += 1

            if not alarma:
                if cerraduras_forzadas >= MAX_CERRADURAS_FORZADAS:
                    alarma = True
                    print("Alarma activada 🚨🚨")
                    print("No lograste abrir la cerradura")
                else:
                    cerraduras_abiertas += 1
                    print("Puerta abierta 🔓")
            else:
                print("No lograste abrir la cerradura")

    elif opcion == "2":
        if energia - 10 < 0:
            print("Energía insuficiente")
        elif tiempo - 3 < 0:
            print("Tiempo insuficiente")
        else:
            energia -= 10
            tiempo -= 3

            if energia <= 0 or tiempo <= 0:
                print("\n💀 DERROTA")
                break

            cerraduras_forzadas = 0

            codigo = "AAB!"

            for step in range(STEPS_HACKEO_PANEL):
                print(f"Hackeando ... paso {step+1}/{STEPS_HACKEO_PANEL}")
                codigo_parcial += codigo[step:step+1]

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < MIN_CERRADURAS_ABIERTAS:
                cerraduras_abiertas += 1
                print("Puerta abierta 🔓")
            else:
                print("Hackeo fallido")

    elif opcion == "3":
        if tiempo - 1 < 0:
            print("Tiempo insuficiente")
        else:
            energia += 15
            tiempo -= 1
            cerraduras_forzadas = 0

            if energia > 100:
                energia = 100

            if alarma:
                energia -= 10

            if energia <= 0 or tiempo <= 0:
                print("\n💀 DERROTA")
                break

            print(f"Energía restaurada: {energia}")

    elif opcion == "4":
        print("Abandonaste la misión")
        break

    if cerraduras_abiertas == MIN_CERRADURAS_ABIERTAS:
        print("\n🏆 VICTORIA")
        break

    if energia <= 0 or tiempo <= 0 or (alarma and tiempo <= 3 and cerraduras_abiertas < MIN_CERRADURAS_ABIERTAS):
        print("\n💀 DERROTA")
        break