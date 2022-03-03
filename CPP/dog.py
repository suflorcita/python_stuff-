class Dog: 
    # Class attribute
    species = "Canis Familiaris"    
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    
    # Instance method 
    def __str__(self): 
        return f"{self.name} is {self.age} years old"

    def speak(self, sound): 
        return f"{self.name} says {sound}"

class JackRusselTerrier(Dog): 
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog): 
    pass

class Bulldog(Dog): 
    pass

class GoldenRetriever(Dog): 
    def speak(self, sound="Bark"): 
        return super().speak(sound)


golden = GoldenRetriever("Golden", 2)
print(golden.speak())



