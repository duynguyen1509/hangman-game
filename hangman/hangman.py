key = "duynguyen"
guesses = ""
turns = 5
count = 0
while turns > 0:
    guess = input("guess a character ")
    if guess in key:
        guesses += guess
    else:
        turns -= 1
        print("Wrong! You have " + str(turns) + " turns left")

    for char in key:
        if char in guesses:
            print(char, end=" ")
            count += 1
        else:
            print("_", end=" ")
    if count == len(key):
        print("you won")
        break
    count = 0
else:
    print("you lose")
    print("the key is: ", key)


