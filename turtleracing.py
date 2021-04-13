# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:59:40 2021

@author: matth
"""

import turtle
import time
import random

#turtle screen
WIDTH,  HEIGHT = 500, 500
COLORS = ['red', 'green', 'orange', 'pink', 'yellow', 'blue', 'brown', 'black', 'purple', 'brown']


def get_number_of_racers():
    racers = 0
    #ask user until valid number is inserted
    while True:
        racers = input("Enter number of racers (2-10): ")
        #before converting check if digit
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            #continue brings you back to the top of the while loop
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
            

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set pos
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles  
  
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            #move each racer
            distance = random.randrange(1, 20, 1)
            racer.forward(distance)
            
            #check if it passed the finish line
            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
#liste von farben mit der richtigen anzahl
colors = COLORS[:racers]
winner = race(colors)

print("winner: " + winner)
time.sleep(5)

# #turtle object
# racer = turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('blue')
# #number = pixel
# racer.forward(100)
# #left, right setting the angle
# racer.left(90)
# racer.forward(100)
# racer.pendown()
# time.sleep(2)
# racer.right(90)
# racer.backward(100)
