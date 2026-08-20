NumberInput = int(input("Enter a number :"))
print("The entered number is : " + str(NumberInput))
savedValue = NumberInput
summed = 0
while NumberInput > 0:
    summed +=NumberInput
    NumberInput -= 1
print("The summed number is : " + str(summed))

