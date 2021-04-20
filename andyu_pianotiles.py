# imports
import turtle
import random
import pickle

# turtle game window setup
wn = turtle.Screen()
wn.title("Piano Tiles")
wn.bgcolor("white")
wn.setup(410,800)
wn.tracer(0)


# initial stuff
possible_x = (-150, -50, 50, 150)
possible_y = (-300, -100, 100, 300)
q = -150, -300
w = -50, -300
e = 50, -300
r = 150, -300
score = 0
lives = 5


# class
class Grid(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("grey")
        self.speed(0)

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
        self.speed(0)
    
    def reset(self):
        self.goto(random.choice(possible_x), y)

class Text(turtle.Turtle):
    def __init__(self, color, x, y, text, size):
        turtle.Turtle.__init__(self)
        font = ("Calibri", size, "bold")
        self.hideturtle()
        self.color(color)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.write(text, align = "center", font = font)
        
    def updatetext(self, new_text, size):
        font = ("Calibri", size, "bold")
        self.clear()
        self.write(new_text, align = "center", font = font)

def play_game():
    wn.clear()
    wn.tracer(0)
    # scoreboard
    scoreboard = Text("red", 0, 350, f"Score: {score} Lives: {int(lives)}", 20)

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
        scoreboard.updatetext(f"Score: {score} Lives: {int(lives)}", 20)

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
                update_scoreboard()
                game_over()
        wn.update()


    # keybinding
    wn.listen()
    wn.onkeypress((lambda:move(q)), "q")
    wn.onkeypress((lambda:move(w)), "w")
    wn.onkeypress((lambda:move(e)), "e")
    wn.onkeypress((lambda:move(r)), "r")
    
    # mainloop
    wn.update()
    wn.mainloop()

def splash_screen():
    wn.clear()
    wn.tracer(0)
        
    splash_title = Text("black", 0, 250, "Piano Tiles", 50)
    highscore = Text("black", 0, 100, f"Highest Score: {pickle.load(open('highscore.dat', 'rb'))}", 20)
    text = Text("black", 0, 50, "Press SPACE to play", 20)
    
    wn.listen()
    wn.onkeypress(play_game, "space")


# game over
def game_over():
    global score
    global lives
    
    if lives == 0.0:
        if score > pickle.load(open("highscore.dat", "rb")):
            pickle.dump(score, open("highscore.dat", "wb"))
        score = 0
        lives = 5
        
        splash_screen()

splash_screen()
wn.mainloop()
