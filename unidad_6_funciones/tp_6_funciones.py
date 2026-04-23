import math

def input_alpha(placeholder = ""):
    value = input(placeholder).strip()
    while not value.isalpha():
        value = input(f"Valor inválido. {placeholder}").strip()
    return value

def input_digit(placeholder = ""):
    value = input(placeholder).strip()
    while not value.isdigit() or int(value) < 1:
        value = input(f"Valor inválido. {placeholder}").strip()
    return int(value)

def input_float(placeholder = ""):
    value = input(placeholder).strip()
    while not value.isdigit() or int(value) < 1:
        value = input(f"Valor inválido. {placeholder}").strip()
    return int(value)

# Ejercicio 1: 
def imprimir_hola_mundo():
    print("¡Hola Mundo!")

# Ejercicio 2: 
def saludar_usuario(nombre):
    print(f"¡Hola {nombre.capitalize()}!")

# Ejercicio 3: 
def solicitar_datos_usuario():
    nombre = input_alpha("Ingrese su nombre: ")
    apellido = input_alpha("Ingrese su apellido: ")
    edad = input_digit("Ingrese su edad: ")
    residencia = input_alpha("Ingrese su lugar de residencia: ")
    return [nombre, apellido, edad, residencia]

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}.")

# Ejercicio 4
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area:.2f}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")

# Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(0, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma,resta,multiplicacion,division)

def print_operaciones(tupla_operaciones):
    print(f"Suma: {tupla_operaciones[0]}")
    print(f"Resta: {tupla_operaciones[1]}")
    print(f"Multiplicación: {tupla_operaciones[2]}")
    print(f"División: {tupla_operaciones[3]}")

# Ejercicio 8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    print(f"El IMC para un peso de {peso} kg y una altura de {altura} m es: {imc:.2f}")

def celsius_a_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")

def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

while True:
    option = input_digit("""
TP 6 Funciones:
-------------------------------------------------------
1-  Ejercicio 1 Imprimir "Hola Mundo"
2-  Ejercicio 2 Saludar usuario
3-  Ejercicio 3 Información personal
4-  Ejercicio 4 Calcular área y perímetro de un círculo
5-  Ejercicio 5 Convertir segundos a horas
6-  Ejercicio 6 Mostrar tabla de multiplicar
7-  Ejercicio 7 Operaciones básicas
8-  Ejercicio 8 Calcular IMC
9-  Ejercicio 9 Convertir Celsius a Fahrenheit
10- Ejercicio 10 Calcular promedio
                         
Seleccione un ejercicio (1-10) o 0 para salir: """)

    match option:
        case 0:
            print("Bye Bye 👋...")
            break
        case 1:
            imprimir_hola_mundo()
        case 2:
            nombre_usuario = input_alpha("Ingrese su nombre: ")
            saludar_usuario(nombre_usuario)
        case 3:
            informacion_personal(*solicitar_datos_usuario())
        case 4:
            radio = input_digit("Ingrese el radio del círculo: ")
            calcular_area_circulo(radio)
            calcular_perimetro_circulo(radio)
        case 5:
            segundos = input_digit("Ingrese la cantidad de segundos: ")
            segundos_a_horas(segundos)
        case 6:
            numero = input_digit("Ingrese un número para mostrar su tabla de multiplicar: ")
            tabla_multiplicar(numero)
        case 7:
            a = input_digit("Ingrese el primer número: ")
            b = input_digit("Ingrese el segundo número: ")
            print_operaciones(operaciones_basicas(a,b))
        case 8:
            peso = input_digit("Ingrese su peso en kg: ")
            altura = input_digit("Ingrese su altura en metros: ")
            calcular_imc(peso, altura)
        case 9:
            temp_celsius = input_digit("Ingrese la temperatura en grados Celsius: ")
            celsius_a_fahrenheit(temp_celsius)
        case 10:
            a = input_digit("Ingrese el primer número: ")
            b = input_digit("Ingrese el segundo número: ")
            c = input_digit("Ingrese el tercer número: ")
            calcular_promedio(a, b, c)
        case _:
            print("Opción fuera de rango. Intente nuevamente (0-10).")