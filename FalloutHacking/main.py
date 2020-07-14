from random import randint
diff1 = ["car", "cat", "hat", "how", "bee", "bar"]
diff2 = ["birch", "perch", "peach", "power", "cower", "touch", "break", "creek"]
diff3 = ["scorpion", "flogging", "croppers", "migraine", "footnote", "refinery", "vaulting", "vicarage", "protract", "descents"]


def diff_select(userdiff):

    if userdiff == "3":
        return diff3
    elif userdiff == "2":
        return diff2
    elif userdiff == "1":
        return diff1

def print_words(difflist):
    for x in difflist:
        print (x.upper())

def word_guess():
    guess = str(input("Guess Password: "))
    return guess

def check_words(guess, password):
    letter_matches = 0
    for i in range(0, len(password)):
        if guess[i] == password[i]:
            letter_matches += 1

    print (str(letter_matches) + "/" + str(len(password)) + " Correct")
    return letter_matches

def run():
    user_select = str(input("Select Game Difficulty (1-3): "))
    difficulty = diff_select(user_select)
    randnum = randint(0, len(difficulty) - 1)
    guesses = 0
    secret_pw = difficulty[randnum]
    #print ("Secret Password! " + secret_pw + '\n')
    print_words(difficulty)

    while True:
        curr_guess = word_guess()
        check_words(curr_guess, secret_pw)
        guesses += 1
        if curr_guess == secret_pw:
            print ("Password Accepted: System Unlocked")
            break
        if guesses == 3:
            print ("Access Denied")
            break

def main():
    play = True
    while play:
        run()
        play = 'y' in input("Play Again? (y/n)").lower()

if __name__ == '__main__':
    main()
