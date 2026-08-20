def integer(input):
    endResult = 1

    for item in range(input, 1, -1):
        endResult *=item
    return endResult

print(integer(3))
print(integer(4))
print(integer(5))

