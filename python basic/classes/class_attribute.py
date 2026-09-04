class cat:
    species = "Felis catus"  # class attribute 
    
    def __init__(self, name):
        self.name = name      #instance attribute
        
    def meow(self):
        return f"{self.name} says Meow!"
    
    @classmethod
    def create_kitten(cls,name):
        return cls(f"Baby {name}")