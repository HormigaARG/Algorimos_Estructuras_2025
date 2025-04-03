def totalPaginas(libros):
    if len(libros) == 1:
        return libros[0]
    else:
        return libros[0] + totalPaginas(libros[1:])
    
print(totalPaginas([50,100,150]))    