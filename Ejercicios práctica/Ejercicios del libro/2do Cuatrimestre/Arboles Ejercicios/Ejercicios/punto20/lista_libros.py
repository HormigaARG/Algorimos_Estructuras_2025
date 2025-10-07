from libro import Libro

# Lista de libros actualizada para el ejercicio
libros = [
    # Libros de Tanenbaum
    Libro("Sistemas Operativos Modernos", "9786073207307", "Tanenbaum", "Pearson", 1136, "Sistemas Operativos"),
    Libro("Redes de Computadoras", "9786073207314", "Tanenbaum", "Pearson", 960, "Redes"),
    Libro("Organización de Computadoras", "9789702604975", "Tanenbaum", "Prentice Hall", 800, "Arquitectura"),
    
    # Libros de Connolly
    Libro("Sistemas de Bases de Datos", "9788478290851", "Connolly", "Addison Wesley", 1234, "Bases de Datos"),
    Libro("Diseño de Bases de Datos", "9788478290868", "Connolly", "Addison Wesley", 650, "Bases de Datos"),
    
    # Libros de Rowling
    Libro("Harry Potter y la Piedra Filosofal", "9788478884456", "Rowling", "Salamandra", 256, "Fantasía"),
    Libro("Harry Potter y la Cámara Secreta", "9788478884951", "Rowling", "Salamandra", 288, "Fantasía"),
    Libro("Harry Potter y el Prisionero de Azkaban", "9788478885194", "Rowling", "Salamandra", 360, "Fantasía"),
    
    # Libros de Riordan
    Libro("Percy Jackson y el Ladrón del Rayo", "9788427200229", "Riordan", "Salamandra", 272, "Fantasía"),
    Libro("Percy Jackson y el Mar de los Monstruos", "9788427200236", "Riordan", "Salamandra", 288, "Fantasía"),
    
    # Libros de Morgan Kass
    Libro("Minería de Datos: Conceptos y Técnicas", "9780123814791", "Morgan Kass", "Morgan Kaufmann", 740, "Minería de Datos"),
    Libro("Fundamentos de Minería de Datos", "9780123814807", "Morgan Kass", "Morgan Kaufmann", 680, "Minería de Datos"),
    
    # Libros de algoritmos
    Libro("Introducción a los Algoritmos", "9780262033848", "Thomas Cormen", "MIT Press", 1312, "Algoritmos"),
    Libro("Algoritmos: Diseño y Análisis", "9780321573513", "Michael Goodrich", "Pearson", 720, "Algoritmos"),
    Libro("Algoritmos Eficientes", "9780321573520", "Robert Sedgewick", "Addison Wesley", 984, "Algoritmos"),
    
    # Libros de bases de datos
    Libro("Fundamentos de Bases de Datos", "9780321122268", "Abraham Silberschatz", "McGraw-Hill", 1100, "Bases de Datos"),
    Libro("Bases de Datos: Teoría y Práctica", "9780321122275", "Hector Garcia-Molina", "Pearson", 780, "Bases de Datos"),
    
    # Libros de minería de datos
    Libro("Minería de Datos Aplicada", "9780123814814", "Jiawei Han", "Morgan Kaufmann", 740, "Minería de Datos"),
    Libro("Técnicas de Minería de Datos", "9780123814821", "Pang-Ning Tan", "Addison Wesley", 650, "Minería de Datos"),
    
    # Libro específico con ISBN solicitado
    Libro("Los 100", "9789504967453", "Kass Morgan", "VR Editoras", 320, "Ciencia Ficción"),
    
    # Libros con más de 873 páginas
    Libro("El Señor de los Anillos", "9788445000665", "J.R.R. Tolkien", "Minotauro", 1216, "Fantasía"),
    Libro("Guerra y Paz", "9788420653632", "León Tolstói", "Alianza", 1568, "Clásico"),
    Libro("En Busca del Tiempo Perdido", "9788437606194", "Marcel Proust", "Cátedra", 4215, "Clásico"),
    
    # Otros libros relevantes
    Libro("Cien Años de Soledad", "9780307474728", "Gabriel García Márquez", "Sudamericana", 471, "Realismo Mágico"),
    Libro("1984", "9780451524935", "George Orwell", "Penguin", 328, "Ciencia Ficción"),
]
