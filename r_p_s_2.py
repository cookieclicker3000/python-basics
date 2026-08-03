#PRINDI ROCK PAPER SCISSORS


import sys, random




print("ROCK PAPER SCISSORS")

wins = 0
losses = 0
ties = 0


while True: # Main mängu loop
    print("%s Wins %s Losses %s Ties" % (wins, losses, ties))

    while True:   #Mängija valiku loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        mängija_valik = input(">")
        if mängija_valik == "r" or mängija_valik == "p" or mängija_valik == "s":
            break
        elif mängija_valik == "q":
            sys.exit()
        else:
            print("Valida saab ainult r, p, s, q")

    
    #Mängija VALIK
    
    if mängija_valik == "r":
        print("KIVI versus...")
    elif mängija_valik == "p":
        print("PABER versus...")
    elif mängija_valik == "s":
        print("KÄÄRID versus...")

    
    #programmi valik

    programmi_valik = random.randrange(0,3)
    if programmi_valik == 0:
        programmi_valik = "r"
        print("KIVI")
    elif programmi_valik == 1:
        programmi_valik = "p"
        print("PABER")
    elif programmi_valik == 2:
        programmi_valik = "s"
        print("KÄÄRID")

    

    #Võitja arvutamine

    if mängija_valik == programmi_valik:
        print("Viik!")
        ties = ties + 1
    
    elif mängija_valik == "r" and programmi_valik == "p":
        print("Kaotus!")
        losses = losses + 1

    elif mängija_valik == "r" and programmi_valik == "s":
        print("Võit!")
        wins = wins + 1

    elif mängija_valik == "p" and programmi_valik == "r":
        print("Võit!")
        wins = wins + 1

    elif mängija_valik == "p" and programmi_valik == "s":
        print("Kaotus")
        losses = losses + 1

    elif mängija_valik == "s" and programmi_valik == "p":
        print("Võit!")
        wins = wins + 1

    elif mängija_valik == "s" and programmi_valik == "r":
        print("Kaotus!")
        losses = losses + 1
