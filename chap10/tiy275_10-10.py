filenames = ["milton.txt", "planet_stories.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        number_words = words.count("and")
    print(f"The file {filename} has the word 'and' printed are {number_words} in it.")

