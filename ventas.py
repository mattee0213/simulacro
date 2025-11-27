from servicios import registar,inventario


ventas=[]


def registar_ventas(ventas,cliente,TipoCliente,ProductoVendido,cantidad_venta,FechaVenta,Descuento):
    nuevo_venta = {
        'cliente': cliente,
        'TipoCliente': TipoCliente,
        'ProductoVendido': ProductoVendido,
        'cantidad_ventas': cantidad_venta,
        'FechaVenta': FechaVenta,
        'Descuento': Descuento
    }
    if TipoCliente ==   '1' :
        print('regular')
        
        precio_final = PrecioUni - (PrecioUni * Descuento / 100)
        print(precio_final)

    elif TipoCliente == '0' :
        print('irregular')
        print('no tiene descuento')
    else :
        print('no existe este cliente')

    
    ventas.append(nuevo_venta)

    return ventas,TipoCliente

def validar_inventario(cantidad_venta,cantidad):
    registar(inventario,cantidad)
    for nuevo_ventas in ventas:
        if nuevo_ventas["cantidad_ventas"] == cantidad_venta:
            cantidad_venta - cantidad 
    
   