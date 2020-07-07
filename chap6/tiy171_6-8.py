pets = {
    "dog": {
        "Type": "Boston Terrier",
        "Owner": "Chrissie Desemberg",
    },
    "cat": {
        "Type": "cheetah",
        "Owner": "Melissa Heystek",
    },
    "Parrot": {
        "Type": "African Grey",
        "Owner": "Annaretha Coetzee",
    }
}

for animal, detail in pets.items():
    type = f"{detail['Type']}"
    owner = f"{detail['Owner']}"
    print(f"\n{animal.upper()}")
    print(f"Type: {type.title()}")
    print(f"Owner: {owner.title()}")



