from graph import *
def draw_face(x,y,R,color:str):
    brushColor(color)
    circle(x,y,R)
def draw_eyes(x,y,R,color:str):
    brushColor(color)
    circle(x,y,R)
    brushColor(color)
    circle(x+125,y,R-15)
    brushColor("black")
    circle(x,y,R-R/2)
    brushColor("black")
    circle(x+125,y,R-30)
    

draw_face(250,250,150,"yellow")
draw_eyes(190,215,40,"red")
run()
