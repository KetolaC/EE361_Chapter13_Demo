from turtle import Turtle

class LaserCannon(Turtle):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__screen = self.getscreen()
        self.__screen.onclick(self.aim)
        self.__screen.onkey(self.shoot, 's')
        self.__screen.onkey(self.quit, 'q')

    def aim(self, x, y):
        heading = self.towards(x, y)
        self.setheading(heading)

    def shoot(self):
        Bomb(self.heading(), 5, self.__xMin, self.__xMax, self.__yMin, self.__yMax)

    def quit(self):
        self.__screen.bye()


# The Bounded Turtle class


from abc import *

class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getXMax(self):
        return self.__yMax

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass

# The Drone Class


import random

class Drone(BoundedTurtle):
    droneList = [] #static variable

    @staticmethod
    def getDrones():
        return [x for x in Drone.droneList if x.__alive]

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()
        if 'Drone.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape('Drone.gif')
        self.shape('Drone.gif')
        self.goto(random.randint(xMin - 1, xMax - 1), yMax - 20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        Drone.droneList = Drone.getDrones()
        Drone.droneList.append(self)
        self.__alive = True
        self.getscreen().ontimer(self.move, 200)

    def move(self):
        self.forward(self.getSpeed())
        if self.outOfBounds():
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 200)

    def remove(self):
        self.__alive = False
        self.hideturtle()

#The Bomb Class


import math

class Bomb(BoundedTurtle):
    def __init__(self, initHeading, speed, xMin, xMax, yMin, yMax):
        super.__init__(speed, xMin, xMax, yMin, yMax)
        self.resizemode('user')
        self.color('red', 'red')
        self.shape('circle')
        self.turtlesize(.25)
        self.setheading(initHeading)
        self.up()
        self.getscreen().ontimer(self.move, 100)

    def move(self):
        exploded = False
        self.forward(self.getSpeed())
        for a in Drone.getDrones():
            if self.distance(a) < 5:
                a.remove()
                exploded = True
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        self.hideturtle()

# The Drone Invaders Game Class


from tkinter import mainloop


class DroneInvaders:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax

    def play(self):
        self.__mainWin = LaserCannon(self.__xMin, self.__xMax, self.__yMin, self.__yMax).getscreen()
        self.__mainWin.bgcolor('light green')
        self.__mainWin.setworldcoordinates(self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)
        self.__mainWin.listen()
        mainloop()

    def addDrone(self):
        if len(Drone.getDrones()) < 7:
            Drone(1, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)
