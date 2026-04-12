import turtle
from math import sqrt

# Konstante
G = 6.6743e-11
M = 1.99e30        # Sonnenmasse
m = 6e24           # Masse des Planeten
dt = 2000          # dt
scale = 1e9        # der Maßstab
running = True

# Anfangsbedingungen
x = 1.5e11
y = 0
vx = 0
vy = int(input("vy?(m/s)"))

# der Bildschirm
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Orbit Simulation")
screen.tracer(0)

# die Sonne
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0, 0)

# der Planet
planet = turtle.Turtle()
planet.shape("circle")
planet.color("white")
planet.penup()
planet.goto(x/scale, y/scale)
planet.pendown()

# der Text
info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(-350, 300)

# die Funktionen
def acceleration(x, y):
    r = sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return ax, ay

def energy(x, y, vx, vy):
    r = sqrt(x**2 + y**2)
    kinetic = 0.5 * m * (vx**2 + vy**2)
    potential = -G * M * m / r
    return kinetic + potential

# die Anfangsbeschleunigung
ax, ay = acceleration(x, y)

# Werle Methode
def step():
    global x, y, vx, vy, ax, ay
    x_new = x + vx*dt + 0.5*ax*dt**2
    y_new = y + vy*dt + 0.5*ay*dt**2
    ax_new, ay_new = acceleration(x_new, y_new)
    vx += 0.5*(ax + ax_new)*dt
    vy += 0.5*(ay + ay_new)*dt
    x, y = x_new, y_new
    ax, ay = ax_new, ay_new
    planet.goto(x/scale, y/scale)
    E = energy(x, y, vx, vy)
    info.clear()
    info.write(f"Energy: {E:.2e}", font=("Arial", 12, "normal"))

# die Pause
def toggle():
    global running
    running = not running

screen.listen()
screen.onkey(toggle, "space")

# der Zyklus
while True:
    if running:
        step()
    screen.update()