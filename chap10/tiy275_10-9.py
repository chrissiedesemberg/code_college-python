filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f"\n{contents}")
    except FileNotFoundError:
        pass