# This program demonstrates key object-oriented programming concepts using a Superhero theme.

# The base class representing a generic superhero.
class Superhero:
    """
    A base class for all superheroes.

    Attributes:
        name (str): The superhero's name.
        superpower (str): The primary special ability.
        _weakness (str): A protected attribute for the superhero's weakness.
    """
    def __init__(self, name, superpower, weakness):
        """
        Initializes a new Superhero object.

        Args:
            name (str): The superhero's name.
            superpower (str): The primary special ability.
            weakness (str): The superhero's vulnerability.
        """
        self.name = name
        self.superpower = superpower
        # Encapsulation: Using a single underscore suggests this is a protected attribute,
        # which should not be accessed directly from outside the class.
        self._weakness = weakness

    def use_superpower(self):
        """
        A method that prints a message when the superhero uses their superpower.
        """
        print(f"{self.name} is using their power: {self.superpower}!")

    def get_weakness(self):
        """
        A public method to safely retrieve the encapsulated weakness attribute.
        This provides controlled access to a protected attribute.
        """
        return self._weakness


# A subclass that inherits from the Superhero class.
class FlyingSuperhero(Superhero):
    """
    A subclass representing a superhero who can fly.
    It inherits attributes and methods from the Superhero class.

    Attributes:
        name (str): The superhero's name.
        superpower (str): The primary special ability.
        _weakness (str): A protected attribute for the superhero's weakness.
        flight_speed (int): The speed at which the superhero can fly, in mph.
    """
    def __init__(self, name, superpower, weakness, flight_speed):
        """
        Initializes a new FlyingSuperhero object.

        Args:
            name (str): The flying superhero's name.
            superpower (str): The primary special ability (e.g., flight).
            weakness (str): The superhero's vulnerability.
            flight_speed (int): The speed at which the superhero can fly, in mph.
        """
        # Inheritance: Call the constructor of the parent class to initialize
        # the inherited attributes.
        super().__init__(name, superpower, weakness)
        self.flight_speed = flight_speed

    def fly(self):
        """
        A method unique to flying superheroes.
        """
        print(f"{self.name} is soaring through the sky at {self.flight_speed} mph!")

    # Polymorphism: Overriding the parent class's method to provide a more specific action.
    def use_superpower(self):
        """
        Overrides the parent method to provide a unique message for flying superheroes.
        """
        print(f"{self.name} is taking flight! Their superpower is {self.superpower}!")


# --- Main Execution Block ---
# This code will run when the script is executed.
if __name__ == "__main__":
    print("--- Creating Objects ---")
    # Create an instance of the base class.
    hero_one = Superhero("Captain Courage", "Enhanced Strength", "Magic")

    # Create an instance of the subclass.
    hero_two = FlyingSuperhero("Swiftwind", "Super Speed", "Extreme Cold", 800)

    print("\n--- Demonstrating the Base Class (Captain Courage) ---")
    print(f"Name: {hero_one.name}")
    print(f"Superpower: {hero_one.superpower}")
    hero_one.use_superpower()
    print(f"Weakness (using a public method): {hero_one.get_weakness()}")

    print("\n--- Demonstrating the Subclass (Swiftwind) ---")
    print(f"Name: {hero_two.name}")
    print(f"Superpower: {hero_two.superpower}")
    print(f"Flight Speed: {hero_two.flight_speed} mph")

    # This calls the overridden method in the subclass.
    # This demonstrates polymorphism, as the same method name (use_superpower) behaves differently
    # for each object type.
    hero_two.use_superpower()

    # This calls the new method unique to the subclass.
    hero_two.fly()

    print(f"Weakness (using a public method): {hero_two.get_weakness()}")
