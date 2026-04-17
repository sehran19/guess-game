import random
number = random.randint(1,50)
guess=0
print=("guess a number between 1 to 50")
while guess!=number:
    guess=int(input("enter your guess:"))
    if guess < number:
        print("too low! try again.")
    elif guess > number:
        print("too high!try again.")
    else:
        print("congratulations! you guessed it ")

