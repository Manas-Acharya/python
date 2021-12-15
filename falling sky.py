import turtle
import random


wd = turtle.Screen()
wd.title("Falling Sky")
#wd.bgcolor("firebrick")
wd.setup(width=1067, height=600)
wd.bgpic("fv.gif")
wd.tracer(0)

wd.register_shape("kurama.gif")
wd.register_shape("kamehame.gif")
wd.register_shape("rasen5.gif")



score = 0
lives = 3
#Player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("kurama.gif")
player.color("white")
player.goto(0, -250)
player.direction = "stop"

#Increase score by collecting safe objects

safel = []

for n in range(6):

    safe = turtle.Turtle()
    safe.speed(0)
    safe.penup()
    safe.shape("rasen5.gif")
    safe.color("yellow")
    safe.goto(-100, 250)
    safe.speed = random.randint(1,2)
    safel.append(safe)


# Objects to avoid

avoidd = []

for n in range(6):

    avoid = turtle.Turtle()
    avoid.speed(0)
    avoid.penup()
    avoid.shape("kamehame.gif")
    #avoid.color("red")
    avoid.goto(-100, 250)
    avoid.speed = random.randint(1,2)
    avoidd.append(avoid)




pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.goto(0, 250)
font = ("Courier", 30, "normal")
pen.write("Score: {}  Lives: {}".format(score, lives),font=font)    








def start_game():
    global game_state
    game_state = "game"
       


def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

def stop_player():
    player.direction = "stop"


 

    


# Keyboard Binding
wd.listen()
wd.onkeypress(go_left, "Left")
wd.onkeypress(go_right, "Right")
wd.onkeypress(stop_player, "Down")
wd.onkeypress(start_game, "f")


game_state = "game"

#Main game
while True:
    

    wd.update()
    
    #if game_state == "game":
     #   wd.bgpic("fv.gif")
    # Game over    
    if game_state == "gameover":
        wd.clear()
        wd.bgpic("gameover1.gif")
        break
    

    # Move the player
    
    if player.direction == "left":
        x = player.xcor()
        x -=1.3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x +=1.3
        player.setx(x)

    if player.direction == "stop":
        x = player.xcor()
        x += 0
        player.setx(x)


#Move the safe objects
    for safe in safel:
        y = safe.ycor()
        y -= safe.speed
        safe.sety(y)

#Check if off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            safe.goto(x, y)


#Check for collision
        if safe.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            score +=10
            safe.goto(x, y)
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives),font=font)

#Move the objects to avoid
    for avoid in avoidd:
        y = avoid.ycor()
        y -= avoid.speed
        avoid.sety(y)

#Check if off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            avoid.goto(x, y)


#Check for collision
        if avoid.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            avoid.goto(x, y)
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives),font=font)
            print(score)
            if lives == 0:
                game_state = 'gameover'





        


    
    



wd.mainloop()
