class Libro:

    def __init__(self, titulo, isbn, autores, editorial, paginas):
        self.titulo = titulo          # Título del libro
        self.isbn = isbn              # Código ISBN
        self.autores = autores        # Lista o cadena con los autores
        self.editorial = editorial    # Editorial del libro
        self.paginas = paginas        # Cantidad de páginas

    def __str__(self):
        return (f'Título: {self.titulo} | '
                f'ISBN: {self.isbn} | '
                f'Autores: {self.autores} | '
                f'Editorial: {self.editorial} | '
                f'Páginas: {self.paginas}')
