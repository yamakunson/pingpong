import turtle
import random
wn = turtle.Screen()
wn.title("Son's game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0
#Title
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center", font=("Courier",24,"normal"), )

#Paddle 1
paddle_1=turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.penup()
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.goto(-350,0)
#Paddle 2
paddle_2=turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.penup()
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.goto(350,0)
#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

#Funtion
def paddleA_up():
    y=paddle_1.ycor()
    y+=40
    paddle_1.sety(y)
def paddleA_down():
    y=paddle_1.ycor()
    y-=40
    paddle_1.sety(y)
def paddleB_up():
    y=paddle_2.ycor()
    y+=40
    paddle_2.sety(y)
def paddleB_down():
    y=paddle_2.ycor()
    y-=40
    paddle_2.sety(y)
wn.listen()
wn.onkeypress(paddleA_up,"w")
wn.onkeypress(paddleA_down,"s")
wn.onkeypress(paddleB_up,"Up")
wn.onkeypress(paddleB_down,"Down")

while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dy=-random.random()*2/10
        if ball.dx<0.3 :
            ball.dx*=-1.2
        else:
            ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"), )
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dy=random.random()*2/10
        if ball.dx<0.3 :
            ball.dx*=-1.2
        else:
            ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"), )
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<=paddle_2.ycor()+50 and ball.ycor()>=paddle_2.ycor()):
        ball.setx(340)
        if ball.dx<0.3 :
            ball.dx*=-1.2
        else:
            ball.dx*=-1
    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<=paddle_1.ycor()+50 and ball.ycor()>=paddle_1.ycor()):
        ball.setx(-340)
        if ball.dx<0.3 :
            ball.dx*=-1.2
        else:
            ball.dx*=-1
       
