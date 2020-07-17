from chap8.messages import send_messages

short_messages = [
    "Hi there, champ!",
    "Whatcha doing good-looking?",
    "Catch you later"
]
sent_messages = []

send_messages(short_messages, sent_messages)


print(f"Here are the sent messages: {sent_messages}")
print(f"Here are the short messages: {short_messages}")
