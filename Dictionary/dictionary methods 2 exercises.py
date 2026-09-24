consonants = {}.fromkeys("bcdefghijklmnopqrstuvwxyz", "consonant")  //One way

for key,value in consonants.items():
    print(key, value)


for key, value in {}.fromkeys("bcdefghijklmnopqrstuvwxyz", "consonant").items(): //2nd direct way
    print(key, value)