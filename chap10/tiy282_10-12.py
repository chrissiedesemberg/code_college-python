import json


def get_stored_fav_number():
    """Give stored favorite_number"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        fav_number()
    else:
        print(f"Hey, we remember you! Your favorite number is {favorite_number}")


def fav_number():
    """Get favorite number"""
    favorite_number = input("What is your favorite number?")
    filename = 'favorite_number.json'
    with open(filename, "w") as f:
        json.dump(favorite_number, f)
    print(f"\nYour favorite number is {favorite_number}. We'll remember it!")

get_stored_fav_number()


