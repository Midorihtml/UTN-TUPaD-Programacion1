USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"
INTENTOS_MAXIMOS = 3

print("\n** Ejercicio 2 — Acceso al Campus **\n")

intentos = 0
acceso = False

while intentos < INTENTOS_MAXIMOS:
    intentos += 1
    print(f"Intento {intentos}/{INTENTOS_MAXIMOS}")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        print("\nAcceso concedido")
        acceso = True
        break

    print("\nError: credenciales inválidas")

if not acceso:
    print("\nCuenta bloqueada")
else:
    while True:
        opcion = ""
        while not opcion.isdigit():
            opcion = input("""

1. Ver estado de inscripción
2. Cambiar clave
3. Mostrar mensaje motivacional
4. Salir

Elije una opción: """).strip()

        while int(opcion) < 1 or int(opcion) > 4:
            opcion = input("Elije una opción: ").strip()
            while not opcion.isdigit():
                opcion = input("Elije una opción: ").strip()

        if opcion == "1":
            print("Inscripto")

        elif opcion == "2":
            nuevaClave = input("Nueva clave: ")
            confirmacion = input("Confirmar clave: ")

            while len(nuevaClave) < 6:
                print("Error: mínimo 6 caracteres")
                nuevaClave = input("Nueva clave: ")
                confirmacion = input("Confirmar clave: ")

            if nuevaClave != confirmacion:
                print("Las claves no coinciden")
            else:
                CLAVE_CORRECTA = nuevaClave
                print("\nClave actualizada correctamente")
                print("\nInicio de sesión requerido\n")

                intentos = 0
                acceso = False

                while intentos < INTENTOS_MAXIMOS:
                    intentos += 1
                    print(f"Intento {intentos}/{INTENTOS_MAXIMOS}")

                    usuario = input("Usuario: ")
                    clave = input("Clave: ")

                    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
                        print("\nAcceso concedido")
                        acceso = True
                        break

                    print("\nError: credenciales inválidas")

                if not acceso:
                    print("\nCuenta bloqueada")
                    break

        elif opcion == "3":
            print("No necesitas todo para empezar. Lo importante es comenzar.")

        elif opcion == "4":
            break