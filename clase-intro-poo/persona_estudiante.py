class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def obtener_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Genero: {self.genero}")
        
    def cumplir_años(self):
        self.edad += 1
        print(f"Acabas de cumplir {self.edad} años")
        
persona1 = Persona("Juan", 25, "Hombre")

persona1.obtener_informacion()
persona1.cumplir_años()
persona1.obtener_informacion()

#hijos, herencia

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso
        
    def estudiar(self):
        print("Estudias para el examen")
        
    def pasar_curso(self):
        self.curso += 1
        print(f"Felicidades, pasas al curso: {self.curso}")
        
print()
Estudiante1 = Estudiante("Andres", 9, "Hombre", 7)
Estudiante1.obtener_informacion()
Estudiante1.estudiar()
Estudiante1.pasar_curso()
print()
Estudiante2 = Estudiante("Camila", 5, "Mujer", 4)
Estudiante2.cumplir_años()
Estudiante2.obtener_informacion()
Estudiante2.estudiar()
Estudiante2.pasar_curso()