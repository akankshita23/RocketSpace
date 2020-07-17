import turtle
screen=turtle.Screen()
screen.setup(400,400)
move = turtle.Turtle()
screen.bgpic("space2.gif")
screen.addshape("1.gif")
move.shape("1.gif")
move_speed = 10
turn_speed = 10


def k1():
  move.forward(move_speed)
def k2():
  move.left(turn_speed)
def k3():
  move.right(turn_speed)
def k4():
  move.back(move_speed)

move.penup()
screen.onkey(k1, "Up")
screen.onkey(k2, "Left")
screen.onkey(k3, "Right")
screen.onkey(k4, "Down")

screen.listen()
screen.mainloop()
screen.exitonclick()