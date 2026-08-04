
import random



print("Terekest! Mõtle number 1-100 ja ma arvan selle ära!")
pakutud_number = input("Mõtlen numbrile...")

min = 1
max = 100


random_number = random.randint(1,100)
print("Kas su number on " + str(random_number) + "?")
vastus = input("")

while True:  #MAIN MÄNGU LOOP
    if vastus == "ei":
        print("Kas pakkusin liiga (k)õrgele või (m)adalale)?")
        vastus = input(">")

        if vastus == "k":
            max = random_number - 1
            max = (min + max) / 2
            print(int(max))
            if
        

        elif vastus == "m":
            print("jou")
            
          


    elif vastus == "jah":
        print("Ma ütlesin, et arvan numbri ära.")
        break



