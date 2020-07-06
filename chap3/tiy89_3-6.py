guests = ["susi", "damon", "christy", "susan"]

cant_come = guests[0]
guests.remove(cant_come)
guests.insert(0, "william")
print(f"{cant_come.title()} cannot make dinner tonight!")

print(f"Hi there {guests[0].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[1].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[2].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[3].title()}, please join us for dinner at our house on Friday!\n")

#code starts here

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
