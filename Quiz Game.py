#####      QUIZ GAME    #######



# Lets setup a questions

Questions = ("Which is the Closest Planet to the sun?: ",
             "Which is the largest planet in the Solar System?: ",
             "Which Planet is called Earth's Twin?: ",
             "Which is the hottest planet in the Solar System?: ",
             "Which is the Natural Satellite of the earth?: ")



# Lets setup an options to select from
        
Options = (("A. Mercury", "B. Venus", "C. Saturn", "D. Earth"),
           ("A. Jupiter", "B. Neptune", "C. Mars", "D. Saturn"),
           ("A. Uranus", "B. Mars", "C. Venus", "D. Jupiter"),
           ("A. Neptune", "B. Mercury", "C. Jupiter", "D. Venus"),
           ("A. Titan ", "B. Ganymede", "C. Moon", "D. Deimos "))


Answers = ("A", "A", "C", "D", "C") 
Guesses = []
Score = 0
question_num = 0


for question in Questions:
    print("------")
    print(question)
    for i in Options[question_num]:
        print(i)


    guess = input("Enter (A,B,C,D): ").upper()
    Guesses.append(guess)

    if guess == Answers[question_num]:
        Score = Score +1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{Answers[question_num]} is the correct answer")    

    question_num = question_num +1

print("------------")
print("     RESULTS     ")
print("------------")


print("Answers: ", end=" ")
for answer in Answers:
    print(answer, end=" ")

print()

print("Guesses: ", end=" ")
for guesses in Guesses:
    print(guesses, end=" " )
print()


score = (Score /len(Questions)*100)

print(f"{score}%")






