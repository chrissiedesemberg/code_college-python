guests = ["susi", "damon", "christy", "susan"]

cant_come = "susi"
guests.remove(cant_come)
guests.append("william")
print(f"{cant_come.title()} cannot make dinner tonight!")

print(f"Hi there {guests[0].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[1].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[2].title()}, please join us for dinner at our house on Friday!")
print(f"Hi there {guests[3].title()}, please join us for dinner at our house on Friday!")