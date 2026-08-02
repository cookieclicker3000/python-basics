#EHITA ISESEISVALT KIVI, PABER, KÄÄRID MÄNG.
#1. programm peab kuvama õigeid asju: kiri "ROCK PAPER SCISSORTS ALGUSES" 
#1.1. näitama iga kord palju on võite, kaotusi ja viike. NT  "0 Wins, 0 Losses, 0 Ties"
#1.2. peab näitama käike mida valida ehk: "(r)ock (p)aper (s)cissors or (q)uit"
#1.3. kui valid käigu siis peab ütlema su valiku ehk nt KIVI... läheb vastu ...PAUS...  PABERILE.
#1.4. viimaseks peab kuvama kas oli võit, kaotus või viik.

#programm peab uuendama edetabelit.
#programm peab teadma mis võidab.
#programm peab genereerima enda käigu.




import sys, random




print("ROCK, PAPER, SCISSORS")


tie_count = 0
lose_count = 0
win_count = 0



while True:
    print(str(win_count) + " Wins, " + str(lose_count) + " Losses, " + str(tie_count) + " Ties")

    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    your_move = input(">")

    programmi_käik = [1, 2, 8]
    programmi_käik = random.choice(programmi_käik)

    print("PABER versus...")

    if programmi_käik == 1:
        print("KÄÄRID")

    elif programmi_käik == 2:
        print("PABER")

    elif programmi_käik == 8:
        print("KIVI")



    if your_move == "r":
        r = 8
        vastus = programmi_käik + r
        if vastus == 16:
            print("VIIK!")
            tie_count = tie_count + 1

        elif vastus == 10:
            print("KAOTASID!")
            lose_count = lose_count + 1
        
        elif vastus == 9:
            print("VÕIT!!!")
            win_count = win_count + 1

        
        
        
    elif your_move == "p":
        p = 2
        vastus = programmi_käik + p
        if vastus == 4:
            print("VIIK!")
            tie_count = tie_count + 1

        elif vastus == 3:
            print("KAOTASID!")
            lose_count = lose_count + 1
        
        elif vastus == 10:
            print("VÕIT!!!")
            win_count = win_count + 1
        



        
    elif your_move == "s":
        s = 1
        vastus = programmi_käik + s
        if vastus == 2:
            print("VIIK!")
            tie_count = tie_count + 1

        elif vastus == 9:
            print("KAOTASID!")
            lose_count = lose_count + 1
        
        elif vastus == 3:
            print("VÕIT!!!")
            win_count = win_count + 1

        



    


    rock_võitis = 9
    paper_võitis = 10
    scissors_võitsid = 3
    tie = 16, 4, 2


 