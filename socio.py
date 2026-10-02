class Socio:
    MAX_LIBROS = 3

    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        self._libros = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def libros(self):
        return self._libros.copy()

    def puede_pedir(self):
        return len(self._libros) < self.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError("El socio ya tiene el máximo de libros.")

        if libro in self._libros:
            raise ValueError("El socio ya tiene ese libro.")

        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError("El socio no tiene ese libro.")

        self._libros.remove(libro)

    def __str__(self):
        return (
            f"{self._nombre} (DNI {self._dni}) - "
            f"{len(self._libros)} libro(s) prestado(s)"
        )
