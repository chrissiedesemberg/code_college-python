favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

new_list = {
    "jen",
    "phil",
    "angela"
}

for name in new_list:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for responding!")
    else:
        print(f"Hi {name.title()}, please take the poll!")

