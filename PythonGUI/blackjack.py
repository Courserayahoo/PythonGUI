import simplegui
import random
 
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
 
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("https://www.dropbox.com/s/75fcadgeewharzg/joker.jpg?dl=1")
 
# initialize some useful global variables
in_play = False
outcome = ""
score = 0
 
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
 
 
# define card class
class Card:
    def __init__(self, suit, rank):
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
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
 
    def __str__(self):
        s = ''
        for c in self.hand:
            s += str(c)
            s += " "
        return s
 
    def add_card(self, card):
        self.hand.append(card)
 
    def hit(self,deck):
        self.add_card(deck.deal_card())
        player.get_value()
        dealer.get_value()
 
    def get_value(self):
        """ count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust"""
        global in_play, message, score
        self.value = 0
        A = 0
        for card in self.hand:
            if card[1] == 'A':
                A += 1
            self.value += VALUES[card[1]]
        if A > 0 and self.value < 12:
            self.value += 10
        if self.value > 21:
            if in_play and (player.value > 21):
                message = "You lose! The computer wins!"
                score -= 1
            in_play = False
        return self.value
 
 
    def draw(self, canvas, pos):
        """draw a hand on the canvas, use the draw method for cards"""
        x = 0
        for card in self.hand:
            card = Card(self.hand[x][0], self.hand[x][1])
            card.draw(canvas, [x * 90 + 50, pos * 200])
            x += 1
 
 
# define deck class
class Deck:
    def __init__(self):
        self.deck = [(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
 
    def shuffle(self):
        random.shuffle(self.deck)
 
    def deal_card(self):
        return self.deck.pop()
 
 
#define event handlers for buttons
def deal():
    global outcome, in_play,deck, hand, dealer, hand_total, player, message, score
    message = "Do you choose to Hit or Stand?"
    if in_play:
        score -= 1
        message = "That's cheating!"
    hand_total = 0
    deck = Deck()
    player = Hand()
    dealer = Hand()
    player.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    dealer.hit(deck)
    in_play = True
 
 
def hit():
    global player, in_play, message
    """if the hand is in play, hit the player"""
    player.get_value()
    if (player.value <= 21) and in_play:
        player.hit(deck)
        if player.value < 21:
            message = "OK. Do you want to Hit again or Stand?"
            """if busted, assign a message to outcome, update in_play and score"""
    else:
        message = "STOP. CLICKING. THAT."
 
 
def stand():
    global value, message, in_play, score
    if in_play == False:
        message = "STOP. CLICKING. THAT."
    else:
        player.value
        message = "Please wait! Computer is making its move..."
        timer.start()
    in_play = False
 
def dealercard():
    global score, message
    if dealer.value < 17:
        dealer.hit(deck)
    elif (player.value > dealer.value) or (dealer.value > 21):
        message = "You win. Congrats! Deal again?"
        score += 1
        timer.stop()
    else:
        message = "Computer Wins. Deal again?"
        score -= 1
        timer.stop()
 
# draw handler
def draw(canvas):
    global dealer, player, message, in_play, score
    scorestring = "Your points are: "
    scorestring += str(score)
    dealer.draw(canvas, 1)
    player.draw(canvas, 2)
    canvas.draw_text(message, [50, 185], 18, "Black")
    canvas.draw_text(scorestring, [480, 555], 14, "Yellow")
    canvas.draw_text("BlackJack Game", [480, 585], 18, "Black")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (88, 249), (70, 94))
 
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Gray")
timer = simplegui.create_timer(1000, dealercard)
 
#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
 
# get things rolling
frame.start()
deck = Deck()
player = Hand()
dealer = Hand()
message = "BlackJack Game.                       Please hit Deal"