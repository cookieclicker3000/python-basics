#ma mõtlen numbrist mis jääb 1 ja 20 vahele.
#ARVA ÄRA 
#number peab jääma samaks iga programmi algatamisega
#kui kasutaja arvab liiga vähe või liiga palju siis ütle talle seda iga korraga.
#kui kasutaja arvab arvu ära siis ütle talle: tubli, sa arvasid numbri ära x korraga.


import random
number = (random.randint(1,20))
print("I am thinking of a number between 1 and 20")



for guesses_taken in range (1,7):
    tries_left = 7 - guesses_taken
    print("You have " + str(tries_left) + " tries to guess the number!")
    guess = int(input(">"))
   

    if guess > number:
        print("GUESS LOWER!")
    elif guess < number:
        print("GUESS HIGHER!")
    else:
        break

if guess == number:
    print("Good job! The number was " + str(number) + "." + " You guessed it in " + str(guesses_taken) + " tries.")
else:
    print("You Failed!")