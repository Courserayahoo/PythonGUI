# implementation of card game - Memory

import simplegui
import random
import math
#CONSTANTS
BACK = [71,96]
FRONT = [73,96]
FRONT_SOURCE = [73,96]
BACK_SOURCE = [71,96]
CARD_IN_ROW = 8
H_ROW = 4
no_img_mode = False
back_img = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png')
front_img = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png')
speed = 4
spin_start = 88
spin = [spin_start] * 16
cards = 2 * range(8)
turns = 0
exposed = []
state = 0
last_choices = []
color = 0#color of cards
# helper function to initialize globals
def new_game():
    global cards, exposed, turns, no_img_mode
    random.shuffle(cards)
    exposed = [False] * 16
    turns = 0
    turn_update()
    state = 0
    no_img_mode = False

# define event handlers
def mouseclick(pos):
    global exposed, last_choices, turns, state
    current = (pos[0] / BACK[0]) + CARD_IN_ROW * (pos[1] / (BACK[1] + H_ROW))
    # add game state logic here
    if exposed[current] == False:
        if state == 0:
            state = 1
            exposed[current] = True
            last_choices.append(current)
        elif state == 1:
            state = 2
            exposed[current] = True
            last_choices.append(current)
            turns += 1
            turn_update()
        else:
            if not cards[last_choices[0]] == cards[last_choices[1]]:
                exposed[last_choices[0]] = False
                exposed[last_choices[1]] = False
            state = 1   
            exposed[current] = True
            last_choices.append(current)
        
        if len(last_choices) > 2:last_choices.pop(0)
    pass
    
def turn_update():
    label.set_text("Turns = %d" % turns)
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global spin, done
    for card in range(16):
        #canvas.draw_line([CARD_WIDTH/2 + (CARD_WIDTH * (card % CARD_IN_ROW)), (CARD_HEIGHT + 5) * (card/CARD_IN_ROW)],\
        #[CARD_WIDTH/2 + (CARD_WIDTH * (card % CARD_IN_ROW)), (CARD_HEIGHT + 5) * (card/CARD_IN_ROW) + CARD_HEIGHT], CARD_WIDTH - 1, "Brown")
        if exposed[card] == False:
            if no_img_mode:
                canvas.draw_line([BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW)],\
                [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), \
                (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]], BACK[0], "Red")    
            else:
                canvas.draw_image(back_img, [BACK_SOURCE[0]/2,BACK_SOURCE[1]/2], BACK_SOURCE,\
                [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)),\
                (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]/2],\
                BACK)
    for card in range(16):
            draw_card(canvas, card)
            #canvas.draw_line([50 + (100 * (card % 8)), 150 * (card/8)],\
            #[50 + (100 * (card % 8)), 150 * (card/8) + 145], CARD_WIDTH, "White")
            #canvas.draw_text(str(cards[card]),[42 + (100 * (card % 8)),\
            #150 * (card/8) + 85], 40, "Black")
def draw_card(canvas, card):
    global speed
    if exposed[card]:
        spin[card] = spin[card] + speed
        curr_card_width = BACK[0] * math.sin(math.radians(spin[card]))
        if no_img_mode:
            spin[card] = 999
        if spin[card] < 270:
            if spin[card] < 180:
                canvas.draw_image(back_img, [BACK_SOURCE[0]/2,BACK_SOURCE[1]/2], BACK_SOURCE,\
                              [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]/2],\
                              [curr_card_width, BACK[1]])
            else:
                canvas.draw_image(front_img, [FRONT_SOURCE[0]/2 + cards[card] * FRONT[0],FRONT_SOURCE[1]/2 + (color * FRONT[1]) + color * (H_ROW/2)], FRONT_SOURCE,\
                              [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]/2],\
                              [math.fabs(curr_card_width), BACK[1]])
        else:
                if no_img_mode:
                    canvas.draw_line([BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW)],\
                [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), \
                (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]], BACK[0], "White")
                    canvas.draw_text(str(cards[card]), [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)) - 8,\
                    (BACK[1] + H_ROW) * (card/CARD_IN_ROW) +  BACK[1]/2 + 8],\
                    32, "Black")
                else:
                    canvas.draw_image(front_img, [FRONT_SOURCE[0]/2 + cards[card] * FRONT[0],FRONT_SOURCE[1]/2 + (color * FRONT[1]) + color * (H_ROW/2)], FRONT_SOURCE,\
                              [BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]/2],\
                              BACK)
                    
                #canvas.draw_line([BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + 5) * (card/CARD_IN_ROW)],\
                #[BACK[0]/2 + (BACK[0] * (card % CARD_IN_ROW)), (BACK[1] + H_ROW) * (card/CARD_IN_ROW) + BACK[1]], BACK[0], "White")
    else:
        spin[card] = spin_start
def cardcolor(input1):
    global color 
    for i in range(4):
        if input1 == str(i):
            color = int(input1)
def cardinrow(input2):
    global CARD_IN_ROW
    if input2 in ['4','8']:
        CARD_IN_ROW = int(input2)	
def noimg():
    global no_img_mode
    no_img_mode = True
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", BACK[0] * CARD_IN_ROW \
                               ,(BACK[1] + H_ROW - 1) * 16/CARD_IN_ROW)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.add_input('Cards color\n0-clubs\n1-spades\n2-hearts\n3-diamonds', cardcolor, 50)
frame.add_button('NO IMG MODE', noimg)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric