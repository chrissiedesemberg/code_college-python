def city_country(city, country, population=""):
    if population:
        location = f"{city.title()}, {country.title()} - population {population}"
    else:
        location = f"{city.title()}, {country.title()}"
    return location


