
import turtle
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Continuous Rainbow Animaton")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

h = 0
i = 1

def animate():
    global h, i

    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.circle(i * 0.3)
    t.left(18)
    t.forward(i * 0.3)
    t.right(70)

    h = (h + 0.003) % 1.0
    i += 0.2

    if i > 200:
        i = 1
        t.clear()

    screen.update()
    screen.ontimer(animate,20)

animate()
turtle.done()
