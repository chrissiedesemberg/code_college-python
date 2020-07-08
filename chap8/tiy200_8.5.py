def describe_city(name, country="germany"):
    print(f"\nOne of my top three cities, {name.title()}, is in {country.title()}.")

describe_city("Koln")
describe_city("Edinburg", country="scotland")
describe_city("Ronda", country="spain")
