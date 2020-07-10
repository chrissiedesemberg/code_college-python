class Restaurant:
    # Restaurant cuisine type
    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe restaurant"""
        print(f"The new restaurant, {self.name.title()}, makes the best {self.cuisine.title()} food in town! ")

    def open_restaurant(self):
        """Announce that restaurant is open"""
        print(f"The restaurant {self.name.title()} is now OPEN for business")

option_1 = Restaurant("verdiccio", "italian")
option_2 = Restaurant("ocean basket", "fish")
option_3 = Restaurant("wombles", "african")

print(f"\nMy favorite restaurant is {option_1.name.title()}.")
print(f"{option_1.name.title()} make the best {option_1.cuisine.title()} "
      f"food in Johannesburg.")
print(f"{option_3.name.title()} is in Fourways")
option_1.describe_restaurant()


print(f"\nMy favorite restaurant is {option_2.name.title()}.")
print(f"{option_2.name.title()} make the best {option_2.cuisine.title()} "
      f"food in Johannesburg.")
print(f"{option_3.name.title()} is in Sunninghill")
option_2.describe_restaurant()

print(f"\nMy favorite restaurant is {option_3.name.title()}.")
print(f"{option_3.name.title()} make the best {option_3.cuisine.title()} "
      f"food in Johannesburg.")
print(f"{option_3.name.title()} is in Parkhurst")
option_3.describe_restaurant()
