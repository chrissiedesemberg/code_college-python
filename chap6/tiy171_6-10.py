favorite_numbers = {
    "Angie": {
    "first": 14,
    "second": 12
    },
    "John": {
    "first": 23,
    "second": 24
    },
    "Chrissie": {
    "first": 4,
    "second": 3
    },
    "David":{
    "first": 12,
    "second": 40
    },
    "Grace":{
    "first": 2,
    "second": 5
    }
}

for name, number in favorite_numbers.items():
    person = f"{name}"
    first = f"{number['first']}"
    second = f"{number['second']}"
    print(f"\n{person.upper()}")
    print(f"The first choice number is: {first}.\nAnd the second choice number is: {second}.")


