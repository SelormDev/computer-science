#secret_number = int(input("Please think of a number between 0 and 100! \n" ))
print("Please think of a number between 0 and 100!")
low_point = 0
high_point = 100
found_guess = False

while (found_guess != True):
    guess = (low_point + high_point) // 2
    print("Is your secret number", end=' ')
    print(guess, end='? \n')
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if check == "h":
        high_point = guess
    elif check == "l":
        low_point = guess
    elif check == "c":
        print("Game over. Your secret number was: ", end=' ')
        print(guess)
        found_guess = True
    else:
        print("Sorry, I did not understand your input.")
