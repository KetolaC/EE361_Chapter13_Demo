from turtle import *
import random
from abc import *
import math

class LaserCannon(Turtle):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__screen = self.getscreen()
        self.__screen.bgcolor('light green')
        self.__screen.setworldcoordinates(xMin, yMin, xMax, yMax)
        self.setheading(90)
        self.up()
        # self.__screen.onclick(self.aim, 1)
        self.__screen.onkey(self.shoot, "s")
        self.__screen.onkey(self.quit, 'q')
        self.__screen.onkey(self.leftKey, 'a')
        self.__screen.onkey(self.rightKey, 'd')

    def aim(self, x, y):
        heading = self.towards(x, y)
        self.setheading(heading)

    def leftKey(self):
        self.setx(self.xcor() - 20)

    def rightKey(self):
        self.setx(self.xcor() + 20)

    def shoot(self):
        Bomb(self.heading(), 20, self.__xMin, self.__xMax, self.__yMin, self.__yMax, self.xcor())

    def quit(self):
        self.screen.bye()

    def keepScore(self):
        print(Score())



class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin=-200, xMax=200, yMin=0, yMax=400):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.speed = speed

    def outOfBounds(self):
        xpos, ypos = self.position()
        out = False
        if xpos < self.__xMin or xpos > self.__xMax:
            out = True
        if ypos < self.__yMin or ypos > self.__yMax:
            out = True
        return out

    def move(self):
        self.forward(self.speed)
        if self.outOfBounds():
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 200)

    def remove(self):
        self.hideturtle()


class Drone(BoundedTurtle):
    DroneList = []

    @staticmethod
    def getDrones():
        return [x for x in Drone.DroneList if x.alive]

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()
        if 'drone.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape('drone.gif')
        self.shape('drone.gif')
        self.goto(random.randint(xMin - 1, xMax - 1), yMax - 20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        Drone.DroneList = [x for x in Drone.DroneList if x.alive]
        Drone.DroneList.append(self)
        self.alive = True
        self.getscreen().ontimer(self.move, 200)

    def remove(self):
        self.alive = False
        self.hideturtle()


class Bomb(BoundedTurtle):
    def __init__(self, initHeading, speed, xMin, xMax, yMin, yMax, startX):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.hideturtle()
        self.up()
        self.setx(startX)
        self.down()
        self.showturtle()
        self.initHeading = initHeading
        self.resizemode('user')
        self.color('red', 'red')
        self.shape('circle')
        self.turtlesize(.25)
        self.setheading(initHeading)
        self.up()
        self.getscreen().ontimer(self.move, 100)

    def move(self):
        exploded = False
        self.forward(self.speed)
        for i in Drone.getDrones():
            if self.distance(i) < 20:
                i.remove()
                exploded = True
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        a = p1[0] - p2[0]
        b = p1[1] - p2[1]
        dist = math.sqrt(a ** 2 + b ** 2)
        return dist


class Score(Turtle):

    Gscore = 0
    GhighScore = 0

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.__highScore = 0
        self.write("Score : {} High Score : {} ".format(self.__score, self.__highScore), align="center", font=
        ("candara", 24, "bold"))

    def addPoints(self, points):
        self.__score += points
        if self.__score > self.__highScore:
            self.__highScore = self.__score

    def getScore(self):
        return self.__score

    def getHighScore(self):
        return self.__highScore



class DroneInvaders:
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax

    def play(self):
        self.mainWin = LaserCannon(self.__xMin, self.__xMax, self.__yMin, self.__yMax).getscreen()
        self.mainWin.ontimer(self.addDrone, 1000)
        self.mainWin.listen()
        mainloop()

    def addDrone(self):
        if len(Drone.getDrones()) < 5:
            Drone(1, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.mainWin.ontimer(self.addDrone, 1000)

game = DroneInvaders(-200, 200, 0, 400)
game.play()
