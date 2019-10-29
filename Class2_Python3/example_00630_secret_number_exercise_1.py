# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt


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

