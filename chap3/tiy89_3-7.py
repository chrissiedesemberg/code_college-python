guests = ["susi", "damon", "christy", "susan"]

cant_come = guests[0]
guests.remove(cant_come)
guests.insert(0, "william")
print(f"{cant_come.title()} cannot make dinner tonight!")

print(f"Hi there {guests[0].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[1].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[2].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[3].title()}, please join us for dinner at our house on Friday!\n")

print("Hi there, I have found a bigger table and more people can make it!\n")

guests.insert(0, "gift")
guests.insert(3, "blake")
guests.append("orion")

print(f"Hi there {guests[0].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[1].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[2].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[3].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[4].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[5].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[6].title()}, please join us for dinner at our house on Friday!\n")

#Code starts here

print("Sorry guys, our table wont be here ontime - we can only seat two people\n")

print(f"Hi there {guests[0].title()}, sorry - we cant accommodate you for dinner!")
guests.pop(0)

print(f"Hi there {guests[0].title()}, sorry - we cant accommodate you for dinner!")
guests.pop(0)

print(f"Hi there {guests[0].title()}, sorry - we cant accommodate you for dinner!")
guests.pop(0)

print(f"Hi there {guests[0].title()}, sorry - we cant accommodate you for dinner!")
guests.pop(0)

print(f"Hi there {guests[0].title()}, sorry - we cant accommodate you for dinner!\n")
guests.pop(0)

print(guests)

print(f"\nGreat news, {guests[0].title()} and {guests[1].title()}, you can still come to dinner! See you Friday")

del guests[1]
del guests[0]
print(guests)
