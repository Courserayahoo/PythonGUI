import simplegui
import math

# define global variables
interval = 10
position = [250,250]
mil_sec =0 
sec = 0
mins = 0
t=0
sec_string=str(0)
sec1=0
sec2=0
sec3=0
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(val):
    sec1=val%10
    sec2=val/10
    sec3=0
    if sec2>=60:
        while sec2>=60:     
            sec2=sec2-60
            sec3=sec3+1
    if sec2>=0 and sec2<=9:
        sec2=str(0)+str(sec2)
    return str(sec3)+":"+str(sec2)+"."+str(sec1)  

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    timer.stop()
    global t
    t = 0

def draw(canvas):
    canvas.draw_text(format(t),position,24,"White")
    canvas.draw_text("Scores",[350,60],20,"Red")

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t+1

# create frame
frame = simplegui.create_frame( "Stop Watch Game " , 500 , 500)
timer = simplegui.create_timer(interval,tick)

# register event handlers
frame.set_draw_handler(draw)
startButton = frame.add_button("Start", start)
stopButton = frame.add_button("Stop", stop)
resetButton = frame.add_button("Reset", reset)

# start timer and frame
frame.start()

"""def format(t):
    global mil_sec
    global sec
    global mins 
    global sec_string
    mins = 0 
    mil_sec = (t %10)
    sec = (t-mil_sec )//10 
    sec, mins = sec % 60 ,sec // 60 
    if mil_sec > 9 :
        mil_sec = 0 
        sec = sec + 1 
    if( sec > 59): 
        mins = mins + 1
        sec = sec-60 
        sec_string = str(sec) 
    if len(str(sec)) == 1:
        sec_string = "0"+str(sec)
        
    return str(mins)+":"+sec_string +"."+str(mil_sec) """