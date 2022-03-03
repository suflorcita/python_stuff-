class Curso:
    max_alumnos = 35 # definimos variable de clase

    def __init__(self, nombre, duracion, alumnos = None, costo=10):
        self.nombre = nombre
        self.duracion = duracion
        if alumnos is None:
            self.alumnos = []
        else:
            self.alumnos = alumnos
        self.costo = costo # costo tiene un valor por default
        """¿Por qué ese if? Las variables por default sólo se evalúan a la hora de ejecutar la sentencia def. 
        En nuestro caso necesitamos que self.alumnos sea una lista y las listas son objetos mutables. 
        Esto quiere decir que podemos modificarla sin volver a asignarla. Si en vez de 'alumnos = None' usáramos
        alumnos = [], entonces con cada nueva instancia del objeto estaríamos compartiendo los alumnos.
        Para evitar eso, en general la forma pythónica de hacerlo es usando None por default y asignando el valor
        deseado dentro de la función y no en el 'def' """

    def inscribir_alumno(self, nombre):
        self.alumnos.append(nombre) # para poder llamar a alumnos tengo que usar self.
        print(f'Se agregó al alumno/a {nombre}')

    def tomar_lista(self):
        for a in self.alumnos:
            print(f'Alumno: {a}')

    def resumen(self):
        print(f'Curso {self.nombre}, {self.duracion} clases pensadas para {len(self.alumnos)} alumnos\n'
              f'Por el muy módico precio de {self.costo} pesos.',
              # llamo variable de clase:
              f'La ocupación actual es del {round(len(self.alumnos)/self.max_alumnos,2)*100}%') 

curso_python = Curso("Python", 6)
print(curso_python.alumnos)

curso_python.inscribir_alumno("Sol")
curso_python.inscribir_alumno("Juana")
print(curso_python.alumnos)

curso_python.tomar_lista()
curso_python.resumen()

curso_ml = Curso("Machine Learning", 8)
curso_ml.inscribir_alumno("Juan")
curso_ml.inscribir_alumno("Tobias")
curso_ml.inscribir_alumno("Julian")

curso_ml.resumen()
print(curso_ml.alumnos)
