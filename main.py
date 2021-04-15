from DroneWASD import *
from HalfLife3 import *
from Snake import SnakeGame

arcade = [DroneInvaders(-200, 200, 0, 400), None, playHL3()]

gameChoice = input("Type a number to select a game:\n1. Drone Invaders\n2. Duck Hunt\n3. Half-Life 3\n")

gameSelect = int(gameChoice)

game = arcade[gameSelect - 1]

game.play()

