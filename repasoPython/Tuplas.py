#Operaciones con tuplas
#El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.
l = [1, 1, 1, 3, 5]
print(l.count(1))

#El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.
l = [7, 7, 7, 3, 5]
print(l.index(5))

#El método index() también acepta un segundo parámetro opcional, que indica a partir de que índice empezar a buscar el objeto.
l = [7, 7, 7, 3, 5]
print(l.index(7, 2))


#Tuplas anidadas
def cargar_paisespoblacion():
    paises = []
    for x in range(5):
        nom = input("Ingresar el nombre del pais:")
        cant = int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom, cant))
    return paises


def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])


def pais_maspoblacion(paises):
    pos = 0
    for x in range(1, len(paises)):
        if paises[x][1] > paises[pos][1]:
            pos = x
    print("Pais con mayor cantidad de habitantes:", paises[pos][0])


# bloque principal

paises = cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)

