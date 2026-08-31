String = input("Please enter the strings here")
reversed_string = ""

for char in range(len(String)-1,-1,-1):
    reversed_string += String[char]
print(reversed_string)

