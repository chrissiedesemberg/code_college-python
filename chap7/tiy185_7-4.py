prompt = f"\nPlease enter a topping to add on your pizza:"

while True:
    message = input(prompt)
    if message == "quit":
        print("Your pizza will be ready in 10 minutes")
        break
    else:
        print(f"\nAdding {message} to your pizza!")

