class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = {}
        self._socios = {}

    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            raise ValueError("Ya existe un libro con ese ISBN.")

        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios:
            raise ValueError("Ya existe un socio con ese DNI.")

        self._socios[socio.dni] = socio

    def prestar(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError("El libro no existe.")

        if dni not in self._socios:
            raise ValueError("El socio no existe.")

        libro = self._libros[isbn]
        socio = self._socios[dni]

        if not libro.disponible:
            raise ValueError("El libro ya está prestado.")

        if not socio.puede_pedir():
            raise ValueError("El socio llegó al máximo de libros.")

        if libro in socio.libros:
            raise ValueError("El socio ya tiene ese libro.")

        libro.prestar()
        try:
            socio.agregar_libro(libro)
        except Exception:
            libro.devolver()
            raise

    def devolver(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError("El libro no existe.")

        if dni not in self._socios:
            raise ValueError("El socio no existe.")

        libro = self._libros[isbn]
        socio = self._socios[dni]

        if libro not in socio.libros:
            raise ValueError("El socio no tiene ese libro.")

        if libro.disponible:
            raise ValueError("El libro ya está disponible.")

        libro.devolver()
        try:
            socio.quitar_libro(libro)
        except Exception:
            libro.prestar()
            raise

    def libros_disponibles(self):
        return [libro for libro in self._libros.values()
                if libro.disponible]
