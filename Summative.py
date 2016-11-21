vname = input("""Hello!
Welcome to the MC quiz.
Today you will be quizzed on some general trivia.
Q0) What is your name? \n \n""")

print("Alright", vname, "Let's start")
print("""This quiz has to types of questions. Th first type is multiple choice.
For these questions, you will be provied with 3 options - A, B and C.
To input you answer, simply type A, B or C in UPPER CASE.

The next type will be free answer (not really)
For this, you will have to input the answer as a word. Please use lower case and don't input any punctuation!
Good Luck!""")




print ("""
Q1)  Other than East Timor, what is the only other Roman Catholic Country in Asia?
Remember you can ask for a hint by typing "hint".
""")

vA1 = input()

if vA1 == ("hint"):
    print ("""
This country is in South East Asia. It is made up of over 7,000 Islands.
It was conquered by the Spanish and named after King Phillip II.
It belonged to the United States for a brief amount of time but gained its independence on the July 4, 1946
Now you can take another guess:""")



elif vA1 == ("phillippines"):
    print ("nice!")

else:
    print ("Sorry wrong answer")
