class Car: 
    def __init__(self, color, mileage): 
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage} miles"

    def drive(self, miles_drive): 
        self.mileage +=  miles_drive

car1 = Car("blue", 20000)
car2 = Car("red", 30000)

print(car1)
print(str(car2))
print(car1.__repr__) # repr 

car1.drive(100)
print(car1.mileage)
