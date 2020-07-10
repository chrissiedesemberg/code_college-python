class Restaurant:
    # Restaurant cuisine type
    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f"\nThe new restaurant, {self.name.title()}, makes the best {self.cuisine.title()} food in town! ")

    def open_restaurant(self):
        """Announce that restaurant is open"""
        print(f"The restaurant {self.name.title()} is now OPEN for business")


restaurant = Restaurant("verdiccio", "italian")

print(f"\nMy favorite restaurant is {restaurant.name.title()}. They make the best "
      f"{restaurant.cuisine.title()} in Johannesburg.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

