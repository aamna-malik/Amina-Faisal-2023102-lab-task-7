class Car:
    def __init__(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.year} {self.make} {self.model} ({status})"


class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"


class Rental:
    def __init__(self):
        self.cars = []
        self.rented_cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, customer, car_index):
        if 0 <= car_index < len(self.cars):
            selected_car = self.cars[car_index]
            if selected_car.available:
                selected_car.available = False
                self.rented_cars.append((customer, selected_car))
                print(f"{customer.name} rented {selected_car.year} {selected_car.make} {selected_car.model}.")
            else:
                print("Sorry, the selected car is not available.")
        else:
            print("Invalid car index.")

    def return_car(self, customer, car_index):
        if 0 <= car_index < len(self.rented_cars):
            rented_customer, rented_car = self.rented_cars[car_index]
            if rented_customer == customer:
                rented_car.available = True
                del self.rented_cars[car_index]
                print(f"{customer.name} returned {rented_car.year} {rented_car.make} {rented_car.model}.")
            else:
                print("Invalid customer for returning the car.")
        else:
            print("Invalid rented car index.")

    def display_rented_cars(self):
        if not self.rented_cars:
            print("No cars are currently rented.")
        else:
            print("Rented Cars:")
            for index, (customer, car) in enumerate(self.rented_cars):
                print(f"{index + 1}. {car} - Rented by {customer}")


# Example usage:

# Create cars
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)
car3 = Car("Ford", "Mustang", 2023)

# Create a rental system
rental_system = Rental()

# Add cars to the rental system
rental_system.add_car(car1)
rental_system.add_car(car2)
rental_system.add_car(car3)

# Create customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Rent a car
rental_system.rent_car(customer1, 0)

# Display rented cars
rental_system.display_rented_cars()

# Return a car
rental_system.return_car(customer1, 0)

# Display rented cars after returning
rental_system.display_rented_cars()
