from servicios import registar,consultar,actualizar,eliminar,inventario
from ventas import registar_ventas,ventas




while True:
    opcion =input('ingresa la opcion  que deseas realizar: \n 1. Registrar producto \n2.consultar \n3.actulizar \n4.eliminar  \n 5.registar ventas \n 6.eliminar \n')

    if opcion == '1':
        print("ingresa los datos que te pedimos: \n")
        NomProduct = input("Nombre del producto: ")
        marca = input("Marca del producto: ")
        categoria = input("Categoria del producto: ")
        PrecioUni = float(input("Precio unitario del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        garantia = int(input("Garantia del producto (en años): "))
        

        inventario =registar(inventario, NomProduct, marca, categoria, PrecioUni, cantidad, garantia)

        print("\nProducto registrado exitosamente!\n")

    elif opcion == '2':

        print(consultar(inventario))
    
    elif opcion == '3' :
        marca=input('ingresa el nombre del producto que quieres actualizar: ')
       

        nuevo_precio=input('ingresa el nuevo precio del producto: ')
        nuevo_stok=input('ingresa la nueva cantidad que abra en el stok: ')

        actualizar(inventario, marca, nuevo_precio, nuevo_stok)

        print(inventario)

    elif opcion == '4':

        marca=input('ingresa la marca que deseas eliminar: ')

        eliminar(inventario,marca)


    elif opcion == '5' :
        print("ingresa los datos que te pedimos: \n")
        cliente = input("Nombre del cliente: ")
        TipoCliente = input("que tipo de cliente es: (1.'frecuente' 0.('regular')) ")
        ProductoVendido = input("nombre del producto vendido: ")
       

        cantidad_venta = float(input("ingresa las unidades vendidas : "))
        FechaVenta = int(input("fecha de venta: "))
        Descuento = float(input("aplica el descuento: "))
        for producto in inventario:
            if ProductoVendido == producto['marca']:
                print('funcioan')

        registar_ventas(ventas,cliente,TipoCliente,ProductoVendido,cantidad_venta,FechaVenta,Descuento)
        print('tu venta a sido registrada')
        print(ventas)
         





    
       

       


