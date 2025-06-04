class Vehicle:
    def __init__(self, vehicle_type, name, price_per_day):
        self.vehicle_type = vehicle_type
        self.name = name
        self.price_per_day = price_per_day
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Rented"
        print(f"{self.vehicle_type} - {self.name} | Rs.{self.price_per_day}/day | {status}")


class RentalSystem:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_available_vehicles(self):
        print("\n Available Vehicles")
        for v in self.vehicles:
            if v.is_available:
                v.display_info()
        print()
    
    def rent_vehicle(self, vehicle_name):
        for v in self.vehicles:
            if v.name.lower() == vehicle_name.lower() and v.is_available:
                v.is_available = False
                print(f"You have rented '{v.name}' for Rs.{v.price_per_day}/day.\n  ")
                return
            print("Vehicle not available or already rented. \n")

    def return_vehicle(self, vehicle_name):
        for v in self.vehicles:
            if v.name.lower() == vehicle_name.lower() and not v.is_available:
                v.is_available = True
                print(f"Thank you for returning '{v.name}'.\n")
                return
            print("This vehicle was not rented or doesnt exist. \n")

rental_system = RentalSystem()


rental_system.add_vehicle(Vehicle("Car", "Toyota Corolla", 3000))
rental_system.add_vehicle(Vehicle("Bike", "Honda 125", 800))
rental_system.add_vehicle(Vehicle("Car", "Suzuki Alto", 2500))
rental_system.add_vehicle(Vehicle("Bike", "Yamaha YBR", 1000))

while True:
    print("==== Vehicle Rental Menu ====")
    print("1. Show Available vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a vehicle")
    print("4. Exit")


    choice = input("Enter your choice (1-4)")
   
    if choice == '1':
      rental_system.show_available_vehicles()
    elif choice == '2':
        name = input("Enter the name of the vehicle you want to rent")
        rental_system.rent_vehicle(name)
    elif choice == '3':
        name = input("Enter the name of the vehicle you want to return")
        rental_system.return_vehicle(name)
    elif choice == '4':
        name = input("Thank you for using the vehicle rental system. Goodbye!")
        break
    else:
        print("Invalid Input. Please choose between 1 to 4. \n")
    

