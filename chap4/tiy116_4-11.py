pizzas = ["BBQ chicken", "Meaty One", "Pepperoni"]

for pizza in pizzas:
    #print(pizza)
    print(f"I like {pizza} pizza")

print("\nI really, really love pizza!")
friend_pizzas = pizzas[:]
print(f"My friend's pizzas are {friend_pizzas}.")
pizzas.append("Margarita")
friend_pizzas.append("Tropical")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)



