#Prueba3
import Parte2 as fn

datosClientes=[]

while True:
    print("***************************")
    print("           MENU\n")
    print('1.- Registrar pedido.')
    print('2.- Listar pedidos.')
    print('3.- Imprimir hoja de ruta.')
    print('4.- Salir.')
    print("***************************")

    while True:
        try:
            opcion=int(input("Seleccione una opcion: "))
            if opcion >= 1 and opcion <= 4:
                break
        except ValueError:
            print("Seleccione un numero valido.")

    if opcion == 1:
        fn.RegistrarPedido(datosClientes)
    elif opcion == 2:
        fn.ListarPedidos(datosClientes)
    elif opcion == 3:
        fn.ImprimirHoja(datosClientes)
    elif opcion == 4:
        break