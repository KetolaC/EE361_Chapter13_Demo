import turtle

class ArcadeMachine:
    turtleList = []
    game = None

    def getGame(self):
        return ArcadeMachine.game

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
        self.arcadeWin.onkey(self.gameUp, 'w')
        self.arcadeWin.onkey(self.gameDown, 's')
        self.pxcept = 0
        self.xcept = 0
        self.arcadeWin.onkey(self.quit, 'i')

    def getScreen(self):
        return self.arcadeWin

    def quit(self):
        self.arcadeWin.bye()
        # self.arcadeWin.getcanvas().destroy()

    def gameUp(self):
        if self.xcept == 0 or self.xcept == 1:
            self.xcept = 4  #For initial screen
        else:
            self.xcept = self.xcept - 1
        self.selectGame()

    def gameDown(self):
        if self.xcept == 4:
            self.xcept = 1  #For last game on list
        else:
            self.xcept = self.xcept + 1
        self.selectGame()

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
        if self.pxcept != self.xcept:
            ArcadeMachine.turtleList[self.xcept].color('green')
            ArcadeMachine.turtleList[self.xcept].write(self.games[self.xcept], align="left", font=("Pixel NES", 40, "normal"))
            self.showGames(self.xcept)
            if self.xcept == 1:
                ArcadeMachine.game = DroneInvaders(-200, 200, 0, 400)
            elif self.xcept == 2:
                ArcadeMachine.game = None # Will place Duck Hunt here
            if self.xcept == 3:
                ArcadeMachine.game = None #SnakeGame()
            if self.xcept == 4:
                ArcadeMachine.game = playHL3()
        self.pxcept = self.xcept
        print(ArcadeMachine.game)

    def use(self):
        self.arcadeWin.listen()
        turtle.mainloop()
