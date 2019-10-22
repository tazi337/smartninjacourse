# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

secret = "7"
counter = 1

while True:
    guess = input("Guess the secret number")

    if guess == secret:
        print("Oh, so great!, you won!")
        break
    elif counter > 5:
        print("You Lost!")
        break
    else:
        print("Oh no, please try again.")
        counter += 1
        print(counter)
