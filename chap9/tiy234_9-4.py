class Restaurant:
    # Restaurant cuisine type
    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f"\nThe new restaurant, {self.name.title()}, makes the best {self.cuisine.title()} food in town! ")

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

restaurant = Restaurant("verdiccio", "italian")

print(f"\nMy favorite restaurant is {restaurant.name.title()}. They make the best "
          f"{restaurant.cuisine.title()} in Johannesburg.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(4)

