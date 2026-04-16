import turtle
from math import sqrt

    # Konstante
G = 6.6743e-11
M = 1.99e30
mu = G * M

dt = 2000
scale = 1e9
running = True

    # Eingabe der Anfangsbedingungen
print("Initial conditions:")

x = float(input("Entfernung von der Sonne x (m, z.B. 1.5e11): "))
y = 0

vx = 0
vy = float(input("vy (m/s): "))

    # Bildschirm
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Orbit Simulation mit Kepler-Check")
screen.tracer(0)

    # Sonne
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0, 0)

    # Planet
planet = turtle.Turtle()
planet.shape("circle")
planet.color("white")
planet.penup()
planet.goto(x/scale, y/scale)
planet.pendown()

    # Text
info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(-350, 300)

    # Beschleunigung
def acceleration(x, y):
    r = sqrt(x**2 + y**2)
    ax = -mu * x / r**3
    ay = -mu * y / r**3
    return ax, ay

    # Initiale Arealgeschwindigkeit
vA0 = 0.5 * (x * vy - y * vx)

    # Schritt
def step():
    global x, y, vx, vy

    ax, ay = acceleration(x, y)

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    planet.goto(x/scale, y/scale)


    # Arealgeschwindigkeit
    vA = 0.5 * (x * vy - y * vx)

    deviation = (vA - vA0) / abs(vA0) * 100

    info.clear()
    info.write(
        f"Arealgeschwindigkeit: {vA:.2e} m²/s\n"
        f"ΔȦ: {deviation:+.2f}%",
        font=("Arial", 12, "normal")
    )

    # Pause
def toggle():
    global running
    running = not running

screen.listen()
screen.onkey(toggle, "space")

    # Hauptschleife
while True:
    if running:
        step()
    screen.update()