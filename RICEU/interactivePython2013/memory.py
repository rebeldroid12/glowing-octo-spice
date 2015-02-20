# implementation of card game - Memory

import simplegui
import random

deck = range(8)*2
exposed = []
state = 0
card1 = 0 
card2 = 0
counter = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, counter
    state = 0
    counter = 0
    random.shuffle(deck)
    exposed = [False] * 16
    label.set_text(counter)



    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card1, card2, counter
    clicked_card = pos[0] // 50 
    if not exposed[clicked_card]:
        if state == 0:
            state = 1
            card1 = clicked_card
        
        elif state == 1:
            # We got 1 card exposed
            state = 2
            card2 = clicked_card
            
        elif state == 2:
            # We got 2 cards exposed
            state = 1
            counter += 1
            if deck[card1] == deck[card2]:      
                if not exposed[clicked_card]:
                    exposed[card1] = True
                    exposed[card2] = True
            else:    
                exposed[card1] = False
                exposed[card2] = False
            card1 = clicked_card
    
    exposed[clicked_card] = True
    label.set_text(counter)
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    space = 10
    for pos in range(16):
        canvas.draw_text(str(deck[pos]), (space,80), 65, "White") 
        canvas.draw_line((space-10,0), (space-10,100), 2, "Red")        
        if not exposed[pos]: 
            #draw green card over
           canvas.draw_line((space+15,0), (space+15,100), 45, "Green")           
        space += 50                         
        
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
label.set_text("Turns = " + str(counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric



#-----------------------------------

# implementation of card game - Memory

# import simplegui
# import random

# deck = range(8)*2
# exposed = []
# state = 0
# card1 = 0 
# card2 = 0

# # helper function to initialize globals
# def new_game():
#     global deck, exposed
#     state = 0
#     random.shuffle(deck)
#     exposed = [False] * 16
#     print deck

    
# # define event handlers
# def mouseclick(pos):
#     # add game state logic here
#     global state, card1, card2
#     #print pos
#     clicked_card = pos[0] // 50
#     #print clicked_card
#     #exposed[clicked_card] = True
    
#     if not exposed[clicked_card]:
#         if state == 0:
#             state = 1
#             card1 = clicked_card
        
#         elif state == 1:
#             # We got 1 card exposed
#             state = 2
#             card2 = clicked_card
            
#         elif state == 2:
#             # We got 2 cards exposed
#             state = 1                
#             if deck[card1] == deck[card2]:
#                 print "match"
#                 if not exposed[clicked_card]:
#                     exposed[card1] = True
#                     exposed[card2] = True
#             else:    
#                 exposed[card1] = False
#                 exposed[card2] = False
#             card1 = clicked_card
    
#     exposed[clicked_card] = True
        
# # cards are logically 50x100 pixels in size    
# def draw(canvas):
#     space = 10
#     for pos in range(16):
#         canvas.draw_text(str(deck[pos]), (space,80), 65, "White") 
#         canvas.draw_line((space-10,0), (space-10,100), 2, "Red")        
#         if not exposed[pos]: 
#             #draw green card over
#            canvas.draw_line((space+15,0), (space+15,100), 45, "Green")           
#         space += 50                         
        
        
# # create frame and add a button and labels
# frame = simplegui.create_frame("Memory", 800, 100)
# frame.add_button("Restart", new_game)
# label = frame.add_label("Turns = 0")

# # register event handlers
# frame.set_mouseclick_handler(mouseclick)
# frame.set_draw_handler(draw)

# # get things rolling
# new_game()
# frame.start()