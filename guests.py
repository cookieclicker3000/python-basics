#tahame kindlat nime saada ja kindlat numbrit. kui nime ei anna küsi uuesti. kui numbrit ei anna lõpeta programm.

name = ""

while not name:
    print("What is your name?")
    name = input(">")
print("How many people are you inviting?")
people_inviting = int(input(">"))
while not people_inviting:
    print("You can not say 0 or a word here")
    print("How many people are you inviting?")
    people_inviting = int(input(">"))
print("We will make sure youre wedding will have enough room to have them all")
print("its done")