import turtle
from math import sqrt

    # Konstanten
G = 6.6743e-11
M = 1.99e30
mu = G * M

dt = 2000
scale =1e9

    # a — Entfernung von der Sonne  (m)
    # vy — vy (m/s)

planets_data = [
    ("Mercury", 5.79e10, 4.79e4),
    ("Venus",   1.082e11, 3.50e4),
    ("Earth",   1.496e11, 2.98e4),
    ("Mars",    2.279e11, 2.41e4),
    ("Jupiter", 7.785e11, 1.31e4),
    ("Saturn",  1.433e12, 9.63e3),
    ("Uranus",  2.872e12, 6.80e3),
    ("Neptune", 4.495e12, 5.43e3),
]

    # Bildschirm
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("All Planet Orbits (Kepler Simulation)")
screen.tracer(0)

    # Sonne
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0, 0)

    # Planeten
bodies = []

colors = ["gray", "orange", "blue", "red", "brown", "gold", "lightblue", "darkblue"]

for i, (name, a, vy) in enumerate(planets_data):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(colors[i % len(colors)])
    planet.penup()
    planet.goto(a / scale, 0)
    planet.pendown()

    bodies.append({
        "name": name,
        "x": a,
        "y": 0,
        "vx": 0,
        "vy": vy,
        "turtle": planet
    })

    # Berechnung
def acceleration(x, y):
    r = sqrt(x*x + y*y)
    ax = -mu * x / r**3
    ay = -mu * y / r**3
    return ax, ay

    # Schritt
def step():
    for b in bodies:
        x, y, vx, vy = b["x"], b["y"], b["vx"], b["vy"]

        ax, ay = acceleration(x, y)

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        b["x"], b["y"], b["vx"], b["vy"] = x, y, vx, vy

        b["turtle"].goto(x / scale, y / scale)

while True:
    step()
    screen.update()