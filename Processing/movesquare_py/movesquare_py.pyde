def setup ():
    size (703, 703)
    background (50,0,50)
x=10
dx=10
def draw():
    global x
    global dx
    background (50, 0,50)
    rect (x, 10, 100, 100)
    if(x+10>=703):
        dx=-10
    elif (x<=0):
        dx= 10
