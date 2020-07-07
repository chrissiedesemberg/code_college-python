places = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for place in places:
    if place >= 4:
        print(f"{place}th")
    elif place == 3:
        print(f"{place}rd")
    elif place == 2:
        print(f"{place}nd")
    else:
        print(f"{place}st")

