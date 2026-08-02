while True:
    print("What is your name?")
    name = input(">")
    if name != "kevin":
        continue
    print("Hello, kevin. What is your password? (its your favourite open world game")
    password = input(">")
    if password == "elden ring":
        break
print("Welcom back Sir.Kevin!")