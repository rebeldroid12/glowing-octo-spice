import random

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0:
      #  name = "rock"
        return "rock"
    
    elif number == 1:
      #  name = "Spock"
        return "Spock"
    
    elif number == 2:
      # name = "paper"
       return "paper"
    
    elif number == 3:
      # name = "lizard"
       return "lizard"
        
    elif number == 4:
      # name = "scissors"
       return "scissors"
    
    else:
        print "not a number! error!"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
################################################works######
    
def name_to_number(name):
    # fill in your code below

      if name == "rock":
       # number = 0
        return 0
    
      elif name == "Spock":
       # number = 1
        return 1
    
      elif name == "paper":
        # number = 2
        return 2
    
      elif name == "lizard":
       # number = 3
        return 3
        
      elif name == "scissors":
       # number = 4
        return 4
    
      else:
        print "not a name! error!"
    
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
################################################works######
    

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    
    diff = (player_number - comp_number) % 5

    
    # use if/elif/else to determine winner
    if (diff == 1) or (diff == 2):
        winner = "Player"
    
      
    elif (diff == 3) or (diff == 4): 
        winner = "Computer"
    
   
    else: 
        print "error in the diffs!"        
        
  
    # convert comp_number to name using number_to_name
    
    comp = number_to_name(comp_number)
    
    # print results
    print " "
    print "Player chooses ", number_to_name(player_number)
    print "Computer chooses ", comp
    print  winner, " wins!"
    
  
    
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
