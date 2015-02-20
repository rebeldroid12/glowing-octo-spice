# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math


# initialize global variables used in your code
secret = 0
user = 0
counter = 0
is_Range100=True

# helper function to start and restart the game
def new_game():
    global secret 
    global user
    global counter
    global is_Range100
   
    
    #print "New game. Range is from 0 to 100"
    #print "Number of remaining guesses is", counter 
    #print ""
    if is_Range100:
        return range100()
    else:
        return range1000()
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret
    global counter
    global is_Range100
    secret=random.randrange(0,100)
      
    counter = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", counter 
    print ""
    is_Range100=True
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret
    global counter
    global is_Range100
    secret=random.randrange(0,1000)
    
    counter = 10
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", counter 
    print ""
    is_Range100=False
    
def input_guess(guess):
    # main game logic goes here	
    global secret
    global counter
    user = float(guess)
    print "Guess was ", user
    #return user
    
    if  user < secret:
        print "Higher!"
        print ""
        counter = counter - 1
        
        if counter > 0:
            print "Number of remaining guesses is", counter
            print ""
            
        else:
            print "You ran out of guesses. The number was", secret    
            print ""
            new_game()
           
            
    elif user > secret:
        print "Lower!"
        print ""
        counter = counter - 1
        
        if counter > 0:
            print "Number of remaining guesses is", counter
            print ""
        else:
            print "You ran out of guesses. The number was", secret    
            print ""
            new_game()
            
        
    elif user == secret:
        print "Correct!"
        print ""
        new_game()
        
        
    else:
        print "error!"
        print ""
 
    
# create frame
frame = simplegui.create_frame("Guess the number!", 300,300)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess!",input_guess, 200)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
