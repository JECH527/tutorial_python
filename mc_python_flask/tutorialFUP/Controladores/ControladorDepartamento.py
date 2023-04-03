from tutorialFUP.Modelos.Departamento import Departamento
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)

"""
class ControladorDepartamento():

   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

   def __init__(self):

    print("Creando ControladorDepartamento")
   def index(self):
       print("Listar el Departemento correspondiente")
       elDepartamento = {

           "_id": "001",
           "nombre": "Cauca",

       }
       return [elDepartamento]
   def create(self, elDepartamento):
       print("Crear el Departamento")
       elDepartamento = Departamento(elDepartamento)
       return elDepartamento.__dict__

   def show(self, id):
       print("Mostrando el Departamento con el id ", id)
       elDepartamento = {

           "_id": "001",
           "nombre": "Cauca"

       }
       return elDepartamento
   def update(self, id, elDepartamento):
       print("Actualizando el Departamento con id ", id)
       elDepartamento = Departamento(elDepartamento)
       return elDepartamento.__dict__


   def delete(self, id):
       print("Elimiando la el Departamento con id ", id)
       return {"deleted_count": 1}