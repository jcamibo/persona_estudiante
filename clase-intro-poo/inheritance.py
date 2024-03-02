#--------Class,methods,atributes, objects--------------------------------
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print("The vehicle has started.")
    
    def stop_engine(self):
        self.is_running = False
        print("The vehicle has stopped.")
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"The vehicle is now {self.color}.")

    def move(self):
        print("The vehicule is in move")

vehicle1 = Vehicle("peugeot","301","Blanco")
print (vehicle1.make, vehicle1.color, vehicle1.model)

vehicle1.start_engine()
vehicle1.change_color("Red")

#------------ inheritence-------------------------------- 
class Car(Vehicle):
    """Class Car que un hijo de Vehicle"""
    def __init__(self, make, model, color, num_doors):
        """Constructor"""
        super().__init__(make, model, color)
        self.num_doors = num_doors
    
    def open_doors(self):
        print(f"The {self.num_doors}-door car has opened its doors.")

    def move(self):
        """polimorf see the difference between this and Truck move function"""
        print("The car is in move")

class Truck(Vehicle):
    def __init__(self, make, model, color, cargo_capacity):
        super().__init__(make, model, color)
        self.cargo_capacity = cargo_capacity
    
    def load(self):
        """polimorf see the difference between this and Car move function"""
        print(f"The truck has been loaded with {self.cargo_capacity} tons of cargo.")

    def move(self):
        print("The truck is in move")

car1 = Car("Ford", "Mustang", "Red", 2)
car1.start_engine()
car1.open_doors()

truck1 = Truck("Chevrolet", "Silverado", "Black", 5)
truck1.start_engine()
truck1.load()
truck1.move()
car1.move()

#la proxima poner el ejemplo de personajes de viedo juegos, 