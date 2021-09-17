import random

def guess(x):
    random_number=random.randint(1,x)

    guess=0

    while guess!= random_number:
        guess=int(input(f"Guess a number betwewn 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    print(f"Yay, congrat. You have guessed the number {random_number } corretly")


def computor_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback=input(f"is {guess} too high (h), too low (l), correct (c)")
        if feedback == 'h' :
            high =guess-1
        elif feedback == 'l':
            low=guess+1
    print(f"The computer guessed the number {guess } corretly")


computor_guess(int(input("What range would you like to guess from starting from 1 :")))
    

guess(int(input("What range would you like to guess from starting from 1 :")))








