import random

highest = 10
answer = random.randint(1, highest)

guess = 0
while guess != answer:
    print("Please guess a number between 1 and {}: ".format(highest))
    guess = int(input())

    if guess == 0:
        print("Hope you enjoyed the game, come back soon!!!")
        break
    elif guess == answer:
        print("Well Done you guessed correctly")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
