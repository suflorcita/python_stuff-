class Punto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): 
        return f"El punto es ({self.x},{self.y})"


punto = Punto(3,4)
print(punto)