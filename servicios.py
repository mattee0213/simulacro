inventario=[{'NomProduct' : "laptop", 'marca': 'asus', 'categoria': 'vibook', 'PrecioUni' : 10000, 'Cantidad': 5, 'garantia' : 2},
            {'NomProduct' : "laptop", 'marca': 'acer', 'categoria': 'gamer', 'PrecioUni' : 8000, 'Cantidad': 8, 'garantia' : 7}]



def registar(inventario, NomProduct, marca, categoria, PrecioUni, cantidad, garantia):
    nuevo_producto = {
        'NomProduct': NomProduct,
        'marca': marca,
        'categoria': categoria,
        'PrecioUni': PrecioUni,
        'Cantidad': cantidad,
        'garantia': garantia
    }
    inventario.append(nuevo_producto)

    return inventario
def consultar (inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre del producto: {producto['NomProduct']}")
            print(f"Marca: {producto['marca']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio unitario: {producto['PrecioUni']}")
            print(f"Cantidad: {producto['Cantidad']}")
            print(f"Garantía (años): {producto['garantia']}")
        return inventario
        
def actualizar(inventario, marca, nuevo_precio,nuevo_stock):
        for producto in inventario:
            if producto['marca'] == marca:
                return producto.update({'PrecioUni' : nuevo_precio,'Cantidad' : nuevo_stock})
            
def eliminar (inventario,marca):
     for productos in inventario:
          if productos['marca'] == marca:
               return inventario.remove(productos)
               
     
     
   
           