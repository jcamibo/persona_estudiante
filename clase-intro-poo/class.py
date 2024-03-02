#--------Class,methods,atributes, objects--------------------------------
class Vehicle:
    #los atributos viven en la clase fuera de los metodos
    def __init__(self, make, model, color):
        """Este metodo sirve para inicializar el objeto que se crea, recuerden las classes son un molde, y las instancias son los objetos creados con esa clase"""
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):
        """Este metodo sirve para encender el motor del vehiculo"""
        self.is_running = True
        print("El vehiculo a iniciado.")
    
    def stop_engine(self):
        """Este metodo sirve para apagar el motor del vehiculo"""
        self.is_running = False
        print("El vehiculo se a detenido.")
    
    def change_color(self, new_color):
        """Este metodo sirve cambiar el color del vehiculo"""
        self.color = new_color
        print(f"El nuevo color del  vehiculo es: {self.color}.")

    def print_atributs(self):
        print(self.color,self.make,self.model)

#en esta linea estamos creando un objeto, otra forma que vamos a encontrar para decir esto es que estamos instanciando una clase
vehicle1 = Vehicle("peugeot","301","Blanco")
print (vehicle1.make, vehicle1.color, vehicle1.model)
vehicle2 = Vehicle("Ford","Explorer","2002")
vehicle2.print_atributs()
print (vehicle2.make)
# Iniciamos el motor del vehiculo 1 
vehicle1.start_engine()
#cambiamos el color del vehiculo 1 
vehicle1.change_color("Red")

