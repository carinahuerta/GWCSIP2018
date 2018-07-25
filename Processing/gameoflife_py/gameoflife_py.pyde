#alive = False

def setup():
    size (500,500)
    frameRate(3)
    random()
        
def draw():
    stroke (0,0,255)
    for x in range(20):
        for y in range (20):
            fill (0,0,0)
            rect (x *50,y*50, 50,50)
            if array[x][y].alive == True:
                fill (233,0,0)
            if array[x][y].alive == False:
                fill (230,0,230)
            rect (x *50,y*50, 50,50)
    update()
    
class life:
    def __init__ (self, alive, x,y):
        self.alive = alive
        self.x = x
        self.y = y

array = [[0 for i in range (20)] for i in range (20)]

for x in range(20):
    for y in range (20):
        array [x][y] = life (False, x, y)
        
def random():
    from random import randint
    for x in range (20):
        for y in range (20):
            
            l= randint(0,100)
            if (l <= 30):
                array[x][y].alive = True
                
def update():
    for x in range(20):
        for y in range (20):
            sum = 0
            if (x != 19 and y != 19):
                if array[x+1][y+1].alive == True:
                    sum += 1
            if (x !=19 and y !=0):
                if array [x+1][y-1].alive == True:
                    sum +=1
            if (x != 0 and y !=0):
                if array [x-1][y-1].alive == True:
                    sum +=1
            if (x != 0 and y !=19):
                if array [x-1][y+1].alive == True:
                    sum +=1
            if (x !=0):
                if array [x-1][y].alive == True:
                    sum +=1
            if (y != 19):
                 if array [x][y+1].alive == True:
                    sum +=1
            if (x!= 19):
                 if array [x+1][y].alive == True:
                    sum +=1
            if (y != 0):
                 if(array [x][y-1].alive == True):
                    sum +=1
            if(sum < 3 or sum >= 5):
                print(sum)
                array [x][y].alive = False
                print("change")
                
            else:
                array [x][y].alive = True
                print("error")



                    
