
from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio: #Lógica de negocio de la biblioteca.
    def __init__(self): # Diccionario de libros disponibles: ISBN -> Libro
        self._libros_disponibles = {} # Diccionario de usuarios registrados: ID -> Usuario
        self._usuarios = {}  # Conjunto para mantener IDs únicos de usuarios (cumple requisito)
        self._ids_usuarios = set()

    # ---------- Gestión de libros ----------
    def agregar_libro(self, libro: Libro) -> bool: #Añade un libro al catálogo de disponibles
        if libro.isbn in self._libros_disponibles:
            return False
        self._libros_disponibles[libro.isbn] = libro
        return True
    
    def quitar_libro(self, isbn: str) -> bool: #  Elimina un libro del catálogo de disponibles (solo si no está prestado).
        if isbn in self._libros_disponibles:
            del self._libros_disponibles[isbn]
            return True
        return False

    # ---------- Gestión de usuarios ----------
    def registrar_usuario(self, usuario: Usuario) -> bool: #Registra un nuevo usuario.
        if usuario.id_usuario in self._ids_usuarios:
            return False
        
        self._usuarios[usuario.id_usuario] = usuario
        self._ids_usuarios.add(usuario.id_usuario)
        return True

    def dar_baja_usuario(self, id_usuario: str) -> bool: # Elimina un usuario si no tiene libros prestados.
        usuario = self._usuarios.get(id_usuario)
        if not usuario:
            return False
        if usuario.libros_prestados:  # tiene libros prestados
            return False
        del self._usuarios[id_usuario]
        self._ids_usuarios.remove(id_usuario)
        return True

    # ---------- Préstamos y devoluciones ----------
    def prestar_libro(self, isbn: str, id_usuario: str) -> bool: #Presta un libro a un usuario.
        if isbn not in self._libros_disponibles:
            return False  # libro no disponible
        if id_usuario not in self._usuarios:
            return False  # usuario no registrado
        libro = self._libros_disponibles.pop(isbn)  # quitar de disponibles
        usuario = self._usuarios[id_usuario]
        usuario.tomar_prestado(libro)
        return True
    def devolver_libro(self, isbn: str, id_usuario: str) -> bool: #Devuelve un libro prestado.
        usuario = self._usuarios.get(id_usuario)
        if not usuario:
            return False

        # Buscar el libro en la lista de préstamos del usuario
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self._libros_disponibles[isbn] = libro
                return True
        return False  # libro no encontrado en préstamos del usuario

    # ---------- Búsquedas ----------
    def _todos_los_libros(self): # Generador que itera sobre todos los libros (disponibles y prestados)
        # Libros disponibles
        yield from self._libros_disponibles.values()
        # Libros prestados (recorriendo usuarios)
        for usuario in self._usuarios.values():
            yield from usuario.libros_prestados
    def buscar_por_titulo(self, titulo: str): #Busca libros cuyo título contenga la cadena (insensible)
        titulo_lower = titulo.lower()
        return [libro for libro in self._todos_los_libros()
                if titulo_lower in libro.titulo.lower()]
    def buscar_por_autor(self, autor: str): #Busca libros cuyo autor contenga la cadena.
        autor_lower = autor.lower()
        return [libro for libro in self._todos_los_libros()
                if autor_lower in libro.autor.lower()]
    def buscar_por_categoria(self, categoria: str): #Busca libros cuya categoría contenga la cadena.
        cat_lower = categoria.lower()
        return [libro for libro in self._todos_los_libros()
                if cat_lower in libro.categoria.lower()]

    # ---------- Listados específicos ----------
    def listar_prestamos_usuario(self, id_usuario: str): #Devuelve la lista de libros prestados a un usuario.
        usuario = self._usuarios.get(id_usuario)
        if usuario:
            return usuario.libros_prestados
        return None

    # Métodos auxiliares para el menú (mostrar listados)
    def listar_libros_disponibles(self): #Retorna lista de libros disponibles.
        return list(self._libros_disponibles.values())

    def listar_usuarios(self): #Retorna lista de usuarios registrados.
        return list(self._usuarios.values())