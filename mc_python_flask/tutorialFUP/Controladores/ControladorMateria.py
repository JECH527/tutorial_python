from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Modelos.Departamento import Departamento

"""

Dentro de la clase se crean unos metodos, estos serán los encargados de manipular

a los modelos, en estos se programarán las tareas básicas tales como crear, listar,

visualizar, modificar y eliminar. (CRUD)

"""



class ControladorMateria():

   """

   constructor que permite llevar a cabo la creacion de instancias del controlador.

   """

   def __init__(self):

       self.repositorioMateria = RepositorioMateria()
       self.repositorioDepartamento = RepositorioDepartamento()

       print("Creando ControladorMateria")


   def index(self):

       print("Listar la Materia correspondiente")

       unaMateria = {

           "_id": "abc321",

           "nombre": "Español",

       }

       return [unaMateria]


   def create(self, laMateria):

       print("Crear la Materia")

       laMateria = Materia(laMateria)

       return laMateria.__dict__


   def show(self, id):

       print("Mostrando la Materia con la id ", id)

       laMateria = {

           "_id": "abc321",

           "nombre": "Creditos Libres"

       }

       return laMateria


   def update(self, id, laMateria):

       print("Actualizando la materia con id ", id)

       laMateria = Materia(laMateria)

       return laMateria.__dict__


   def delete(self, id):

       print("Elimiando la Materia con id ", id)

       return {"deleted_count": 1}

   """
   Relación departamento y materia
   """

   def asignarDepartamento(self, id, id_departamento):
       materiaActual = Materia(self.repositorioMateria.findById(id))
       departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
       materiaActual.departamento = departamentoActual
       return self.repositorioMateria.save(materiaActual)