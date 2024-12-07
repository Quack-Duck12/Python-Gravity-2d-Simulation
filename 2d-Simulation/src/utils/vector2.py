class vector2():
    def __init__(self, Xpos: int | float, Ypos: int | float):
        
        self.X: int|float = Xpos
        self.Y: int|float = Ypos
        self.Value: tuple = (Xpos, Ypos)

    def setX(self, Xpos: int | float):
        self.X: int|float = Xpos
        self.Value: tuple = (self.X, self.Y)

    def setY(self, Ypos: int | float):
        self.Y: int|float = Ypos
        self.Value: tuple = (self.X, self.Y)
    
    def setValue(self, Xpos: int | float, Ypos: int | float):
        self.Value: tuple = (Xpos, Ypos)
        self.X: int|float = Xpos
        self.Y: int|float = Ypos

    def __add__(self, obj: 'vector2'):
        return vector2(self.X + obj.X, self.Y + obj.Y)
    def __sub__(self, obj: 'vector2'):
        return vector2(self.X - obj.X, self.Y - obj.Y)
    
    def __mul__(self, obj: int|float):
        return vector2(self.X * obj, self.Y * obj)
    
    def __truediv__(self, obj: int|float):
        if obj != 0:
            X = self.X / obj
            Y = self.Y / obj
            return(vector2(X, Y))
        else: 
            raise(f"Can't Divide The pos of {self} By 0")

    def __exp__(self, obj: int|float):
        return vector2(self.X ** obj, self.Y ** obj)
    
    def dot_product(self, obj: 'vector2') -> int|float:
        return self.x * obj.x + self.y * obj.y