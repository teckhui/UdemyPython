for index, character in enumerate("abcdefgh"): #shorthand to unpack from tuple
     print(index, character)

for t in enumerate("abcdefgh"): #unpack and save as tuple that enumerate creates
    index,character = t
    print(t)

index, character = (0,'a')
print(index)
print(character)