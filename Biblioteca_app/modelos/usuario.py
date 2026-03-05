class Usuario: #Representa un usuario de la biblioteca.
    
    def __init__(self, nombre: str, id_usuario: str): #Inicializa un nuevo usuario con su nombre, ID y una lista vacía de libros prestados.
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados = []  # lista de objetos Libro

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def id_usuario(self) -> str:
        return self._id_usuario

    @property
    def libros_prestados(self): #Devuelve una copia de la lista para evitar modificaciones externas.
        return self._libros_prestados.copy()

    def tomar_prestado(self, libro): #Agrega un libro a la lista de préstamos (uso interno desde el servicio).
        self._libros_prestados.append(libro)

    def devolver_libro(self, libro): #Elimina un libro de la lista de préstamos.
        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)
        else:
            raise ValueError("El libro no está en préstamo de este usuario")

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Préstamos: {len(self._libros_prestados)}"