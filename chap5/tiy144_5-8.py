username = ["admin", "twin123", "learn456", "guessed321", "battlesteed832"]

for name in username:
    if name != "admin":
        print(f"Hello {name}! Thank you for logging in!")
    else:
        print(f"Hello {name}, would you like to see a status report?")


