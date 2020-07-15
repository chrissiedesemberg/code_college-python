from chap11.name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first.lower() == 'q':
        break
    last = input("Please give me a last name: ")
    if last.lower() == 'q':
        break
    middle_available = input("\nDo you have a middle name? ")
    if middle_available.lower() == 'q':
        break
    elif middle_available.lower() == 'no':
        middle = None
    else:
        middle = input("\nWhat is your middle name? ")

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tNeatly formatted name: {formatted_name}.")