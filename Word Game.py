vinput = input("Please input a word:\n\n ")
tries = 0
vlength = len(vinput)
print("The word has", vlength, "letters")
vguess = input("")


while vguess != vinput:
    vguess = input("Guess a letter in the word")
    if vguess in vinput:
        print("Yes, that is in the word.It is in position",vinput.index(vguess))

        vguess = ("Ok,guess the word")

    else:
        print ("That is right!")




