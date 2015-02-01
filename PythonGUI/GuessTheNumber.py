# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random 

store=0
operand=0
secret_number=0
noofguess=0


#helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0,100)
    global noofguess
    noofguess=7
    print "New Game. Range is from 0 to 100"
    print "Number of Remaining Guesses ",noofguess
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print ""
    global secret_number
    secret_number=random.randrange(0,100) 
    global noofguess
    noofguess=7
    print "New Game. Range is from 0 to 100"
    print "Number of Remaining Guesses ",noofguess
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    secret_number=random.randrange(0,1000)     
    global noofguess
    noofguess=10
    print "New Game. Range is from 0 to 1000"
    print "Number of Remaining Guesses ",noofguess
    
    
def input_guess(guess):
    # main game logic goes here	
    global operand
    operand=int(guess)
    global noofguess
    noofguess=noofguess-1
    print "Guess was ",operand
    print "Remaining Guesses ",noofguess
    if noofguess==0:
        print "You ran out of guesses. The Number was ",secret_number
        print ""
        new_game() 
    elif operand>secret_number:
        print "lower"
    elif operand<secret_number:
        print "Higher"
    else:
        print "Correct"
    
    
# create frame
frame=simplegui.create_frame("Guess The Number",200,200)

# register event handlers for control elements and start frame
# frame.add_button("Print ",output,100)
# frame.add_button("swap ",swap,100)

frame.add_button("Range is [0,100) ",range100,200)
frame.add_button("Range is [0,1000) ",range1000,200)

frame.add_input("Enter Guess",input_guess,100)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
