secret = "7"

while True:
    guess = input("Guess the secret number: ")

    if guess == secret:
        print("Oh, so great!, you won!")
        break
    else:
        print("Oh no, please try again.")
