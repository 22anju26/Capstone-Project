# imports
import tkinter as tk
import turtle
import random
import pickle


# turtle game window setup
wn = turtle.Screen()
wn.title("Piano Tiles")
wn.bgcolor("white")
wn.setup(410,800)
wn.tracer(0)


# turtle splashscreen setup
def open_splashscreen():
    root = tk.Tk()
    root.title("Piano Tiles")
    root.geometry("410x800")
    
    # functions
    
    
    # widgets
    label_title = tk.Label(root, text = "Piano Tiles", font = ("Arial", 30))
    label_title.pack()
    
    label_highscore = tk.Label(root, text = f"Highest Score: {pickle.load(open('highscore.dat', 'rb'))}", font = ("Arial", 25))
    label_highscore.pack()
    
    
    
    root.mainloop()


# initial stuff
score = 0
lives = 5
font = ("Calibri", 20, "bold")
possible_x = (-150, -50, 50, 150)
possible_y = (-300, -100, 100, 300)
q = -150, -300
w = -50, -300
e = 50, -300
r = 150, -300


# class
class Grid(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("grey")

    def vertical(self):
        self.shapesize(400, 0.1, 0.1)
    
    def horizontal(self):
        self.shapesize(0.1, 400, 0.1)


class Tile(turtle.Turtle):
    def __init__(self, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(random.choice(possible_x), y)
        self.shape("square")
        self.shapesize(10, 5, 0.1)
        self.color("black")


# scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("red")
scoreboard.speed(0)
scoreboard.penup()
scoreboard.goto(0, 350)
scoreboard.write(f"Score: {score} Lives: {int(lives)}", align = "center", font = font)


# grids
grid1 = Grid(-100, 0)
grid2 = Grid(0, 0)
grid3 = Grid(100, 0)
vertical_grids = (grid1, grid2, grid3)
for grid in vertical_grids:
    grid.vertical()

grid4 = Grid(0, -200)
grid5 = Grid(0, 0)
grid6 = Grid(0, 200)
grid7 = Grid(0, -400)
horizontal_grids = (grid4, grid5, grid6, grid7)
for grid in horizontal_grids:
    grid.horizontal()


# tiles
tile1 = Tile(-300)
tile2 = Tile(-100)
tile3 = Tile(100)
tile4 = Tile(300)

tiles = [tile1, tile2, tile3, tile4]


# functions
def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score} Lives: {int(lives)}", align = "center", font = font)

def move_down():
    for tile in tiles:
        tile.sety(tile.ycor() - 200)

def move(key):
    global score
    global lives
    for tile in tiles:
        if tile.pos() == key:
            score += 10
            tile.goto(random.choice(possible_x), 300)
            tiles.remove(tile)
            move_down()
            tiles.append(tile)
            update_scoreboard()
            break
        else:
            lives -= 0.25
            game_over()
            update_scoreboard()
    wn.update()


# keybinding
wn.listen()
wn.onkeypress((lambda:move(q)), "q")
wn.onkeypress((lambda:move(w)), "w")
wn.onkeypress((lambda:move(e)), "e")
wn.onkeypress((lambda:move(r)), "r")


# check life
def game_over():
    if lives == 0.0:
        pickle.dump(score, open("highscore.dat", "wb"))
        wn.bye()
        open_splashscreen()


# mainloop
wn.update()
wn.mainloop()
