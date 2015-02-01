# template for "Stopwatch: The Game"
import simplegui
# define global variables
tenths  = 0
totalStops = 0
successfulStops = 0
isStopped = True

#seconds = 0
#minutes = 0
#secstring = ''

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #zeros = len(str(t)) - 1
    #tenth = t/(10**zeros)
    m = t/600
    s = t/10
    #remainder = 0
    while s >= 60:
        s -= 60
    if len(str(s))<2:
        seconds = '0'+str(s)
    else:
        seconds = str(s)
    minutes = str(m)
    tenths = str(t)[-1:]
    return minutes+':'+seconds+'.'+tenths 
    pass

"""def format(t):
    global tenths
    global seconds
    global minutes
    seconds = t//10
    minutes = seconds//60
    return seconds, minutes
    pass"""
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler_start():
    global isStopped
    timer.start()
    isStopped = False
    
def button_handler_stop():
    global totalStops, successfulStops, tenths, isStopped
    timer.stop()
    if isStopped == False:
        totalStops += 1
    if str(tenths)[-1:] == '0':
        successfulStops += 1
    isStopped = True

def button_handler_reset():
    global tenths, successfulStops, totalStops, isStopped
    timer.stop()
    tenths = 0
    successfulStops = 0
    totalStops = 0
    isStopped = True

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths
    #global seconds
    """ global minutes
    if tenths == 10:
        seconds += 1
        tenths = 0
    if seconds == 60:
        minutes += 1
        seconds = 0"""
    #print tenths
    tenths += 1
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(tenths), [50,110], 40, 'Red')
    canvas.draw_text(str(successfulStops)+'/'+str(totalStops), [165, 25], 20, 'Green')
    
# create frame
frame = simplegui.create_frame('Stop Watch', 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

start = frame.add_button('Start', button_handler_start, 60)
stop = frame.add_button('Stop', button_handler_stop, 60)
reset = frame.add_button('Reset', button_handler_reset, 60)
# start frame
#print time


frame.start()
#print format(1200)

# Please remember to review the grading rubric
