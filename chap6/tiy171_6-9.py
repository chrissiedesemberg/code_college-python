favorite_places = {
    "Andrew": {
        "Place 1": "Durban Waterfront",
        "Place 2": "Kirstenbosch Gardens",
    },
    "Susan": {
        "Place 1": "Clarens",
        "Place 2": "Rhodes",
    },
    "Denise": {
        "Place 1": "Buffelspoort",
        "Place 2": "Warmbaths",
    }
}

for person, detail in favorite_places.items():
    name = f"{person.title()}"
    first = f"{detail['Place 1']}"
    second = f"{detail['Place 2']}"

    print(f"\n{name.upper()}'s first choice to go would be {first.title()}, then {second.title()}!")

print(f"\n or print as list:")

for person, details in favorite_places.items():
    name = f"{person.title()}"
    first = f"{detail['Place 1']}"
    second = f"{detail['Place 2']}"
    print(f"\n{name.upper()}")
    print(f"{first.title()}")
print(f"{second.title()}")
