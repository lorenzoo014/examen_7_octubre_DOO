
from Ejercicio1 import Apartado1,Apartado2
from Ejercicio2 import Apartado_1,Apartado_2
from Ejercicio3 import ApartadoA, ApartadoB

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Ejercicio_1 ")
        print("[2] Ejercicio_2 ")
        print("[3] Ejercicio_3 ")
        print("[4] Ejercicio_4 ")
        print("[5] Ejercicio_5 ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Apartado_1")
                # print("1er ej.-->Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.\n")
                # print("1er ej.-->Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.\n")
                # print("1er ej.-->Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.\n")
                print("[2] Apartado_2")
                print("[3] Salir del ejercicio")
                opcion2 = input("> ")
                if opcion2 == '1':
                    
                elif opcion2 == '3':
                    break
        if opcion == '6':
            print("Saliendo...")
            break
iniciar()

        #         print("Listando los clientes.../n")

        # elif opcion == '2':
        #     print("Buscando un cliente.../n")
        #     dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #     cliente = db.Clientes.buscar(dni)
        #     print(cliente) if cliente else print("Cliente no encontrado.")

        # elif opcion == '3':
        #     print("Añadiendo un cliente.../n")

        #     dni = None
        #     while True:
        #         dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #         if helpers.dni_valido(dni, db.Clientes.lista):
        #             break

        #     nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
        #     apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
        #     db.Clientes.crear(dni, nombre, apellido)
        #     print("Cliente añadido correctamente.")

        # elif opcion == '4':
        #     print("Modificando un cliente.../n")
        #     dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #     cliente = db.Clientes.buscar(dni)
        #     if cliente:
        #         nombre = helpers.leer_texto(
        #             2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
        #         apellido = helpers.leer_texto(
        #             2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
        #         db.Clientes.modificar(cliente.dni, nombre, apellido)
        #         print("Cliente modificado correctamente.")
        #     else:
        #         print("Cliente no encontrado.")

        # elif opcion == '5':
        #     print("Borrando un cliente.../n")
        #     dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #     print("Cliente borrado correctamente.") if db.Clientes.borrar(
        #         dni) else print("Cliente no encontrado.")