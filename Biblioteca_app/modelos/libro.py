class Libro: #Representa un libro con título, autor, categoría e ISBN.
    
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str): #Inicialización de un libro con sus atributos.
        # Almacenamos título y autor en una tupla para hacerlos inmutables
        self._titulo_autor = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn
        
    # Propiedades de solo lectura para título y autor (inmutables)
    @property
    def titulo(self) -> str: #Permite acceder al título pero no modificarlo.
        return self._titulo_autor[0]
    
    @property
    def autor(self) -> str: #Permite acceder al autor pero no modificarlo.
        return self._titulo_autor[1]
    
    @property
    def categoria(self) -> str: #Permite acceder a la categoría, que es mutable.
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str):#Permite modificar la categoría si es necesario.
        self._categoria = nueva_categoria
        
    @property
    def isbn(self) -> str:
        return self._isbn

    def __str__(self) -> str: #Representación legible del libro.
        return f"'{self.titulo}' por {self.autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"