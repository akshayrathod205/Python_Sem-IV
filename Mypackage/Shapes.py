from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def volume():
        pass
    
class Sphere(Shapes):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def volume(self):
        volume = ((4/3) * (self.radius ** 3))
        print(f"Volume: {volume}")
        
class Cube(Shapes):
    def __init__(self, side):
        super().__init__()
        self.side = side
        
    def volume(self):
        volume = self.side ** 3
        print(f"Volume: {volume}")