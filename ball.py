import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

def draw_square():
    square = turtle.Turtle()
    square.color("white")
    square.penup()
    square.goto(-300, 300)
    square.pendown()
    for _ in range(4):
        square.forward(600)
        square.right(90)
    square.hideturtle()

draw_square()

balls = []
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan"]
score = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

ball = turtle.Turtle()
ball.shape("circle")
ball.color(random.choice(colors))
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.dx = random.choice([-2, 2])
ball.dy = random.choice([-2, 2])
balls.append(ball)

target = turtle.Turtle()
target.shape("square")
target.color("white")
target.penup()
target.goto(200, 0)

def add_ball():
    new_ball = turtle.Turtle()
    new_ball.shape("circle")
    new_ball.color(random.choice(colors))
    new_ball.penup()
    new_ball.speed(0)
    new_ball.goto(random.randint(-200, 200), random.randint(-200, 200))
    new_ball.dx = random.choice([-2, 2])
    new_ball.dy = random.choice([-2, 2])
    balls.append(new_ball)

while True:
    screen.update()
    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        ball.dy -= 0.1


        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -0.9
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.distance(target) < 20:
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
            target.goto(random.randint(-200, 200), random.randint(-200, 200))
            ball.color(random.choice(colors))
            ball.dx *= 1.1
            ball.dy *= 1.1
            add_ball()
