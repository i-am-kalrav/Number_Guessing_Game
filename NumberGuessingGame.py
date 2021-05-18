import random

def play(min, max):
    goal = random.randint(min, max)
    guess = max + 2
    tries = 0
    while guess != goal:
        tries += 1
        guess = int(input("Guess an integer between " + str(min) + " and " + str(max) + " (inclusive):\n"))
        if guess < goal:
            print("\nToo low, guess higher.\n")
        elif guess > goal:
            print("\nToo high, guess lower.\n")
    if tries <= max + 1 - min:
        if tries == 1:
            print("Correct! It took you 1 try to guess it.\n")
            print("Accuracy: 100%\n")
        elif tries > 1:
            print("Correct! It took you", tries, "tries to guess it.\n")
            print("Accuracy: " + str(accuracy(tries, max + 1 - min)) + "%\n")
    else:
        print("Low accuracy!\n")

def accuracy(nTries, range):
    return (1 - (nTries - 1) / range) * 100

print("Give the upper and lower bounds integers (inclusive) for the guessing game:")
low = input("Lower bound:\n")
high = input("Upper bound:\n")
again = 'n'
while low != '' and high != '':
    try:
        play(int(low), int(high))
    except:
        print("\nError in input. You can try again.\n")

    again = input("Do you want to play again? [Yes/y or No/n]:\n")
    if again.lower() == 'yes' or again.lower() == 'y':
        print("\nThen give the upper and lower bounds integers (inclusive) for the guessing game:")
        low = input("Lower bound:\n")
        high = input("Upper bound:\n")
    else:
        print("Thanks for playing!")
        exit()