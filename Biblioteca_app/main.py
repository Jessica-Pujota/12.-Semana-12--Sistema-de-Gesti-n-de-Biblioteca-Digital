from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    print("\n--- SISTEMA DE BIBLIOTECA DIGITAL ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros por título")
    print("8. Buscar libros por autor")
    print("9. Buscar libros por categoría")
    print("10. Listar libros prestados a un usuario")
    print("11. Listar libros disponibles")
    print("12. Listar usuarios registrados")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    servicio = BibliotecaServicio()

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            print("\n--- AÑADIR LIBRO ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            if servicio.agregar_libro(libro):
                print("Libro añadido correctamente.")
            else:
                print("Error: Ya existe un libro con ese ISBN.")
        elif opcion == "2":
            print("\n--- QUITAR LIBRO ---")
            isbn = input("ISBN del libro a quitar: ")
            if servicio.quitar_libro(isbn):
                print("Libro eliminado (si estaba disponible).")
            else:
                print("Error: El libro no existe o está prestado.")
        elif opcion == "3":
            print("\n--- REGISTRAR USUARIO ---")
            nombre = input("Nombre: ")
            id_usuario = input("ID de usuario: ")
            usuario = Usuario(nombre, id_usuario)
            if servicio.registrar_usuario(usuario):
                print("Usuario registrado.")
            else:
                print("Error: ID de usuario ya existe.")
        elif opcion == "4":
            print("\n--- DAR DE BAJA USUARIO ---")
            id_usuario = input("ID de usuario: ")
            if servicio.dar_baja_usuario(id_usuario):
                print("Usuario dado de baja.")
            else:
                print("Error: Usuario no existe o tiene libros prestados.")

        elif opcion == "5":
            print("\n--- PRESTAR LIBRO ---")
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            if servicio.prestar_libro(isbn, id_usuario):
                print("Préstamo realizado.")
            else:
                print("Error: Libro no disponible o usuario no registrado.")

        elif opcion == "6":
            print("\n--- DEVOLVER LIBRO ---")
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            if servicio.devolver_libro(isbn, id_usuario):
                print("Devolución exitosa.")
            else:
                print("Error: No se pudo devolver (verifique usuario y libro).")

        elif opcion == "7":
            print("\n--- BUSCAR POR TÍTULO ---")
            titulo = input("Título (o parte): ")
            resultados = servicio.buscar_por_titulo(titulo)
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(f"  - {libro}")
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            print("\n--- BUSCAR POR AUTOR ---")
            autor = input("Autor (o parte): ")
            resultados = servicio.buscar_por_autor(autor)
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(f"  - {libro}")
            else:
                print("No se encontraron libros.")

        elif opcion == "9":
            print("\n--- BUSCAR POR CATEGORÍA ---")
            categoria = input("Categoría (o parte): ")
            resultados = servicio.buscar_por_categoria(categoria)
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(f"  - {libro}")
            else:
                print("No se encontraron libros.")

        elif opcion == "10":
            print("\n--- LISTAR PRÉSTAMOS DE USUARIO ---")
            id_usuario = input("ID del usuario: ")
            prestamos = servicio.listar_prestamos_usuario(id_usuario)
            if prestamos is None:
                print("Usuario no encontrado.")
            elif prestamos:
                print(f"Libros prestados a {id_usuario}:")
                for libro in prestamos:
                    print(f"  - {libro}")
            else:
                print("El usuario no tiene libros prestados.")

        elif opcion == "11":
            print("\n--- LIBROS DISPONIBLES ---")
            disponibles = servicio.listar_libros_disponibles()
            if disponibles:
                for libro in disponibles:
                    print(f"  - {libro}")
            else:
                print("No hay libros disponibles.")

        elif opcion == "12":
            print("\n--- USUARIOS REGISTRADOS ---")
            usuarios = servicio.listar_usuarios()
            if usuarios:
                for usuario in usuarios:
                    print(f"  - {usuario}")
            else:
                print("No hay usuarios registrados.")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()