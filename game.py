# Space Invaders
# Python 3.7.3
# Visual Studio Code (Mac)

import turtle
import os
import math
import random

# Create the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# Scoring
score = 0

# Registering shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw the score
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.speed(0)
score_pen.hideturtle()
score_pen.color("white")
score_pen.setposition(-290, 280)
score_print = "Score: %s" % score
score_pen.write(score_print, False, align="left", font=("Arial", 14, "normal"))

# Create the border
border = turtle.Turtle()
border.color("white")
border.penup()
border.hideturtle()
border.setposition(-300, -300)
border.pensize(3)
border.speed(0)
border.pendown()
for sides in range(4):
    border.forward(600)
    border.left(90)

# Create multiple enemies
number_of_enemies = 5

enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_speed = 5  # 1.5
enemy_drop = 40

# Initialise enemies
for enemy in enemies:
    enemy.shape("invader.gif")
    enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.setpos(random.randint(-200, 200), random.randint(100, 250))

# Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15


# Player movements
def Move_Left():
    x = player.xcor()
    x -= player_speed
    if x <= -275:
        x = -275
    player.setx(x)


def Move_Right():
    x = player.xcor()
    x += player_speed
    if x >= 275:
        x = 275
    player.setx(x)


# Create the bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.speed(0)
bullet.setposition(0, -400)
bullet.setheading(90)

bullet_speed = 35


# Fire bullet
def Fire_Bullet():
    if not bullet.isvisible():
        os.system("afplay laser.wav&")
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


# Collision checking
def Collision(turtle_1, turtle_2):
    distance = math.sqrt(
        math.pow(turtle_1.xcor() - turtle_2.xcor(), 2) + math.pow(turtle_1.ycor() - turtle_2.ycor(), 2))
    return distance


# Keyboard bindings
turtle.listen()
turtle.onkey(Move_Left, "Left")
turtle.onkey(Move_Right, "Right")
turtle.onkey(Fire_Bullet, "space")

# Main loop
while True:

    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        if x > 275:
            enemy_speed *= -1
            for e in enemies:
                y = e.ycor()
                y -= enemy_drop
                e.sety(y)

        if x < -275:
            enemy_speed *= -1
            for e in enemies:
                y = e.ycor()
                y -= enemy_drop
                e.sety(y)

        # Check if bullet hit enemy
        if Collision(bullet, enemy) <= 15:
            os.system("afplay explosion.wav&")
            score += 10
            score_pen.clear()
            score_print = "Score: %s" % score
            score_pen.write(score_print, False, align="left", font=("Arial", 14, "normal"))
            bullet.hideturtle()
            bullet.setposition(0, -400)
            enemy.setpos(random.randint(-200, 200), random.randint(100, 250))

        # Check if enemy hit player
        if enemy.ycor() < (player.ycor() + 25):
            quit("Game Over")

    # Move the bullet
    if bullet.isvisible():
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 250:
        bullet.setposition(player.xcor(), player.ycor())
        bullet.hideturtle()
