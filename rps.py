import random

def play(x):
    computer =random.choice(['r','p','s'])
    if x==computer:
        return "Tie"
    elif (x=='r' and computer=='s') or (x=='s' and computer=='p') or (x=='p' and computer=='r'):
        return computer, "You won"
    else:
        return computer, "You lost"


print(play(input(f"chose between rock (r), paper (p), scissors (s) :")))

