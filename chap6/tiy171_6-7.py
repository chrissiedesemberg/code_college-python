people = {
    "mom":{
        "first_name": "Val",
        "last_name": "Uys",
        "age": 52,
        "city": "Pretoria"
    },
    "dad": {
        "first_name": "Peter",
        "last_name": "Uys",
        "age": 67,
        "city": "Pretoria"
         },
    "sister": {
        "first_name": "Melissa",
        "last_name": "Heystek",
        "age": 34,
        "city": "Menlyn"},
    "me": {
        "first_name": "Chrisse",
        "last_name": "Desemberg",
        "age": 34,
        "city": "Centurion"}
}

for person, details in people.items():
    relationship = f"{person}"
    full_name = f"{details['first_name']} {details['last_name']}"
    age = f"{details['age']}"
    city = f"{details['city']}"
    print(f"\nRelationship: {relationship.upper()}")
    print(f"Full name: {full_name.title()}")
    print(f"Age: {age.title()}")
    print(f"City: {city.title()}")
