import funciones as fnc
import json

libroId = 0
usuarioId = 0
prestamoId = 0
categoriaId = 0
opcion = 0
opcionMantenedores = 0
opcionReportes = 0

        
while opcion!=3:

    print("")
    print("")
    print("      [MUNDO LIBRO]       \n")
    print("[1] - Mantenedor de Catagorias")
    print("[2] - Reportes")
    print("[3] - Salir")
    print("")

    opcion = int(input("Seleccione una opcion: \n\n"))

    if opcion == 1:

        while opcion != 5:
            print("     [MANTENEDOR CATEGORIAS]     \n")
            print("[1] - Agregar Categoria")
            print("[2] - Editar categoria")
            print("[3] - Eliminar categoria")
            print("[4] - Buscar categoria")
            print("[5] - Salir")

            opcionMantenedores = int(input("Seleccione una accion: \n\n"))

            if opcionMantenedores == 1:
                agregar = input("Ingrese el nombre para una categoria nueva: ")
                print(fnc.AgregarCategoria)
                
            elif opcionMantenedores == 2:
                print()