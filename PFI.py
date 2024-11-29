# ARMAMOS UN ARCHIVO DESDE CERO SEGUN LOS REQUERIMIENTOS FINALES


# ******************************************************************
# DECLARACION DE VARIABLES
# ******************************************************************
# a fines practicos (temporalmente hasta que implementemos Base de Datos) almacenamos en lista o diccionario
lista_productos = []  # esta variable lista luego se reemplazar por una tabla en SQLite
inventario = {}  # esta variable diccionario luego se reemplazar por una tabla en SQLite
# Modelo del diccionario para un producto dado
# producto = {
#     "nombre": None,
#     "descripcion": None,
#     "cantidad": 100,
#     "precio": None,
#     "categoria": None,
# }


# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************


# Funcion que muestra el menú
def mostrar_menu():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        "1. Agregar Producto \n2. Mostrar Producto \n3. Actualizar \n4. Eliminar \n5. Buscar Producto \n6. Reporte Bajo Stock \n7. Salir"
    )
    opcion = input("Ingrese la opción deseada: ")
    # Agregan un modulo de validacion para evitar errores - PENDIENTE
    # retorno un Str
    return opcion


# Función alta o registro de producto
def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    # Cuerpo de la función
    nuevo_producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria,
    }
    inventario[nombre] = (
        nuevo_producto  # Usamos el nombre como clave para facilitar la búsqueda
    )


# print("REGISTRAR PRODUCTO")
# Función que muestra los productos almacenados en nuestro inventario


def mostrar_productos():
    # Cuerpo de la función
    if lista_productos:
        for producto in lista_productos:
            print(
                f"Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Categoría: {producto['categoria']}"
            )
    else:
        print("No hay productos registrados.")


# Función que actualiza los datos de un producto especifico
def actualizar_producto():
    # Cuerpo de la función
    nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
    for producto in lista_productos:
        if producto["nombre"] == nombre_producto:
            # Actualizar los campos deseados
            producto["cantidad"] = int(input("Nueva cantidad: "))
            # ... otros campos a actualizar
            print("Producto actualizado exitosamente.")
    return print("Producto no encontrado.")

    # print("ACTUALIZAR UN PRODUCTO")


# Función que elimina un producto especifico
def eliminar_producto():
    # Cuerpo de la función
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
    for i, producto in enumerate(lista_productos):
        if producto["nombre"] == nombre_producto:
            del lista_productos[i]
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")


# print("ELIMINAR UN PRODUCTO")


# Función que busca un producto especifico
def buscar_producto():
    # Cuerpo de la función
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    for producto in lista_productos:
        if producto["nombre"] == nombre_producto:
            print(producto)
            return
    print("Producto no encontrado.")
    # print("BUSCAR UN PRODUCTO")


# Función que genera un reporte de Bajo Stock
def reporte_bajo_stock():
    # Cuerpo de la función
    # Pedir al usuario que ingrese el umbral_minimo_stock
    umbral = int(input("Ingrese el umbral mínimo de stock: "))
    for producto in lista_productos:
        if producto["cantidad"] < umbral:
            print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    # print("REPORTE DE BAJO STOCK")


def main():  # funcion o cuerpo principal del archivo Python
    while True:
        opcion = mostrar_menu()  # esta aca dentro opcion = input("Elija una opción: ")
        print(
            "Usted selcciono: ", opcion
        )  # imprime la opción seleccionada por el usuario

        if opcion == "1":
            opcion = registrar_producto()

        elif opcion == "2":
            # mostrar_productos()
            # elif opcion == "3":
            eliminar_producto()
        elif opcion == "3":
            actualizar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            buscar_producto()

        elif opcion == "6":
            reporte_bajo_stock()

        elif opcion == "7":
            print("Adios")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        continuar = input(
            "Presione 's' para terminar..."
        ).lower()  # pausa para que el usuario pueda ver
        if continuar == "s":
            break


# ******************************************************************
# INVOCAMOS A LA FUNCION PRINCIPAL
# ******************************************************************
main()  # invocar o llamar a la funcion main()
