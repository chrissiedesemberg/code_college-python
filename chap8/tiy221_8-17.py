def describe_city(name, country="germany"):
    print(f"\nOne of my top three cities, {name.title()}, "
          f"is in {country.title()}.")


describe_city("Koln")
describe_city("Edinburg", country="scotland")
describe_city("Ronda", country="spain")

print("\n...")


def make_album(name, title, number_songs=None):
    if number_songs:
        album = f"\nArtist name: {name.title()}, Album title: {title.title()}, Number of songs: {number_songs}"
    else:
        album = f"\nArtist name: {name.title()}, Album title: {title.title()}"
    return album


album_1 = make_album("Avenged Sevenfold", "Nightmare", number_songs=12)
album_2 = make_album("Avenged Sevenfold", "Nightmare")
album_3 = make_album("Avenged Sevenfold", "Nightmare")

print(album_1)
print(album_2)
print(album_3)

print("\n...")


def ingredients(*toppings):
    print("\nYou have selected the following toppings:")
    for topping in toppings:
        print(f"{topping}")


ingredients("onions", "cheese", "bbq sauce")


