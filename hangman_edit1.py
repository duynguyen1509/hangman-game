key = "duynguyen" # create your own key
guesses = ""
turns = 3 # number of turns you give your friend
count = 0
typed_character=""

while turns > 0:
    guess = input("guess a character ") # ask your friend to enter a character

    # check if the guess is valid
    while len(guess)>1 : 
        print("the guess is not valid")
        guess = input("please enter again ")

    # show what you have typed
    typed_character += guess 
    print("you typed:")
    for char in typed_character:
        print(char,end="\n")

    if guess in key: # check if the guessed character is true
        guesses += guess
    else:
        turns -= 1
        print("Wrong! You have " + str(turns) + " turns left")

    for char in key: # display of the game
        if char in guesses:
            print(char, end=" ")
            count += 1
        else:
            print("_", end=" ")

    if count == len(key): # check if you already won
        print("you won")
        break
    count = 0
else:
    print("You lose. The key is: ", key)


