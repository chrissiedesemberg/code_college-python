cities = {
    "edinburg": {
        "country": "scotland",
        "population": 100_000,
        "fact": "the city has an underground city level where the foundations were built on."
    },
    "los angeles": {
        "country": "united states of america",
        "population": 3_990_000,
        "fact": "there is a theme park called Knottsberry Farm, which is the birthplace of Snoopy."
    },
    "cologne": {
        "country": "germany",
        "population": 1_061_000,
        "fact": "there are golden plagues on the floor in the streets, which marks where Jewish people lived that died in the war."
    }
}

for city, information in cities.items():
    place = f"{city}"
    country = f"{information['country']}"
    population = f"{information['population']}"
    fact = f"{information['fact']}"
    print(f"\n{city.upper()}")
    print(f"The {city} is in {country.title()} and has a population of {population} and did you that {fact}")
