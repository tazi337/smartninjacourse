limit = 3
counter = 0
secret = "7"

while counter < limit:
    guess = input("Guess the secret number: ")
    if guess == secret:
        print("Great!!!!")
        break
    else:
        print("Oh no, please try again")
    counter += 1

print("Game Over")
