class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x, y)
    
    def __sub__(self, obj):
        x = self.x - obj.x
        y = self.y - obj.y
        return Point(x, y)
    
    def __lt__(self, obj):
        if(((self.x ** 2 + self.y ** 2) ** 0.5) < ((obj.x ** 2 + obj.y ** 2) ** 0.5)):
            return True
        else:
            return False
        
    def __gt__(self, obj):
        if(((self.x ** 2 + self.y ** 2) ** 0.5) > ((obj.x ** 2 + obj.y ** 2) ** 0.5)):
            return True
        else:
            return False
        
    def __str__(self):
        return (f"X co-ordinate: {self.x} Y co-ordinate: {self.y}")
    
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2
print(p3)