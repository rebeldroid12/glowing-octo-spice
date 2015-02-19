# template for "Stopwatch: The Game"
import simplegui


# define global variables
tposition = [100,150]

wins = 0
trials = 0
sposition = [240,30]

interval = 100 #0.01 second
seconds = 0



# define helper function format that converts time
# in tenths of seconds into formatted string A:B.C
"""a:B.c"""
def format(t): 
    # Check if it's in a minute
    c = t % 10
    b = (t / 10) % 60
    a = (t / 600)    
    return "%d:%02d.%d" % (a, b, c)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    watch.start()


def stop():

#calculating wins vs trials
    global trials,wins,seconds
    if watch.is_running():
        watch.stop()
        trials = trials + 1
   
    global seconds
    if (seconds % 10 == 0):
           wins = wins + 1

def reset():    
    global wins, trials, seconds
    watch.stop()    
    wins = 0
    trials = 0
    seconds = 0
    

# define event handler for timer with 0.1 sec interval
def timer():
    global seconds   
    seconds= seconds +1
    
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(seconds), tposition, 50, "White")
    canvas.draw_text(str(wins)+"/"+str(trials), sposition, 25, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300,300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
watch = simplegui.create_timer(interval, timer)

# start frame
frame.start()


# Please remember to review the grading rubric
