filename = "guest_book.txt"


while True:
    name = input("What is your name?")
    if name != "q":
        with open(filename, "a") as file_object:
            file_object.write(f"Welcome to the best guesthouse in the country, {name}!\n")
    else:
        break
