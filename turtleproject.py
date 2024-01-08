import turtle
import random
#import random library to put waves in the random position in the river
# Make a window and a turtle. These will be global
window = turtle.Screen()
turtle.tracer(False)
window.title('The happy guy by Mark and Mykyta')
t = turtle.Turtle() # t is the traditional name
window.bgcolor("aqua")
t.penup()
t.goto (90,100)
t.pendown()
#begin making sun

t.pen(pencolor="orange", fillcolor="yellow", pensize=5, speed=15)
t.begin_fill()
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.circle(80,45)
t.right(90)
t.forward(40)
t.backward(40)
t.left(90)
t.end_fill()
t.penup()
t.goto(-110,100)
t.pendown()
#creating the first cloud by placing multiple circles in close proximity to eachother
# created by Mark
t.pen(pencolor="white", fillcolor="white", pensize=3, speed=15)
t.begin_fill()
t.circle(50)
#first circle
t.end_fill()
#moving to new position
t.penup()
t.forward(50)
t.right(90)
t.forward(20)
t.left(90)
t.pendown()
t.begin_fill()
t.circle(50)
#second cirlce
t.end_fill()
t.penup()
#moving to next position
t.right(180)
t.forward(110)
t.right(180)
t.pendown()
t.begin_fill()
t.circle(50)
#third cicle
t.end_fill()
t.penup()
#moving turtle to next pos
t.forward(40)
t.pendown()
t.begin_fill()
t.circle(20)
#fourth circle
t.end_fill()
t.penup()
#moving turtle to next pos
t.forward(20)
t.pendown()
t.begin_fill()
t.circle(20)
#fifth circle
t.end_fill()
t.penup()
#moving turtle to last pos
t.forward(20)
t.pendown()
t.begin_fill()
t.circle(20)
#sixth circle
t.end_fill()
t.penup()
#creating function for clouds and setting each cordinate by using the pre-existing cloud created above
#Created by Mark
def makeClouds(t,x,y):
    t.goto(x,y)
    t.pen(pencolor="white", fillcolor="white", pensize=3, speed=0)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.right(180)
    t.forward(110)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.forward(40)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
# all cloud positions using the x and y positions on the drawing chart
makeClouds(t,-200,200)
makeClouds(t,200,200)
makeClouds(t,250,50)
makeClouds(t,-400,300)
makeClouds(t,400,300)
#going to first tree pos
t.goto(-280,-200)
t.left(90)
#creating tree function by using an if statment and a reacution to create the branches then chosing colour and size repeating the process 10 times.
# Created by Mark
def tree(i):
    if i<10:
        return
    else:
        t.speed(0)
        t.forward(i)
        t.left(20)
        tree(3*i/4)
        t.right(40)
        tree(3*i/4)
        t.left(20)
        t.pen(pencolor="green", fillcolor="green", pensize=4, speed=0)
        t.begin_fill()
        t.circle(4)
        t.end_fill()
        t.pencolor("burlyWood")
        t.backward(i)
t.pendown()
#first tree placement- by Mark
tree(50)
t.penup()
t.end_fill()




