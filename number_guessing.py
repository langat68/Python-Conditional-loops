import random   # this is a random python library that has random numbers

secret = random.randint(1,5) # the user is limted to 1 nad 5

guess = None # a special value in python to the the program no value yet

while guess != secret:
    guess = int(input("Guess a random number between 1 and 5 : "))

    if guess < secret:
     print("Too low, try again")

    elif guess > secret:
       print("Too high. try again")

    else :
        print("Locked in!")


