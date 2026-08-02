while (users_guess) != (number):
    if (users_guess) > (number):
        print("way too high")
        print("guess again")
        users_guess = input(">")
        users_guess = int(users_guess)
    elif (users_guess) < (number):
        print("way too low")
        print("guess again")
        users_guess = input(">")
        users_guess = int(users_guess)
    

print("You guessed the number! It was " + str(users_guess))