#code section made by Mykyta
t.right(90)
#move to the grass position
t.goto(0,0)
t.penup()
t.forward(750)
t.right(90)
t.forward(175)
#start filling in the grass
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(215)
t.right(90)
t.forward(1500)
t.right(90)
t.forward(215)
t.right(90)
t.forward(1500)
t.end_fill()
t.penup()
#go to position where guy's head is going to be located
t.right(180)
t.forward(1200)
t.right(90)
t.forward(100)
#draw a guy's head
t.pendown()
t.pencolor("black")
t.fillcolor("LightSalmon")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()
#setup the cursor for the body
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
#make the main body
t.pendown()
t.fillcolor("DodgerBlue3")
t.begin_fill()
t.right(90)
t.forward(30)
t.left(90)
t.forward(100)
t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.end_fill()
#go to the left leg positions
t.forward(30)
t.left(90)
t.forward(100)
#draw left leg
t.begin_fill()
t.fillcolor("gray60")
t.forward(80)
t.left(90)
t.forward(20)
t.left(90)
t.forward(80)
t.left(90)
t.forward(20)
t.end_fill()
#move onto position of the right leg
t.left(180)
t.forward(40)
t.right(90)
#draw the right leg
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(20)
t.left(90)
t.forward(80)
t.left(90)
t.forward(20)
t.end_fill()
#move onto shoulder position
t.fillcolor("DodgerBlue3")
t.begin_fill()
t.left(180)
t.forward(20)
t.left(90)
t.forward(100)
#draw the right shoulder
t.right(135)
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(45)
t.end_fill()
#go to the positon of the right arm
t.right(135)
t.forward(10)
#draw right arm
t.fillcolor("LightSalmon")
t.begin_fill()
t.right(45)
t.forward(60)
t.left(90)
t.forward(14)
t.left(90)
t.forward(74)
t.left(135)
t.forward(20)
t.end_fill()
#go to left side of the shoulder
t.right(90)
t.forward(10)
t.right(45)
t.forward(28)
t.left(90)
t.forward(60)
t.left(90)
t.forward(28)
t.right(135)
#draw the left shoulder
t.fillcolor("DodgerBlue3")
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(45)
t.forward(28)
t.end_fill()
#go to the position of the lef arm
t.right(135)
t.forward(30)
t.right(45)
#draw the left arm
t.fillcolor("LightSalmon")
t.begin_fill()
t.forward(74)
t.right(90)
t.forward(14)
t.right(90)
t.forward(60)
t.right(45)
t.forward(20)
t.end_fill()

#face

