# Number Guessing Game
secret_number = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("You Won")
        break
    elif guess > secret_number:
        print("Too High")
    else:
        print("Too Low")