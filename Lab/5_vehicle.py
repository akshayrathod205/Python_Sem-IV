class Vehicle:
    def __init__(self, mileage, max_speed, name):
        self.mileage = mileage
        self.max_speed = max_speed
        self.name = name
        
    def seating_capacity(self):
        pass
    
    def fare(self):
        return (self.seating_capacity() * 20) + (self.seating_capacity() * 20 * 0.1)
    
    def vehicle_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Mileage: {self.mileage}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Seating Capacity: {self.seating_capacity()}")
        print(f"Fare: {self.fare()}")
        
class Bus(Vehicle):
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
        
    def seating_capacity(self):
        return 40
    
class Car(Vehicle):
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)
        
    def seating_capacity(self):
        return 4
    
bus = Bus(10, 100, "Volvo")
bus.vehicle_info()