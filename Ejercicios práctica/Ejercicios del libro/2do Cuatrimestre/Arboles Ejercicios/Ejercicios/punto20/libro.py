class Libro:

    def __init__(self, titulo, isbn, autor, editorial, paginas, categoria=None):
        self.titulo = titulo          # Título del libro
        self.isbn = isbn              # Código ISBN
        self.autor = autor            # Autor del libro
        self.editorial = editorial    # Editorial del libro
        self.paginas = paginas        # Cantidad de páginas
        self.categoria = categoria    # Categoría/tema del libro

    def __str__(self):
        return (f'Título: {self.titulo} | '
                f'ISBN: {self.isbn} | '
                f'Autor: {self.autor} | '
                f'Editorial: {self.editorial} | '
                f'Páginas: {self.paginas} | '
                f'Categoría: {self.categoria}')