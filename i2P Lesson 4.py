vScore = 75

if vScore >= 50:
    print ("\n Ok, you can pass")

else:
    print("\n U Fail")

vMonth = "September"
vLetter = "e"

if vLetter in vMonth:
    print("There is a letter", vLetter, "in", vMonth)

else:
    print("There is NOT a letter", vLetter, "in", vMonth)

vChoice = input("enter a number from 1 - 3 \n \n")
print()

if vChoice == "1":
    print("Bananas")

elif vChoice == "2":
    print("Apples")

elif vChoice == "3":
    print("Oranges")



vWord = input("Enter a word \n \n")

vWord = vWord.lower()

score = 0

for letter in vWord:
    if letter  == "a":
        score = score + 5
        print(letter, "is worth 5")

    elif letter == "e":
        score = score + 4
        print(letter, "is worth 4")

    elif letter == "i":
        score = score + 3
        print(letter, "is worth 3")

    elif letter == "o":
        score = score + 2
        print(letter, "is worth 2")

    elif letter == "u":
        score = score + 1
        print(letter, "is worth 1")

print ("total score is", score)
