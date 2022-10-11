
# from Ejercicio1 import Apartado1,Apartado2,main
import sys
sys.path.insert(0,"C:/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_7_octubre_DOO/Ejercicio1")
sys.path.insert(0,"C:/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_7_octubre_DOO/Ejercicio2")
sys.path.insert(0,"C:/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_7_octubre_DOO/Ejercicio3")
sys.path.insert(0,"C:/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_7_octubre_DOO/Ejercicio4")
from Ejercicio2 import main2
from Ejercicio1 import main
from Ejercicio3 import main3
# from Ejercicio3 import ApartadoA, ApartadoB,main3

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Ejercicio_1 ")
        print("[2] Ejercicio_2 ")
        print("[3] Ejercicio_3 ")
        print("[4] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Apartado_1")
                print("[2] Apartado_2")
                print("[3] Salir del ejercicio")
                opcion2 = input("> ")
                if opcion2 == '1':
                    main2.primer_apartado()
                elif opcion == '2':
                    main2.segundo_apartado()
                elif opcion2 == '3':
                    print()
                    break
        if opcion == '2':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Apartado_1")
                print("[2] Apartado_2")
                print("[3] Salir del ejercicio")
                opcion3 = input("> ")
                if opcion3 == '1':
                    main.primer_apartado()
                elif opcion3 == '2':
                    main.segundo_apartado()
                elif opcion3 == '3':
                    print()
                    break
        if opcion == '3':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Apartado_1")
                print("[2] Apartado_2")
                print("[3] Salir del ejercicio")
                opcion4 = input("> ")
                if opcion4 == '1':
                    main3.primer_apartado()
                elif opcion4 == '2':
                    main3.segundo_apartado()
                elif opcion4 == '3':
                    print()
                    break
        if opcion == '4':
            print("Saliendo...")
            break
iniciar()