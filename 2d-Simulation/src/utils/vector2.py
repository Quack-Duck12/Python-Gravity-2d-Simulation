class vector2():
    def __init__(self, Xpos: int | float, Ypos: int | float):
        
        self.X: int|float = Xpos
        self.Y: int|float = Ypos

    def setX(self, Xpos: int | float):
        self.X: int|float = Xpos

    def setY(self, Ypos: int | float):
        self.Y: int|float = Ypos
    
    def setValue(self, Xpos: int | float, Ypos: int | float):
        self.X: int|float = Xpos
        self.Y: int|float = Ypos

    def __add__(self, obj: 'vector2'):
        return vector2(self.X + obj.X, self.Y + obj.Y)
    def __sub__(self, obj: 'vector2'):
        return vector2(self.X - obj.X, self.Y - obj.Y)
    
    def __mul__(self, scalar_value: int|float):
        return vector2(self.X * scalar_value, self.Y * scalar_value)
    
    def __truediv__(self, scalar_value: int|float):
        if scalar_value != 0:
            X = self.X / scalar_value
            Y = self.Y /scalar_value
            return(vector2(X, Y))
        else: 
            raise(f"Can't Divide The pos of {self} By 0")

    def __exp__(self, obj: 'vector2'):
        return vector2(self.X ** obj.X, self.Y ** obj.Y)
    
    def dot_product(self, obj: 'vector2') -> int|float:
        return self.x * obj.x + self.y * obj.y