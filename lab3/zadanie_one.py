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
    
def draw_mouth(x,y,x2,y2,color="black"):
    brushColor(color)
    rectangle(x,y,x2,y2)
#def draw_eyebrows(x,y,x2,y2,color="black"):     FIXME
  #  brushColor(color)
   # rectangle(x,y,x2,y2)
draw_face(250,250,150,"yellow")
draw_eyes(190,215,40,"red")
draw_mouth(190,330,315,350)
#draw_eyebrows(100,150,230,205)
run()

