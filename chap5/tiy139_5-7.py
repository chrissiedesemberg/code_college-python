fruits = ["bananas", "oranges", "apricots", "strawberries", "raspberries", "apples", "pears"]
favorite_fruit = ["figs", "oranges", "apples", "nectarines"]

for fruit in fruits:
    if fruit == "bananas" or fruit == "apricots" or fruit == "oranges":
        print(f"Yes, we have that {fruit.title()}")
    elif fruit == "raspberries" or fruit == "apples" or fruit == "strawberries":
        print(f"Yes, we have that {fruit.title()}")
    else:
        print(f"Sorry we don't have that fruit!")

for fav_fruit in favorite_fruit:
    if fav_fruit == "figs" or fav_fruit == "apples":
        print(f"You really like {fav_fruit}!")
    elif fav_fruit == "oranges":
        print(f"You really like {fav_fruit}!")
    else:
        print(f"We don't have the fruit you want!")