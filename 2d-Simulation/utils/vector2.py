import re


class vector2():
    def __init__(self, Xpos: int | float, Ypos: int | float):
        
        self.X: int|float = Xpos
        self.Y: int|float = Ypos

    def Value(self):
        return (self.X, self.Y)

    def setX(self, Xpos: int | float):
        self.X: int|float = Xpos

    def setY(self, Ypos: int | float):
        self.Y: int|float = Ypos
    
    def setValue(self, Xpos: int | float, Ypos: int | float):
        self.X: int|float = Xpos
        self.Y: int|float = Ypos

    def __str__(self):
        return f"vector2{self.Value()}"

    def __add__(self, obj: 'vector2'):
        return vector2(self.X + obj.X, self.Y + obj.Y)
    def __sub__(self, obj: 'vector2'):
        return vector2(self.X - obj.X, self.Y - obj.Y)
    
    def __rmul__(self, obj: int|float):
        return vector2(self.X * obj, self.Y * obj)
    def __mul__(self, obj: int|float):
        return vector2(self.X * obj, self.Y * obj)
    
    def __truediv__(self, obj: int|float):
        if obj != 0:
            X = self.X / obj
            Y = self.Y /obj
            return(vector2(X, Y))
        else: 
           return(vector2(1, 1))

    def __exp__(self, obj: 'vector2'):
        return vector2(self.X ** obj.X, self.Y ** obj.Y)
    
    def dot_product(self, obj: 'vector2') -> int|float:
        return self.x * obj.x + self.y * obj.y
    
    def magnitude(self):
        return ((self.X ** 2) + (self.Y ** 2)) ** 0.5
    
    def normalize(self):
        magnitude = self.magnitude()
        return (self / magnitude)