# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

secret = "1"
counter = 5

while counter > 0:

    counter -= 1
    guess = input("guess the number")

    if guess == secret:
        print("yes, the guess was right!")
    else:
        print(f"Sorry, thats not correct. Number of further guesses: {counter}")

else:
    print("game over")







secret = "10"
counter = 0

while counter < 5:
    guess = input("Guess the secret number")
    counter += 1

    if guess == secret:
        print("You won!")
        break
    else:
        print("Try again!")

else:
    print("Game Over")

