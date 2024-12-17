# Base Class: Vehicle
class Vehicle:
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed  # Speed in km/h
        self.capacity = capacity  # Number of passengers
    
    def move(self):
        print(f"The vehicle {self.name} is moving at {self.speed} km/h.")
    
    def details(self):
        print(f"Name: {self.name}, Speed: {self.speed} km/h, Capacity: {self.capacity} passengers")


# Subclass: Car
class Car(Vehicle):
    def __init__(self, name, speed, capacity, fuel_type):
        super().__init__(name, speed, capacity)
        self.fuel_type = fuel_type  # Gasoline, Diesel, Electric
    
    def move(self):
        print(f"The car '{self.name}' is driving on the road at {self.speed} km/h.")


# Subclass: Plane
class Plane(Vehicle):
    def __init__(self, name, speed, capacity, airline):
        super().__init__(name, speed, capacity)
        self.airline = airline  # Airline name
    
    def move(self):
        print(f"The plane '{self.name}' from {self.airline} is flying at {self.speed} km/h.")


# Subclass: Boat
class Boat(Vehicle):
    def __init__(self, name, speed, capacity, boat_type):
        super().__init__(name, speed, capacity)
        self.boat_type = boat_type  # Yacht, Ferry, Sailboat
    
    def move(self):
        print(f"The boat '{self.name}' is sailing on water at {self.speed} km/h.")


# Testing Polymorphism
def main():
    # Create objects of each class
    car = Car("Tesla Model 3", 150, 5, "Electric")
    plane = Plane("Boeing 747", 900, 416, "Delta Airlines")
    boat = Boat("Sea Breeze", 50, 30, "Yacht")
    
    # Store objects in a list
    vehicles = [car, plane, boat]
    
    # Demonstrate polymorphism
    print("### Polymorphism in Action ###\n")
    for vehicle in vehicles:
        vehicle.move()
        vehicle.details()
        print()

if __name__ == "__main__":
    main()
