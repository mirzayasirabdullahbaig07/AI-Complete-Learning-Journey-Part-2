# Step 1: Base Class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price:.2f}")


# Step 2: Subclasses
class FoodItem(MenuItem):
    def __init__(self, name, price, cuisine_type):
        super().__init__(name, price)
        self.cuisine_type = cuisine_type

    def display(self):
        print(f"[Food] {self.name} ({self.cuisine_type}): ${self.price:.2f}")


class DrinkItem(MenuItem):
    def __init__(self, name, price, is_cold=True):
        super().__init__(name, price)
        self.is_cold = is_cold

    def display(self):
        temp = "Cold" if self.is_cold else "Hot"
        print(f"[Drink] {self.name} ({temp}): ${self.price:.2f}")


# Step 3: Menu Class
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to the menu.")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{item.name} removed from the menu.")
                return
        print(f"Item '{name}' not found in the menu.")

    def display_menu(self):
        if not self.items:
            print("The menu is empty.")
        else:
            print("\n=== Restaurant Menu ===")
            for item in self.items:
                item.display()


# Step 4: User Interface
def show_menu_options():
    print("""
========= Restaurant Menu System =========
1. Add Food Item
2. Add Beverage Item
3. Remove Item
4. Display Menu
5. Exit
""")


def main():
    menu = Menu()

    while True:
        show_menu_options()
        choice = input("Select an option (1 to 5): ")

        if choice == '1':
            name = input("Enter food name: ")
            price = float(input("Enter food price: $"))
            cuisine = input("Enter cuisine type (e.g. Italian, Indian): ")
            food = FoodItem(name, price, cuisine)
            menu.add_item(food)

        elif choice == '2':
            name = input("Enter beverage name: ")
            price = float(input("Enter beverage price: $"))
            is_cold = input("Is it a cold drink? (yes/no): ").strip().lower() == "yes"
            beverage = DrinkItem(name, price, is_cold)
            menu.add_item(beverage)

        elif choice == '3':
            name = input("Enter the name of the item to remove: ")
            menu.remove_item(name)

        elif choice == '4':
            menu.display_menu()

        elif choice == '5':
            print("Exiting the menu system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the program
main()
