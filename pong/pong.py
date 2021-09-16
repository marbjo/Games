import turtle

image = "crop.gif"
turtle.register_shape("crop.gif")

#Screen
wn = turtle.Screen()
wn.title("Pong by Markus")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Objects

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("crop.gif")
ball.shapesize(stretch_wid=0.01, stretch_len=0.01)
#ball.shape("crop.jpg")
ball.color("green")
#ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0,0)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 ||| Player 2: 0", align="center",font=("courier", 24, "normal"))

#Score
score_a = 0
score_b = 0

def move_a_up():
    y = paddle_a.ycor()
    if y<240:
        y += 30
        paddle_a.sety(y)

def move_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 30
        paddle_a.sety(y)

def move_b_up():
    y = paddle_b.ycor()
    if y<240:
        y += 30
        paddle_b.sety(y)

def move_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 30
        paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkey(move_a_up, 'w')
wn.onkey(move_a_down, 's')

wn.onkey(move_b_up, 'Up')
wn.onkey(move_b_down, 'Down')

x_vel = 0.05
y_vel = -0.05

#Main game loop
while True:

    #AI can't be beat LOL
    #paddle_b.sety(ball.ycor())

    #ball movement
    ball.setx(ball.xcor() + x_vel)
    ball.sety(ball.ycor() + y_vel)

    #Roof or floor collision
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        y_vel = -y_vel

    #Paddle A collision
    if abs(ball.xcor() - paddle_a.xcor()) < 0.01 and abs(ball.ycor() - paddle_a.ycor()) < 100:
        x_vel = -x_vel

    #Paddle B collision
    if abs(ball.xcor() - paddle_b.xcor()) < 0.01 and abs(ball.ycor() - paddle_b.ycor()) < 100:
        x_vel = -x_vel

    #Ball reset
    if ball.xcor() < -400:
        ball.goto(0,0)
        #Scorer has to catch ball first
        x_vel = -x_vel

        score_b += 1
        pen.clear()
        pen.write("Player 1: {} ||| Player 2: {}".format(score_a, score_b), align="center",font=("courier", 24, "normal"))

    if ball.xcor() > 400:
        ball.goto(0,0)
        #Scorer has to catch ball first
        x_vel = -x_vel

        score_a += 1
        pen.clear()
        pen.write("Player 1: {} ||| Player 2: {}".format(score_a, score_b), align="center",font=("courier", 24, "normal"))

    wn.update()
