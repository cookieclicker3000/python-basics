#ma taha luua programmi mis kasutab sys.exit() commandi ja töötab nii kaua kuniks kasutaja kirjtab "exit"

import sys

while True:
    print("Kirjuta exit kui tahad väljuda programmist")
    vastus = input(">")
    if vastus == "exit":
        sys.exit()
    print("sa kirjutasid " + vastus + " mitte exit")

    