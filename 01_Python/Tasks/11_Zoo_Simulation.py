# Python Project: Zoo Simulation using Inheritance

# Base Animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} the {self.species} moves around."

    def __str__(self):
        return f"{self.name} the {self.species}"


# Subclass: Lion
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        return "Roar!"


# Subclass: Elephant
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def make_sound(self):
        return "Trumpet!"


# Subclass: Monkey
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey")

    def make_sound(self):
        return "Ooh ooh aah aah!"


# Zoo class to manage animals
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} has been added to {self.zoo_name}.")

    def make_all_sounds(self):
        print(f"\nSounds from all animals in {self.zoo_name}:")
        for animal in self.animals:
            print(f"{animal}: {animal.make_sound()}")

    def show_all_animals(self):
        print(f"\nAnimals in {self.zoo_name}:")
        for animal in self.animals:
            print(f"- {animal}")


# Example usage
if __name__ == "__main__":
    # Create a zoo
    my_zoo = Zoo("Wild World Zoo")

    # Create animals
    simba = Lion("Simba")
    dumbo = Elephant("Dumbo")
    george = Monkey("George")

    # Add animals to the zoo
    my_zoo.add_animal(simba)
    my_zoo.add_animal(dumbo)
    my_zoo.add_animal(george)

    # Show all animals in the zoo
    my_zoo.show_all_animals()

    # Make all animals produce sounds
    my_zoo.make_all_sounds()
