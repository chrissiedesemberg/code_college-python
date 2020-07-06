languages = ["french", "spanish", "mandarin"]

print(languages[0])
print(languages[-1])

print(f"\nI would like to learn {languages[0]} first\n")

languages[2] = "dutch"
print(languages)

languages.append("zulu")
print(languages)

languages.insert(0, "sotho")
print(languages)

del languages[0]
print(languages)

languages.pop()
print(languages)

languages.pop(1)
print(languages)

languages.remove("dutch")
print(languages)

languages = ["french", "spanish", "dutch"]
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(sorted(languages))
print(languages)

languages.reverse()
print(languages)


