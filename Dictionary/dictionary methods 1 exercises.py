dictionary = {"Queen": "Bohemian Rhapsody",
              "Bee Gees": "Stayin' Alive",
              "U2": "One",
              "Michael Jackson": "Billie Jean",
              "The Beatles": "Hey Jude",
              "Bob Dylan": "Like A Rolling Stone"}
print(len(dictionary))

for key in dictionary.keys():
    print(key)

print(dictionary.values())

for key, value in dictionary.items():
    print(key)

print(dictionary.get("U2", "Nice song"))
print(dictionary.get("Alan", "Not in the Library"))

