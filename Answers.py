# This program demonstrates polymorphism using a Vehicle theme.

# The base class representing a generic vehicle.
class Vehicle:
    """
    A base class for all vehicles.
    """
    def __init__(self, make, model):
        """
        Initializes a new Vehicle object.

        Args:
            make (str): The manufacturer of the vehicle.
            model (str): The specific model of the vehicle.
        """
        self.make = make
        self.model = model

    def move(self):
        """
        A placeholder method that all subclasses must implement.
        Raises a NotImplementedError if a subclass does not define its own move() method.
        """
        raise NotImplementedError("Subclasses must implement the 'move' method.")


# A subclass representing a car.
class Car(Vehicle):
    """
    A class for cars, inheriting from Vehicle.
    """
    def __init__(self, make, model, drive_type):
        """
        Initializes a Car object.

        Args:
            make (str): The car's manufacturer.
            model (str): The car's model.
            drive_type (str): The type of drivetrain (e.g., 'FWD', 'RWD', 'AWD').
        """
        super().__init__(make, model)
        self.drive_type = drive_type

    def move(self):
        """
        Implements the move() method for a car.
        """
        print(f"The {self.make} {self.model} is driving on the road! 🚗")


# A subclass representing a plane.
class Plane(Vehicle):
    """
    A class for planes, inheriting from Vehicle.
    """
    def __init__(self, make, model, num_engines):
        """
        Initializes a Plane object.

        Args:
            make (str): The plane's manufacturer.
            model (str): The plane's model.
            num_engines (int): The number of engines on the plane.
        """
        super().__init__(make, model)
        self.num_engines = num_engines

    def move(self):
        """
        Implements the move() method for a plane.
        """
        print(f"The {self.make} {self.model} is flying high above the clouds! ✈️")


# A function to demonstrate polymorphism.
def transport_item(vehicle):
    """
    Accepts a vehicle object and calls its move() method.
    This function doesn't need to know the specific type of vehicle.
    """
    print(f"\nTime to get moving in the {vehicle.make} {vehicle.model}!")
    vehicle.move()

# --- Main Execution Block ---
if __name__ == "__main__":
    print("--- Creating Objects ---")
    car = Car("Ford", "Focus", "FWD")
    plane = Plane("Boeing", "747", 4)

    print("\n--- Demonstrating Polymorphism ---")
    # Both objects are passed to the same function, but each calls its own
    # unique move() method.
    transport_item(car)
    transport_item(plane)
