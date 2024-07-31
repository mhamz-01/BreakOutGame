import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.9
ball.dy = -1.9

# Bricks
bricks = []

for y in range(4):
    for x in range(8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("blue")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(-290 + (x * 80), 250 - (y * 30))
        bricks.append(brick)


# Functions to move the paddle
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (
            ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and brick collision
    for brick in bricks:
        if (ball.distance(brick) < 27):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick out of the screen
            bricks.remove(brick)

    # Check if all bricks are cleared
    if len(bricks) == 0:
        print("You win!")
        break
