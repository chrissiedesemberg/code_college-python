rivers = {
    "Egypt": "Nile",
    "Zambia": "Zambezi",
    "Germany": "Rhein"
}

print("")

for country, river in rivers.items():
    print(f"The {river} runs through the country {country}!")

print("")

for river in rivers.values():
    print(river)

print("")

for country in rivers.keys():
    print(country)

