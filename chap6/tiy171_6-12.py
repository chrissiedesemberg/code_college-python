favorite_languages = {
'jen': {
    'programming': 'python',
    'home': 'french'
},
'sarah': {
    'programming': 'c',
    'home': 'english'
},
'edward': {
    'programming': 'ruby',
    'home': 'spanish'
},
'phil': {
    'programming': 'python',
    'home': 'mandarin'
}}

for name, languages in favorite_languages.items():
    person = f"{name}"
    programming = f"{languages['programming']}"
    home = f"{languages['home']}"
    print(f"\n{person.title()} loves to program in {programming.title()} and prefers talking {home.title()}.")
