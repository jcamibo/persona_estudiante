#--------Class,methods,atributes, encapsulation, objects--------------------------------

class Vehicle:
    def __init__(self, make, model, color):
        self._make = make
        self.model = model
        self._color = color
        self._is_running = False
    
    def start_engine(self):
        self._is_running = True
        print("The vehicle has started.")
    
    def stop_engine(self):
        self._is_running = False
        print("The vehicle has stopped.")
    
    def change_color(self, new_color):
        self._color = new_color
        print(f"The vehicle is now {self._color}.")
    
    def get_make(self):
        return self._make
    
    def set_make(self, make):
        self._make = make
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    def get_is_running(self):
        return self._is_running


car1 = Vehicle("Ford", "Mustang", "Red")
print(car1.get_make())  

car1.set_make("Chevrolet")
print(car1.get_make())  

print(car1.model)
