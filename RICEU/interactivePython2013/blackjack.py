# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
q = ""
score_dealer = 0
score_player = 0

dealer = []
player = []
thisDeck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.show_back = False
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if self.show_back:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def value(self):
        return VALUES[self.rank]

        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.HandList = []
        

    def __str__(self):
        strHand = ""
        for card in self.HandList:
            strHand += str(card) + " "
        return "Hand contains " + strHand	# return a string representation of a hand

    def show_cards(self):
        for card in self.HandList:
            card.show_back = False
            
    def add_card(self, card):
       self.HandList.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust                
        
        handValue = 0 
        hasAce = False
        for card in self.HandList:
            handValue += card.value()
            if card.rank == 'A':
               hasAce = True
        
        if hasAce:        
            if handValue + 10 <= 21:
                handValue += 10
        
        #return handValue
        return handValue
   
    def draw(self, canvas, pos): 
            # draw a hand on the canvas, use the draw method for cards     
        inc = 0
        for card in self.HandList:            
            card.draw(canvas, [pos[0]+inc, pos[1]+inc/5])
            inc += 40 
        
# define deck class 
class Deck:
    def __init__(self):
        self.Deck = []
        for i in SUITS:
            for j in RANKS:
                mycard = Card(i,j)
                self.Deck.append(mycard)
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.Deck)    # use random.shuffle()

    def deal_card(self):
            return self.Deck.pop(0)
            # deal a card object from the deck
    
    def __str__(self):
        strDeck = ""
        for mycard in self.Deck:
                strDeck += str(mycard) + " "
        return "Deck contains " + strDeck
    # return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, thisDeck, q, score_dealer
    outcome = ""
    q = ""
    
    # your code goes here
    thisDeck = Deck()
    thisDeck.shuffle()
    print thisDeck
    
    dealer = Hand()
    player = Hand()
    
    #card 1 for each
    firstCard = thisDeck.deal_card()
    firstCard.show_back = True
    dealer.add_card(firstCard)    
    player.add_card(thisDeck.deal_card())
    
    print "dealer",dealer
    print "player",player
    
    #card 2 for each
    dealer.add_card(thisDeck.deal_card())
    player.add_card(thisDeck.deal_card())
    
    print "dealer", dealer
    print "player", player
    
    if in_play:
        score_dealer +=1
    
    q = "HIT OR STAND?"
    in_play = True
    
    print q
    
    
def hit():
        # replace with your code below
    global in_play, score_dealer, score_player, outcome,q
    # if the hand is in play, hit the player
   
    
    if in_play and player.get_value() <= 21:
        player.add_card(thisDeck.deal_card()) 
        print "ppp", player, player.get_value()
        q = "HIT OR STAND?"
        print q
        
    # if busted, assign a message to outcome, update in_play and score
    
    if player.get_value() > 21:
        print "player", player.get_value()
        print "dealer",dealer.get_value()
        dealer.show_cards()
        outcome = "YOU BUSTED"
        score_dealer += 1
        q = "NEW DEAL?"
        
        print outcome
        print "dealer score", score_dealer 

def stand():
    global in_play, score_dealer, score_player, outcome,q
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    q =""
    
    dealer.show_cards()
    
    if player.get_value() > 21:
        outcome = "YOU BUSTED"
        print outcome
        score_dealer += 1
        in_play = False
        q = "new deal?"
    
    else:
        
        while in_play and dealer.get_value() <= 17:
            dealer.add_card(thisDeck.deal_card()) 
            print "dealer", dealer, dealer.get_value()
        
        if dealer.get_value() > 21:
            outcome = "DEALER BUSTED"
            score_player += 1 
                
            
        elif (player.get_value() <=21) and (player.get_value() > dealer.get_value()):
            print "player", player.get_value()
            print "dealer",dealer.get_value()
            score_player += 1
            outcome = "YOU WON!"
        
        else:
            print "player", player.get_value()
            print "dealer",dealer.get_value()
            score_dealer += 1
            outcome = "DEALER WON"
        
        in_play=False
        
        print outcome
        print "dealer score", score_dealer
        print "player score", score_player
        
        q = "new deal?"
        print q
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global score_player, score_dealer, outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack", (50,50), 45, "White")
    canvas.draw_text("Is luck on your side?", (51,75), 25, "White")
    
    #cards
    dealer.draw(canvas, [100,175])
    player.draw(canvas, [100,400])
    
    canvas.draw_text(outcome, (350,400), 30, "Blue")
    canvas.draw_text(q, (375,425), 25, "White")
    
    #box
    canvas.draw_line((400,10), (585,10), 5, "White")
    canvas.draw_line((400,125), (585,125), 5, "White")
    canvas.draw_line((400,10), (400,125), 5, "White")
    canvas.draw_line((585,10), (585,125), 5, "White")

    #score
    canvas.draw_text("Score", (445,50), 45, "White")
    
    #dealer
    canvas.draw_text("Dealer:", (50,145), 45, "White")
    
    #you
    canvas.draw_text("You:", (50,375), 45, "White")
    
    #keeping score
    canvas.draw_text("Dealer", (410,80), 30, "White")
    canvas.draw_text(str(score_dealer), (440,110), 25, "White")
    
    canvas.draw_text("You", (510,80), 30, "White")
    canvas.draw_text(str(score_player), (540,110), 25, "White")
    

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()



# remember to review the gradic rubric