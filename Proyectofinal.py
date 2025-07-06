
print("¡Hola! Soy ChatPablo, tu asistente de inventarios.")
print("Escribe 'ayuda' para ver los comandos disponibles\n")

inventario = {}
comandos = ["agregar", "eliminar", "buscar", "mostrar", "total", "verificar", "salir"]

while True:
    accion = input("\n¿Qué deseas hacer? ").lower()
    
    # Comando: Ayuda
    if accion == "ayuda":
        print("\nComandos disponibles:")
        for cmd in comandos:
            print(f"- {cmd}")
    
    # Comando: Agregar producto
    elif accion == "agregar":
        nombre = input("Nombre del producto: ").title()
        
        if any(nombre == prod for prod in inventario):
            print(f"¡{nombre} ya existe! Usa 'eliminar' para modificarlo")
            continue
            
        try:
            cantidad = int(input("Cantidad a agregar: "))
            if cantidad <= 0:
                print("¡Error! La cantidad debe ser positiva")
            else:
                inventario[nombre] = cantidad
                print(f"✔️ {cantidad} unidades de {nombre} agregadas")
        except:
            print("¡Debes ingresar un número válido!")
    
    # Comando: Eliminar producto
    elif accion == "eliminar":
        nombre = input("Nombre del producto: ").title()
        
        if all(nombre != prod for prod in inventario):
            print(f"¡{nombre} no existe en el inventario!")
            continue
            
        try:
            cantidad = int(input("Cantidad a eliminar: "))
            if cantidad <= 0:
                print("¡Error! La cantidad debe ser positiva")
            elif cantidad > inventario[nombre]:
                print("¡No hay suficiente stock!")
            else:
                inventario[nombre] -= cantidad
                print(f" {cantidad} unidades de {nombre} eliminadas")
                
                if inventario[nombre] == 0:
                    del inventario[nombre]
                    print(f" {nombre} eliminado del inventario (stock 0)")
        except:
            print("¡Debes ingresar un número válido!")
    
    # Comando: Buscar producto
    elif accion == "buscar":
        nombre = input("Nombre del producto: ").title()
        
        for producto, stock in inventario.items():
            if producto == nombre:
                print(f"Stock de {producto}: {stock} unidades")
                break
        else:
            print("Producto no encontrado")
    
    # Comando: Mostrar inventario
    elif accion == "mostrar":
        if not inventario:
            print("¡El inventario está vacío!")
        else:
            print("\nInventario completo:")
            for i, (producto, stock) in enumerate(inventario.items(), 1):
                print(f"{i}. {producto}: {stock} unidades")
    
    # Comando: Total stock
    elif accion == "total":
        total = sum(inventario.values())
        print(f"Total de productos en stock: {total} unidades")
    
    # Comando: Verificar stock
    elif accion == "verificar":
        if not inventario:
            print("Inventario vacío - nada que verificar")
        else:
            bajos = [p for p, s in inventario.items() if s < 10]
            if any(inventario.values()):
                print("✓ Todos los productos tienen stock positivo")
            if bajos:
                print("¡Atención! Stock bajo en:")
                for producto in bajos:
                    print(f"- {producto} ({inventario[producto]} unidades)")
    
    # Comando: Salir
    elif accion == "salir":
        print("¡Gracias por usar ChatStock! Hasta pronto.")
        break
    
    # Comando no reconocido
    else:
        print("Comando no válido. Escribe 'ayuda' para ver opciones")