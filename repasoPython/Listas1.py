#Listas con operaciones
#adjuntar
notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
suma_de_notas = sum(notas)
print(suma_de_notas)

#La función built-in len () devuelve la longitud
notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
cantidad_notas = len(notas)
print(cantidad_notas)

#Python nos trae el método remove(), que toma como parámetro el valor que queremos eliminar de nuestra lista.
notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
notas.remove(9.0)
print(notas)

#Contar elementos en una lista con el método count()
cantidad_sietes = notas.count(7.0)
print (cantidad_sietes)

#Listas enlazadas
# A Nodo de lista enlazada
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Función para imprimir una lista enlazada dada
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=' —> ')
        ptr = ptr.next

    print('None')


# Función para construir una lista enlazada a partir de un conjunto dado de claves
def construct(keys):
    head = None

    # empieza desde el final de la lista
    for i in reversed(range(len(keys))):
        # asigna un nuevo nodo en un heap y establece sus datos
        head = Node(keys[i], head)

    return head


if __name__ == '__main__':
    # Teclas de entrada
    keys = [1, 2, 3, 4]

    # apunta al nodo principal de la lista enlazada
    head = construct(keys)

    # Lista enlazada de impresión
    printList(head)