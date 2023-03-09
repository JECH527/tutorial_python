#Crear un diccionario
#crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.
d1 = dict([
      ('Nombre', 'Estheban'),
      ('Edad', 21),
      ('Documento', 1003882),
])
print(d1)

#Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key
for x in d1:
    print(d1[x])

#Diccionarios anidados
#Los diccionarios en Python pueden contener uno dentro de otro. Podemos ver como los valores anidado uno y dos del diccionario d contienen a su vez otro diccionario.
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}

#Operaciones con diccionario
#El método clear() elimina todo el contenido del diccionario.
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

#El método get() nos permite consultar el value para un key determinado. El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor a devolver si no se encuentra la key.
d = {'a': 1, 'b': 2}
print(d.get('b')) #1
print(d.get('z', 'No encontrado')) #No encontrado

#El método items() devuelve una lista con los keys y values del diccionario. Si se convierte en list se puede indexar como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value.
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

#El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

#El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}