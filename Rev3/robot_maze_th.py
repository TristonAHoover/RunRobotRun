#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

# direct movement
def move_up():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(90)
  robot.speed(2)
  robot.fd(50)

def move_left():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(180)
  robot.speed(2)
  robot.fd(50)

def move_right():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(0)
  robot.speed(2)
  robot.fd(50)

def move_down():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(270)
  robot.speed(2)
  robot.fd(50)

def reset():
  robot.clear()
  robot.speed(0)
  robot.setheading(90)
  robot.goto(startx,starty)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

while True:
  # maze/movement
  # maze 1
  wn.bgpic("maze1.png")
  for step in range(8):
    move()
    if step == 3:
      for i in range(3):
        turn_left()
  reset()

  # maze 2
  wn.bgpic("maze2.png")
  for step in range(5):
    move()
    if step == 2:
      for i in range(3):
        turn_left()
  reset()

  # maze 3
  wn.bgpic("maze3.png")
  for step in range(4):
    if step != 0:
      turn_left()
    move()
    for i in range (3):
      turn_left()
    move()
    if step == 1:
      robot.pencolor("deepskyblue")
  reset()

  # maze 4
  wn.bgpic("maze4.png")
  robot.pencolor("darkorchid")
  for step in range(16):
    if step < 4 or step > 11:
      move_right()
    elif step != 4 and step != 5 and step != 10 and step != 11:
      move_left()
    else:
      move_up()
  reset()

#---- end robot movement 

wn.mainloop()