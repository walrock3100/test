import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(0)
tracer(5)  # Tempo: kleinere Zahl = langsamer, größere Zahl = schneller
hideturtle()
bgcolor("black")
color("red")

for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    goto(0, 0)

# Blaues B, Linie für Linie
tracer(1)
speed(3)  # Tempo für das B: 1 = langsam, 10 = schnell
color("blue")
pensize(12)

penup()
goto(-40, -80)
pendown()
setheading(90)
forward(160)          # senkrechter Strich
setheading(0)
forward(40)
circle(-40, 180)      # oberer Bogen
forward(40)
setheading(0)
forward(45)
circle(-40, 180)      # unterer Bogen
forward(45)

update()
done()
