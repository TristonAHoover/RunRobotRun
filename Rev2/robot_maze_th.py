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
  robot.pencolor("darkorchid")
  reset()

#---- end robot movement 

wn.mainloop()