#function to draw eye, basically drawing a straight vertical line length of 10 of black color. Function takes  x and y cordinate as parameters
def draweye(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pen(pensize=4)
    t.setheading(90)
    t.forward(10)
    t.penup()
#draw left eye
draweye(t,-482.0,-69.0)
#draw right eye
draweye(t,-466.0,-69.0)

#draw the smile(it's a half circle)
t.setheading(270)
t.goto(-480,-80)
t.pendown()
t.circle(7,180)
t.penup()

t.pensize(1)
#code for the river
#go to the positon of the left border of the river
t.goto(100,-177.0)
t.fillcolor("cyan2")
t.begin_fill()
#to make a river's border i used 7 circles with extent to 70 degrees which will result in wave line
#border of the right side of the river
t.pendown()
t.setheading(358)
t.circle(-100,70)
t.circle(100,70)
t.circle(-100,70)

#go the place for the second border
t.setheading(180)
t.forward(300)

#draw the left border of the river
t.setheading(178)
t.circle(-100,70)
t.circle(100,70)
t.circle(-100,70)

t.setheading(0)
t.forward(300)
t.end_fill()
#the river is ready
t.penup()

t.pencolor("blue")

#function for little waves, which are basically two circles with extent of 70 which together form a little "wave"
def wave(xcord, ycord):
    t.goto(xcord,ycord)
    t.pendown()
    t.setheading(358)
    t.circle(-20, 70)
    t.circle(20, 70)
    t.penup()

#create some waves manually
wave(-93.0,-217.0)
wave(-63.0,-197.0)
wave(266.0,-331.0)
wave(-145.0,-195.0)
wave(186.0,-339.0)
wave(331.0,-354.0)
#make waves in random places inside the river
for i in range(10):
    xcord = random.randint(-20,180)
    ycord = random.randint(-332,-176)
    wave(xcord,ycord)

#function of a stone, consists of a 3/4 of circle on the right side, and then a smaller half circle on the left side
def stone(xcord =0, ycord=0):
    t.goto(xcord,ycord)
    t.pendown()
    t.fillcolor("azure3")
    t.begin_fill()
    t.setheading(0)
    t.circle(15,245)
    t.circle(-15,45)
    t.circle(7.5,180)
    t.setheading(0)
    t.forward(abs(xcord-t.xcor()))
    t.penup()
    t.end_fill()


    t.left(90)
    t.forward(20)
    t.right(90)

    t.pensize(1)
    t.fillcolor("azure4")
    t.begin_fill()
    t.pendown()
    t.circle(3)
    t.end_fill()
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.right(90)
    t.penup()
    t.forward(18)
    t.pendown()
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.penup()





#draw some stones across the river's border
t.pencolor("black")
t.pensize(3)
stone(-193.0,-197.0)
stone(-149.0,-236.0)
stone(-57.0,-263.0)
stone(-18.0,-307.0)
stone(10.0,-363.0)
stone(112.0,-179.0)
stone(167.0,-202.0)
stone(192.0,-249.0)
stone(227.0,-294.0)
stone(323.0,-327.0)


#print hello world in the river
#H
t.pencolor("cyan4")
t.goto(-96.0,-209.0)
t.pendown()
t.setheading(90)
t.forward(20)
t.right(180)
t.forward(10)
t.left(90)
t.forward(10)
t.left(90)
t.forward(10)
t.right(180)
t.forward(20)
t.penup()

#E
t.setheading(45)
t.goto(-32.0,-231.0)
t.pendown()
t.forward(10)
t.backward(10)
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.backward(10)
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.penup()

#L
t.setheading(135)
t.goto(27.0,-215.0)
t.pendown()
t.right(90)
t.forward(20)
t.left(90)
t.forward(10)
t.penup()

#L
t.setheading(90)
t.goto(68.0,-247.0)
t.pendown()
t.right(90)
t.forward(20)
t.left(90)
t.forward(10)
t.penup()

#O
t.setheading(60)
t.goto(132.0,-250.0)
t.pendown()
t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.penup()
t.forward(30)
#W

t.goto(24.0,-285.0)
t.pendown()
t.setheading(280)
t.forward(22)
t.left(150)
t.forward(22)
t.right(150)
t.forward(22)
t.left(150)
t.forward(22)
t.penup()


#O
t.goto(64.0,-335.0)
t.pendown()
t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.penup()

#R
t.goto(121.0,-312.0)
t.pendown()
t.left(90)
t.forward(20)
t.right(90)
t.circle(-5,180)
t.setheading(315)
t.forward(12)
t.penup()

#L
t.goto(175.0,-341.0)
t.pendown()
t.left(90)
t.forward(20)
t.backward(20)
t.right(90)
t.forward(10)
t.penup()


#D
t.setheading(30)
t.goto(237.0,-346.0)
t.pendown()
t.forward(20)
t.right(90)
t.circle(-10,180)
t.penup()

#go to flowers position
t.goto(376.0,-238.0)
t.setheading(90)

#left part of the flower, recursion: draws a line, then goes back a bit, turns onto a small angle and repeats the process in total of 7 times
#after the left side of the flower is painted, the cursor goes back to where it started drawing flower
def leftflower(i, color):
    if i == 0:
        return
    else:
        t.forward(20)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(-3)
        t.end_fill()
        t.backward(10)
        t.left(25)
        leftflower(i-1, color)
        t.right(25)
        t.backward(10)

#right part of the flower, same functionality as on the left side, but the angle turns right this time
def rightflower(i, color):
    if i ==0:
        return
    else:
        t.forward(20)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.backward(10)
        t.right(25)
        rightflower(i - 1, color)
        t.left(25)
        t.backward(10)

#function that draws flower in designated x and y corrdinate, with a choice for a base color and choice for the color of the circles
def flower(xcord, ycord,basecolor, ccolor):
    t.goto(xcord,ycord)
    t.pencolor(basecolor)
    t.pendown()
    leftflower(7, ccolor)
    rightflower(7, ccolor)
    t.penup()
#draw flowers
flower(531.0,-226.0,"orange","white")
flower(640.0,-328.0, "grey", "cyan")
flower(451.0,-306.0, "DarkKhaki","DarkMagenta")
flower(-125.0,-332.0,"DarkGoldenRod1", "DarkSeaGreen1")
flower(-263.0,-240.0, "bisque", "brown2")
flower(-450.0,-330.0, "chocolate1", "DarkOrchid1")
flower(-600,-270,"DarkRed", "aquamarine2")
#end of the code section created by Mykyta





#setting the second tree's position by usuing x and y cordinates.- by Mark
t.goto(200,-200)
t.pendown()
tree(50)
t.penup()

# sentence in text, augutana offers best cs lab in canada - by Mark
t.goto(-150,300) #setting pos
t.pen(pencolor="dark violet", fillcolor="dark violet", pensize= 7)
t.pendown()
t.write("Augustana Offers the Best Comp Sci Lab in Canada", align="center", font=("pacifico", 35, "bold" ))
# turtle writes text controlling the font and the font size









turtle.tracer(True)
def buttonclick(x, y):
    print("You clicked at this coordinate({0},{1})".format(x, y))
# onscreen function to send coordinate
turtle.onscreenclick(buttonclick, 1)
while True:
    t.pendown()
    t.penup()

window.exitonclick()
















