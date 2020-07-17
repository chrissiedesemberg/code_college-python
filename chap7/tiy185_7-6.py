
#break

# ask_topping = input("\nPlease enter a topping to add on your pizza:")
# while True:
#     message = ask_topping
#     if message == "quit":
#         print("Your pizza will be ready in 10 minutes")
#         break
#     else:
#         print(f"\nAdding {message} to your pizza!")

#active
# ask_topping = input("\nPlease enter a topping to add on your pizza:")
# active = True
# while active:
#     message = ask_topping
#     if message == "quit":
#         print("Your pizza will be ready in 10 minutes")
#         active = False
#     else:
#         print(f"\nAdding {message} to your pizza!")

#conditional test

ask_topping = "\nPlease enter a topping to add on your pizza:"

while True:
    message = input(ask_topping)
    if message != "quit":
        print(f"Added {message.upper()} to your pizza!")
    else:
        print("Your pizza will be ready in 10 minutes!")
        break
