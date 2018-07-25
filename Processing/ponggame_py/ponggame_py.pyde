x_rect = 250
circle_xspeed = 1
circle_yspeed = 1

circle_x = 10
circle_y = 10
circle_xreverse = -10
circle_yreverse = -10
def setup():
    background (217,204,255)
    size (500,500)
    
    

    
def draw():
    global x_rect
    global circle_x
    global circle_y
    global circle_xreverse
    global circle_yreverse
    background (217,204,255)
    fill (255,230,204)
    rect (x_rect, 460, 70, 20)
    if (keyPressed == True and keyCode == RIGHT and x_rect != 430):
        x_rect += 10 
    if (keyPressed == True and keyCode == LEFT and x_rect !=0):
        x_rect -= 10
    ellipse (circle_x, circle_y, 50, 50)
    if(circle_x <= 475 and circle_y <= 475):
        circle_x += circle_xspeed
        circle_y += circle_yspeed
        
    if (x_rect<=circle_x<=(x_rect+70) and circle_y== 460):
        circle_xreverse += circle_xspeed
        circle_yreverse += circle_yspeed

    








    


        
