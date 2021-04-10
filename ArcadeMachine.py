import turtle
import time
from DroneInvaders import *
#from HalfLife3 import HalfLife3
#from SnakeGamePlay import *


class ArcadeMachine:
    turtleList = []

    def __init__(self):
        self.x, self.y = 0, 0
        self.games = ["Select Game", "Drone Invaders", "Duck Hunt", "Snake", "Half Life 3"]
        for i in range(5):
            ArcadeMachine.turtleList.append(turtle.Turtle())
        arcade = turtle.Turtle()
        self.arcadeWin = arcade.getscreen()
        self.arcadeWin.setworldcoordinates(0, 0, 100, 100)
        self.arcadeWin.bgcolor('black')
        self.showGames()
        self.canvas = turtle.getcanvas()
        self.canvas.bind('<Motion>', self.motion)
        self.pxcept = 0
        self.xcept = 0
        # self.arcadeWin.onclick(self.selectGame())

    def getScreen(self):
        return self.arcadeWin

    def getCanvas(self):
        return self.canvas

    def motion(self, event):
        self.x, self.y = event.x, event.y
        self.selectGame()
        print('{}, {}'.format(self.x, self.y))

    def showGames(self, exception = 6):
        x = 1
        for i in (range(5)):
            if i != exception:
                ArcadeMachine.turtleList[i].hideturtle()
                ArcadeMachine.turtleList[i].color('white')
                ArcadeMachine.turtleList[i].up()
                ArcadeMachine.turtleList[i].setpos((5, 100 - 15 * x))
                ArcadeMachine.turtleList[i].down()
                ArcadeMachine.turtleList[i].write(self.games[i], align="left", font=("Pixel NES", 40, "normal"))
            x += 1

    def selectGame(self):
        if 100 < self.y < 200:
            self.xcept = 1
        elif 200 < self.y < 300:
            self.xcept = 2
        elif 300 < self.y < 400:
            self.xcept = 3
        elif 400 < self.y < 500:
            self.xcept = 4
        if self.pxcept != self.xcept:
            ArcadeMachine.turtleList[self.xcept].color('green')
            ArcadeMachine.turtleList[self.xcept].write(self.games[self.xcept], align="left", font=("Pixel NES", 40, "normal"))
            self.showGames(self.xcept)
        self.pxcept = self.xcept


arcade0 = ArcadeMachine()
canvas0 = arcade0.getCanvas()
arcadeWin0 = arcade0.getScreen()
arcadeWin0.listen()
mainloop()

# turtle.exitonclick()

#game = DroneInvaders(-200, 200, 0, 400)
#game = SnakeGamePlay()
#game = HalfLife3()
#game.play()

