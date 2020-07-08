short_messages = [
    "Hi there, champ!",
    "Whatcha doing good-looking?",
    "Catch you later"
]
sent_messages = []


def send_messages():
    for message in short_messages:
        sent_messages.append(message[:])
        print(message)


send_messages()


print(sent_messages)
print(short_messages)
