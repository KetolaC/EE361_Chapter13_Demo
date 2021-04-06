import turtle
import random
import time

# Credit to geeksforgeeks for their snake tutorial

class SnakeGame:
    def __init__(self):
        self.__win = turtle.Screen()
        self.__win.bgcolor('black')
        self.__win.setup(width=500, height=500)
        self.__snake = Snake()
        self.__scores = Score()

    def restart(self):
        time.sleep(1)
        self.__scores.resetPoints()
        self.__snake.removeSegs()

    def play(self):
        self.__win.listen()
        self.__win.onkeypress(self.__snake.moveUp, "w")
        self.__win.onkeypress(self.__snake.moveDown, "s")
        self.__win.onkeypress(self.__snake.moveLeft, "a")
        self.__win.onkeypress(self.__snake.moveRight, "d")
        while True:
            self.__win.update()
            if self.__snake.outOfBounds():
                self.restart()




class Snake:
    def __init__(self):
        # self.__snakeWin = win
        self.__segments = []
        self.__head = turtle.Turtle()
        self.__head.shape("square")
        self.__head.color("green")
        self.__head.penup()
        self.__head.goto(0, 0)
        self.__head.direction = "Stop"

    def moveUp(self):
        if self.__head.direction != "down":
            self.__head.direction = "up"

    def moveDown(self):
        if self.__head.direction != "up":
            self.__head.direction = "down"

    def moveLeft(self):
        if self.__head.direction != "right":
            self.__head.direction = "left"

    def moveRight(self):
        if self.__head.direction != "left":
            self.__head.direction = "right"

    def move(self):
        if self.__head.direction == "up":
            y = self.__head.ycor()
            self.__head.sety(y + 20)
        if self.__head.direction == "down":
            y = self.__head.ycor()
            self.__head.sety(y - 20)
        if self.__head.direction == "left":
            x = self.__head.xcor()
            self.__head.setx(x - 20)
        if self.__head.direction == "right":
            x = self.__head.xcor()
            self.__head.setx(x + 20)

    def addSeg(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")  # tail colour
        new_segment.penup()
        self.__segments.append(new_segment)

    def removeSegs(self):
        self.__head.goto(0, 0)
        self.__head.direction = "Stop"
        for segment in self.__segments:
            segment.goto(1000, 1000)
        self.__segments.clear()

    def outOfBounds(self):
        if self.__head.xcor() > 290 or self.__head.xcor() < -290 or self.__head.ycor() > 290 or self.__head.ycor() < \
                -290:
            return True
        else:
            return False

class Food:
    def __init__(self):
        self.__food = turtle.Turtle()
        foodColor = random.choice(['pink', 'blue', 'white', 'red', 'yellow', 'orange'])
        self.__food.shape('circle')
        self.__food.color(foodColor)
        self.__food.penup()
        self.__food.goto(0, 100)


class Score:
    def __init__(self, win):
        self.__score = 0
        self.__highScore = 0
        self.__scorePen = turtle.Turtle()
        self.__scorePen.hideturtle()
        self.__scorePen.goto(0, 250)
        self.__scorePen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

    def keepScore(self):
        self.__scorePen.write("Score : {}  High Score : {}".format(self.__score, self.__highScore), align="center",
                              font=("candara", 24, "bold"))
        if self.__score > self.__highScore:
            self.__highScore = self.__score

    def addPoints(self):
        self.__score += 10
        self.__scorePen.clear()

    def resetPoints(self):
        self.__score = 0
        self.__scorePen.clear()
