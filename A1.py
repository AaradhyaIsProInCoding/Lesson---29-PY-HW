class Dog:
    species = "Canis lupus familiaris"  
    def __init__(self, breed, age):
        
        self.breed = breed
        self.age = age
    
    def display_details(self):
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Species: {Dog.species}")
        print("-" * 30)

dog1 = Dog("Golden Retriever", 5)
dog2 = Dog("Bulldog", 3)

dog1.display_details()
dog2.display_details()