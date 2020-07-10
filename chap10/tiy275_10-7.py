print("Give me two numbers and I will add them for you.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number:")
    if first_number == 'q':
        break

    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("\nThis will only work with numbers! Try again with a number!\n")
    else:
        print(f"\n{first_number} + {second_number} = {answer}")
        print("Wasn't that fun!\n")

print("Thanks for playing! See you next time!")
