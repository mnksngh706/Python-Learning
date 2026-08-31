mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.lower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.title())

title_case = mixed_case.title()
print(title_case)

print(title_case.startswith("A"))
print(title_case.endswith("Fire"))


words = mixed_case.split()
print(words)

print(" ".join(words).isalpha())