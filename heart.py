import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

def bogen(mx, my, r):
    # Punkte eines Halbkreises rechts vom Mittelpunkt, von oben nach unten
    return [(mx + r*math.cos(math.radians(a)), my + r*math.sin(math.radians(a)))
            for a in range(90, -91, -5)]

# Alle Punkte, durch die der Stift für das B fährt
b_punkte = ([(-40, y) for y in range(-80, 81, 5)]      # senkrechter Strich
            + [(x, 80) for x in range(-40, 1, 5)]      # oben nach rechts
            + bogen(0, 40, 40)                         # oberer Bogen
            + [(x, 0) for x in range(0, -41, -5)]      # zurück zur Mitte
            + [(x, 0) for x in range(-40, 6, 5)]       # Mitte nach rechts
            + bogen(5, -40, 40)                        # unterer Bogen
            + [(x, -80) for x in range(5, -41, -5)])   # unten zurück

tracer(5)  # Tempo: kleinere Zahl = langsamer, größere Zahl = schneller
bgcolor("black")

herz = Turtle()
herz.hideturtle()
herz.speed(0)
herz.color("red")

b = Turtle()
b.hideturtle()
b.speed(0)
b.color("blue")
b.pensize(12)
b.penup()
b.goto(b_punkte[0])
b.pendown()

schritte = 6000
b_nr = 0
for i in range(schritte):
    herz.goto(hearta(i)*20, heartb(i)*20)
    herz.goto(0, 0)

    # Das B wächst gleichzeitig mit dem Herz
    while b_nr < (i + 1) * len(b_punkte) // schritte:
        b.goto(b_punkte[b_nr])
        b_nr += 1

    # B immer vor den roten Linien halten
    for linie in b.items:
        getcanvas().tag_raise(linie)

update()
done()
