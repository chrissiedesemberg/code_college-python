class Restaurant:
    # Restaurant cuisine type
    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f"\nThe new restaurant, {self.name.title()}, makes the best {self.cuisine.title()} in town! ")

    def open_restaurant(self):
        """Announce that restaurant is open"""
        print(f"The restaurant {self.name.title()} is now OPEN for business")

    def set_number_served(self, people):
        """Add the given amount to the amount of people served"""
        self.number_served = people
        print(f"They have now served {self.number_served} people")

    def increment_number_served(self, person):
        """Add the given amount to the amount of people served"""
        self.number_served += person
        print(f"UPDATED - They have served a total of {self.number_served} people")


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine, *flavours):
        """Initialize name and type attributes."""
        super().__init__(name, cuisine)
        self.flavours = flavours


    def flavours(self):
        print(f"Here are the flavours available:\n"
              f"{self.flavours}")

shop_1 = IceCreamStand("Ice cream shop", "desserts", "vanilla", "strawberry", "lime")
shop_1.describe_restaurant()
shop_1.flavours()
