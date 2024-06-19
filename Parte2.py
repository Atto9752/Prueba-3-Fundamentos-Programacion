#Parte2

def RegistrarPedido(datosClientes):
    cantPeq=0
    cantMed=0
    cantGran=0
    #Solicitar Nombre y Apellido:
    while True:
        nombre=input('Ingrese su Nombre y Apellido: ')
        if nombre == '':
            print('Por favor ingrese un nombre.')
        else:
            break
    #Solicitar dirección:
    while True:
        direccion=input('Ingrese su dirección: ')
        if direccion == '':
            print('Por favor ingrese una dirección.')
        else:
            break
    #Solicitar sector:
    while True:
        sector=input('Ingrese su sector (Centro-Norte-Sur): ').upper()
        if sector == '':
            print('Por favor ingrese un sector')
        elif sector == 'CENTRO':
            sector='Centro'
            break
        elif sector == 'NORTE':
            sector='Norte'
            break
        elif sector == 'SUR':
            sector='Sur'
            break
        else:
            print('Por favor ingrese un sector válido.')
    #Solicitar detalle de paquetes:
    while True:
        #Solicitar tipo de paquete:
        while True:
            tipoPaquete=input('Ingrese el tipo de paquete (Pequeño-Mediano-Grande): ').upper()
            if tipoPaquete == '':
                print('Por favor ingrese el tipo de paquete.')
            elif tipoPaquete == 'PEQUEÑO':
                tipoPaquete='Pequeño'
                break
            elif tipoPaquete == 'MEDIANO':
                tipoPaquete='Mediano'
                break
            elif tipoPaquete == 'GRANDE':
                tipoPaquete='Grande'
                break
            else:
                print('Por favor, ingrese un tipo de paquete válido.')
        while True:
            try:
                while True:
                    cantPaquete=int(input('Ingrese la cantidad del paquete seleccionado: '))
                    if cantPaquete == '':
                        print('Por favor ingresa una cantidad.')
                    else:
                        if tipoPaquete == 'Pequeño':
                            cantPeq=cantPeq+cantPaquete
                            break
                        elif tipoPaquete == 'Mediano':
                            cantMed=cantMed+cantPaquete
                            break
                        elif tipoPaquete == 'Grande':
                            cantGran=cantGran+cantPaquete
                            break
                if cantPaquete != '':
                    break
            except ValueError:
                print('Por favor ingresa un número entero.')
        #Para preguntar si desea agregar más paquetes:
        while True:
            agregarMasPaq=input('¿Desea añadir más paquetes? Si/No: ').upper()
            if agregarMasPaq == '':
                print('Por favor ingresa una respuesta.')
            elif agregarMasPaq == 'SI':
                break
            elif agregarMasPaq == 'NO':
                break
            else:
                print('Por favor ingresa una respuesta válida.')

        if agregarMasPaq == 'SI':
            continue
        elif agregarMasPaq == 'NO':
            break
    
    #Añadir datos a una lista:
    datosClientes.append([f'Cliente: {nombre}'])
    datosClientes.append([f'Direccion: {direccion}'])
    datosClientes.append([f'Sector: {sector}'])
    datosClientes.append([f'Paquetes: Pequeño {cantPeq}, Mediano - {cantMed}, Grande - {cantGran}'])

def ListarPedidos(datosClientes):
    #Debe mostrar en la pantalla la lista de todos los pedidos realizados similar al ejemplo anterior de registro de pedidos.
    for i,cliente in enumerate(datosClientes):
        print(cliente)
        if i == 3 or i == (i%3 == 0):
            print('\n')

def ImprimirHoja(datosClientes):
    #- Permitir al usuario seleccionar uno de los sectores predefinidos (Centro, Norte, Sur).
    #- Generar un archivo de texto (.txt) con el detalle de los pedidos para el sector seleccionado.
    while True:
        tipoHoja=input('Seleccione la ruta que desea ver (Centro-Norte-Sur): ').upper()
        if tipoHoja == 'CENTRO':
            nombreArchivo='hoja_centro.txt'
            with open (nombreArchivo,'w') as archivo:
                for cliente in datosClientes:
                    if 'Centro' in cliente:
                        archivo.write(cliente)
            break
        elif tipoHoja == 'NORTE':
            nombreArchivo='hoja_norte.txt'
            with open (nombreArchivo,'w') as archivo:
                for cliente in datosClientes:
                    if 'Norte' in cliente:
                        archivo.write(cliente)
            break
        elif tipoHoja == 'SUR':
            nombreArchivo='hoja_sur.txt'
            with open (nombreArchivo,'w') as archivo:
                for cliente in datosClientes:
                    if 'Sur' in cliente:
                        archivo.write(cliente)
            break
        else:
            print('Ingresa un valor válido.')