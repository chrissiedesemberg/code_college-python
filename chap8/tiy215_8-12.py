def ingredients(*toppings):
    print("\nYou have selected the following toppings:")
    for topping in toppings:
        print(f"{topping}")


ingredients("onions", "cheese", "bbq sauce")
