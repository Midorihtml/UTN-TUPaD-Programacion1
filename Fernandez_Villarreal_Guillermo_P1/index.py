herramientas = [];
existencias  = [];
carga_inicial_completadas = [False,False];

alerta_herramientas = """* Carga inicial de Herramientas sin completar""";

alerta_existencias = """* Carga inicial de Existencias sin completar""";

menu = f"""
*** Sistema de Control de Inventario 🛠️ ***
-------------------------------------------

1- Carga Inicial de Herramientas
2- Carga de Existencias
3- Visualización de Inventario
4- Consulta de Stock (existencias)
5- Reporte de Agotados
6- Alta de Nuevo Producto
7- Actualización de Stock (Venta/Ingreso)
8- Salir

Ingrese una opción (sólo números): """;

while True:

    if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
        print("""
===================              
Tareas pendinentes
===================              
""");
        if not carga_inicial_completadas[0]:
            print(alerta_herramientas);
        
        if not carga_inicial_completadas[1]:
            print(alerta_existencias);

    opcion = input(menu);

    match opcion:
        case o if not o.isdigit():
            print('\nOpción inválida. Sólo números');
        case "1":
            if carga_inicial_completadas[0]:
                print('\n❗ Carga inicial completada. Para añadir un producto utilice la opción 6');
                continue;
            
            cantidad_herramientas = input('\nIngrese la cantidad de herramientas que se pondrán a la venta (sólo números enteros positivos): ');
            
            while not cantidad_herramientas.isdigit() or int(cantidad_herramientas) <= 0:
                cantidad_herramientas = input('\nIngrese la cantidad de herramientas que se pondrán a la venta (sólo números enteros positivos): ');

            print(f'\nCargando {cantidad_herramientas} herramientas');

            for i in range(int(cantidad_herramientas)):
                herramienta1 = input(f'\nIngrese el nombre de la herramienta {i+1} (sólo letras): ');
                while not herramienta1.isalpha():
                    herramienta1 = input(f'\nIngrese el nombre de la herramienta {i+1} (sólo letras): ');
        
                herramientas.append(herramienta1.upper().strip());
            
            if int(cantidad_herramientas) != len(herramientas):
                print('\n❌ Error al cargar las herramientas. Intente nuevamente más tarde.');
            else:
                print(f'\n✅ Se cargaron {len(herramientas)} herramienta/s correctamente');
                carga_inicial_completadas[0] = True;
        
        case "2":
            if not carga_inicial_completadas[0] or not len(herramientas):
                print('\n❌ Primero cargue las herramientas que estarán a la venta');
                continue;
            
            if carga_inicial_completadas[1]:
                print('\n❗ Carga inicial completada. Para actualizar las existencias utilice la opción 7');
                continue;
            
            for i in range(len(herramientas)):
                existencia = input(f'\nIngrese las existencias para: {herramientas[i]} (sólo números enteros positivos): ');
                
                while not existencia.isdigit() or int(existencia) < 0:
                    existencia = input(f'\nIngrese las existencias para: {herramientas[i]} (sólo números enteros positivos): ');
                
                existencias.append(int(existencia));
            if len(existencias) != len(herramientas):
                print('\n❌ Error al cargar existencias. Intente nuevamente más tarde.');
                continue;
            
            print(f'\n✅ Existencias cargadas correctamente');
            carga_inicial_completadas[1] = True;
        
        case "3":
            if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
                print('\n❗ No se encontraron herramientas y/o existencias cargadas');
                print('\n❗ Realize primero la carga incial para continuar');
                continue;
            print("""
Visualizando inventario:

EXISTENCIAS | HERRAMIENTA
""");
            for i in range(len(herramientas)):
                print(f'{0 if 0 == len(existencias) or len(existencias) < i else existencias[i]} | {herramientas[i]}');
        
        case "4":
            if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
                print('\n❗ No se encontraron herramientas y/o existencias cargadas');
                print('\n❗ Realize primero la carga incial para continuar');
                continue;
            
            herramienta2 = input('\nIngrese el nombre de la herramienta (sólo letras): ');
            while not herramienta2.isalpha():
                herramienta2 = input('\nIngrese el nombre de la herramienta (sólo letras): ');

            herramienta2 = herramienta2.upper();

            if not herramienta2 in herramientas:
                print(f'\n❗ {herramienta2} no encontrada.');
                continue;

            index_herramienta = herramientas.index(herramienta2); 
            print(f"""
EXISTENCIAS | HERRAMIENTA
-------------------------
{0 if 0 == len(existencias) or len(existencias) < index_herramienta else existencias[index_herramienta]} | {herramientas[index_herramienta]}                  
""");
        
        case "5":
            if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
                print('\n❗ No se encontraron herramientas y/o existencias cargadas');
                print('\n❗ Realize primero la carga incial para continuar');
                continue;
            
            herramientas_agotadas = [];
            for i in range(len(herramientas)):
                if not existencias[i]:
                    herramientas_agotadas.append(herramientas[i]);
        
            if not len(herramientas_agotadas):
                print('\n✅ No se encontraron herramientas agotadas');
                continue;
            
            print('\nHerramientas agotadas:');
            for herramienta_agotada in herramientas_agotadas:
                print(herramienta_agotada);
        
        case "6":
            if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
                print('\n❗ No se encontraron herramientas y/o existencias cargadas');
                print('\n❗ Realize primero la carga incial para continuar');
                continue;
            
            herramienta3 = input('\nIngrese el nombre de la herramineta: ').upper();
            while not herramienta3.isalpha() or herramienta3 in herramientas:
                if herramienta3 in herramientas:
                    print(f'\nHerramienta {herramienta3} duplicada');
                    continue;
                herramienta3 = input('\nIngrese el nombre de la herramineta (sólo letras): ').upper();
            
            herramientas.append(herramienta3);

            existencia = input(f'\nIngrese las existencias para {herramienta3}: ');
            while not existencia.isdigit() or int(existencia) < 0:
                existencia = input(f'\nIngrese las existencias para {herramienta3} (sólo números enteros positivos): ');

            existencias.append(int(existencia));

            print('\n✅ Herramienta y existencia cargadas correctamente');

        case "7":
            if not carga_inicial_completadas[0] or not carga_inicial_completadas[1]:
                print('\n❗ No se encontraron herramientas y/o existencias cargadas');
                print('\n❗ Realize primero la carga incial para continuar');
                continue;

            herramienta4 = input('\nIngrese el nombre de la herramienta a actualizar stock (sólo letras): ').upper();
            while not herramienta4.isalpha() or herramienta4 not in herramientas:
                if herramienta4 not in herramientas:
                    print(f'\nHerramienta {herramienta4} no encontrada.');
                
                herramienta4 = input('\nIngrese el nombre de la herramienta a actualizar stock (sólo letras): ').upper();

            op = input(F"""
Actualización de Stock (Venta/Ingreso)
--------------------------------------
                       
EXISTENCIAS | HERRAMIENTA
{existencias[herramientas.index(herramienta4)]} | {herramienta4}
                                  
1- venta
2- Ingreso

Ingrese una opción (sólo números): """);

            match op:
                case op1 if not op1.isdigit():
                    print('\nOpción inválida. Sólo números');
                case '1':
                    if not existencias[herramientas.index(herramienta4)]:
                        print(f'\nHerramienta {herramienta4} sin existencias disponibles');
                        continue;
                    
                    cantidad_venta = input(f'\nIngrese la cantidad de {herramienta4} vendida/s (sólo números enteros positivos): ');
                    while not cantidad_venta.isdigit() or 0 >= int(cantidad_venta) or int(cantidad_venta) > existencias[herramientas.index(herramienta4)]:
                        cantidad_venta = input(f'\nIngrese la cantidad de {herramienta4} vendida (sólo números enteros positivos): ');

                        if cantidad_venta.isdigit() and int(cantidad_venta) > existencias[herramientas.index(herramienta4)]:
                            print(f'\n❗ Existencias ({existencias[herramientas.index(herramienta4)]}) insuficientes para concretar la venta');
                            continue;
                    
                    existencias[herramientas.index(herramienta4)] -= int(cantidad_venta);
                    print(f'\n✅ Se vendieron {cantidad_venta} {herramienta4} correctamente');
                
                case '2':
                    cantidad_reposicion = input(f'\nIngrese la cantidad de {herramienta4} a reponer (sólo números enteros positivos): ');
                    while not cantidad_reposicion.isdigit() or int(cantidad_reposicion) <= 0:
                        cantidad_reposicion = input(f'\nIngrese la cantidad de {herramienta4} a reponer (sólo números enteros positivos): ');

                    existencias[herramientas.index(herramienta4)] += int(cantidad_reposicion);
                    print(f"""
✅ Se actualizó el stock de {herramienta4} correctamente
EXISTENCIAS | HERRAMIENTA
{existencias[herramientas.index(herramienta4)]} | {herramienta4}
""");
                case _:
                    print('\nOpción fuera de rango (1-2)');
        
        case "8":
            print('Bye Bye 👋');
            break;
        case _:
            print('\nOpción fuera de rango (1-8)');
