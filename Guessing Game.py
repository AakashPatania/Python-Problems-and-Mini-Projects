### Python Guessing Game ###

import random 

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("lets begin the Python Guessing game")
print(f"Select the number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input(f"Enter the number between {lowest_num} and {highest_num}: ")

    try:
        guess = int(guess)
        guesses += 1
    except ValueError:
        print("Invalid choice")
        print(f"Please select a number between {lowest_num} and {highest_num}")
        continue

    if guess < lowest_num or guess > highest_num:
        print("The number you guess is out of range, please try again")

    elif guess < answer:
        print("number is low")
    elif guess > answer:
        print("number is high")   
    else:
        print(f"the answer is {answer}")
        print(f"the number of guesses you took {guesses}")
        is_running = False        



