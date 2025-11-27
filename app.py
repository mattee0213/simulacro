from servicios import registar,consultar,actualizar,eliminar,inventario



while True:
    opcion =input('ingresa la opcion  que deseas realizar: \n 1. Registrar producto \n2.consultar \n3.actulizar \n4.eliminar \n')

    if opcion == '1':
        print("ingresa los datos que te pedimos: \n")
        NomProduct = input("Nombre del producto: ")
        marca = input("Marca del producto: ")
        categoria = input("Categoria del producto: ")
        PrecioUni = float(input("Precio unitario del producto: "))
        Cantidad = int(input("Cantidad del producto: "))
        garantia = int(input("Garantia del producto (en años): "))
        

        inventario =registar(inventario, NomProduct, marca, categoria, PrecioUni, Cantidad, garantia)

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

        print(f"el producto {marca} a sido eliminado")
    



    
       

       


