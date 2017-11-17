#Hangman Game
#
#11/13/20
#Anders B

#imports
import time
import random 
#Languge
#conditionals
strikes = 0
limit = 6
gameover = 0
result = 0
animals = ["penguin", "panda", "puffin"]
foods = ["pancake", "pineapple", "panini", "pastrami", "pasta" , "pickle", "potato"]
trees = ["palm", "pine"]
def start_screen():
    print ("Welcome to Penguin Games Studios you probably know how this works")
    print()
    time.sleep(1)
    image = input("Wanna see something cool?")
    print()
    image = image.lower()
    if "y" in image:
        print ("Alright!")
        print()
        print()
        time.sleep(.5)
    else:
        print ("Too bad it's too gnarly")
        print()
        print()
        time.sleep(.5)
    print ("__________¶¶_¶¶__¶¶_¶¶_")
    time.sleep(.1)
    print ("_________¶¶_¶¶_¶¶_¶¶_¶¶¶ ")
    time.sleep(.1)
    print ("_____¶¶¶¶¶____________¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("___¶¶¶¶¶_______________¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶¶¶¶¶__________________¶¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶¶¶¶____________________¶¶¶")
    time.sleep(.1)
    print ("___¶¶______________________¶¶¶ ")
    time.sleep(.1)
    print ("___¶________________________¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶¶_____¶¶¶______¶¶________¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶_____¶¶¶¶_____¶¶¶¶¶______¶¶¶¶¶¶_¶ ")
    time.sleep(.1)
    print ("__¶____¶¶¶¶¶____¶¶¶¶¶¶¶¶____¶¶¶¶¶¶__¶ ")
    time.sleep(.1)
    print ("__¶¶__¶¶¶¶¶______¶¶¶¶¶¶¶___¶¶¶¶¶¶¶___¶ ")
    time.sleep(.1)
    print ("___¶__¶¶¶__________¶¶¶¶___¶¶¶¶¶¶¶¶¶___¶ ")
    time.sleep(.1)
    print ("___¶¶____________________¶¶¶¶¶¶¶¶¶¶___¶¶¶ ")
    time.sleep(.1)
    print ("___¶¶¶_____¶¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶")
    time.sleep(.1)
    print ("___¶¶¶¶¶___¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶")
    time.sleep(.1)
    print ("___¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("___¶¶¶¶¶¶¶¶__¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("____¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶ ")
    time.sleep(.1)
    print ("__¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶")
    time.sleep(.1)
    print ("___¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("___________________¶¶¶¶¶¶¶¶¶¶¶ ")
    time.sleep(.1)
    print ("___________________¶¶¶¶¶¶¶¶¶¶ ")
    print()
    print()
    time.sleep(1)

def start_up(limit):
        print ("This is definitely not hangman its 'Shopping Spree!'")
        print()
        print ("You have to spell the word to buy it")
        print()
        print ("You have a total of "  + str(limit) + " strikes then your out, so no this isn't baseball")
        print()

def get_puzzle(animals, foods, trees):
    puzzling = -1
    while puzzling == -1:
        wordbankchoice = input("Please chose from the catagories: 0)Animals 1)Foods 2)Trees ")
        time.sleep(.5)
        print()
        wordbankchoice = int(wordbankchoice)
        
        if wordbankchoice == 0:
            puzzling = 0
            return random.choice(animals)
        elif wordbankchoice == 1:
            puzzling = 0
            return random.choice(foods)
        elif wordbankchoice == 2:
            puzzling = 0
            return random.choice(trees)
        else:
            print("Please chose an option otherwise this is gonna be a long day")
            print()
            time.sleep(.5)

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def display_board(solved,guesses):
    print(solved , "[" + guesses + "]")
    print()

def get_guess():
    while True:
        letter = input("Guess a lonely letter of the alphabet:")
        print()
        time.sleep(.5)

        if len(letter) ==1:
            if(letter).isalpha():
                return letter
            else:
                print("Only letters can be guessed idiot")
                print()
                time.sleep(.5)
        else:
                print("Only one character at a time idiot")
                print()
                time.sleep(.5)

def show_result(result):
    if result == 0:
        print("You probably won")
        print()
        time.sleep(.5)
    else:
        print("You lost I think")
        print()
        time.sleep(.5)
        
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        print()
        time.sleep(.5)
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print()
            time.sleep(.5)

def show_credits():
    print ("Thanks for playing man")
    print()
    time.sleep(1)
    print ("I'm sorry you are aweful at this game")
    print()
    time.sleep(1)
    print ("Maybe, I don't know, try playing iSPY by yourself")
    print()
    time.sleep(1)
    print ("You might actually win")
    print()
    time.sleep(1)
    print ("Anyway this game was made by Anders")
    print()
    time.sleep(1)
    print ("On the 20th of November, 2017")
    print()

    

#Master Function    
def play(strikes,limit,gameover,result):
   

    start_up(limit)
    puzzle = get_puzzle(animals, foods, trees)
    guesses = ""
    solved = get_solved(puzzle,guesses)
    display_board(solved,guesses)

  
    
    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1
            print ("You have " + str(strikes) + " strikes")
            print()
            time.sleep(1)
            if strikes == limit:
                print("Game over loser")
                print()
                time.sleep(1)
                gameover = 1
                result = 1
        
        guesses += letter
        solved = get_solved(puzzle,guesses)
        display_board(solved,guesses)

        
    show_result(result)

    
# Game starts running here
start_screen()

playing = True

while playing:
    play(strikes,limit,gameover,result)
    playing = play_again()

show_credits()

    
