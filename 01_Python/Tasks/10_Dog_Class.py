# Step 1: Define the class
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = True

    def bark(self):
        print(f"Woof! My name is {self.name}.")

    def eat(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f"{self.name} has eaten and is now full.")
        else:
            print(f"{self.name} is already full.")

    def dog_info(self):
        hunger_status = "Yes" if self.is_hungry else "No"
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Hungry: {hunger_status}")
        print("-" * 30)

# Step 2: Create dog objects
dog1 = Dog("Rockey", "German Shepherd", 4)
dog2 = Dog("Bella", "Labrador", 2)
dog3 = Dog("Charlie", "Poodle", 3)

# Step 3: Test methods for each dog
for dog in [dog1, dog2, dog3]:
    dog.bark()
    dog.dog_info()
    dog.eat()
    dog.dog_info()

# Step 4: Bonus Challenge - Manage a list of dogs
print("\n=== Bonus Challenge ===")

# Creating a list of dogs
dog_list = [dog1, dog2, dog3]

# Bark if hungry and feed all
for dog in dog_list:
    if dog.is_hungry:
        dog.bark()
        dog.eat()

# Show final info of all dogs
print("\nFinal Dog Status:")
for dog in dog_list:
    dog.dog_info()
