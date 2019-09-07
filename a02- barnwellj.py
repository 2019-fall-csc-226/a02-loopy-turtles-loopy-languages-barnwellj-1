import turtle

wn = turtle.Screen()
wn.bgcolor('red')    #sets the background color of the screen to red

turtle.color("magenta")
Jimmy = turtle.Turtle()
Jimmy.pensize(20)

Jimmy.color("purple")
Jimmy.begin_fill()
for i in range(3):
    Jimmy.forward(100)        #draws triangle for eye 1
    Jimmy.left(120)
Jimmy.end_fill()

Billy = turtle.Turtle()         #setting up Billy the turtle
Billy.color("magenta")
Billy.pensize(20)

Billy.penup()
Billy.right(180)
Billy.forward(40)               #Postions billy to the left of Jimmy
Billy.pendown()

Billy.color("purple")
Billy.begin_fill()
for b in range(4):
    Billy.forward(100)          #Billy draws a square for eye 2
    Billy.right(90)
Billy.end_fill()

Charles = turtle.Turtle()       #Creating a new turtle Charles, to draw a smiley face underneath the eyes
Charles.color("black")
Charles.pensize(20)

Charles.penup()
Charles.right(180)
Charles.forward(150)         #positions Charles to draw a half circle
Charles.left(90)
Charles.forward(50)
Charles.pendown()
Charles.speed(0)
for c in range(180):     #charles draws a smiley face
    Charles.left(1)
    Charles.forward(2.5)

Charles.penup()
Charles.forward(190)
Charles.left(90)                                        #tells the user to Have a nice day
Charles.forward(155)
Charles.write("Have a Nice Day!! ",move=False,align='center',font=("Comic Sans",30,("bold","normal")))










wn.exitonclick()








