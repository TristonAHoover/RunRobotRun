#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move_up():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(90)
  robot.speed(2)
  robot.fd(50)
  detectLocation()

def move_left():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(180)
  robot.speed(2)
  robot.fd(50)
  detectLocation()

def move_right():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(0)
  robot.speed(2)
  robot.fd(50)
  detectLocation()

def move_down():
  robot.dot(10)
  robot.speed(0)
  robot.setheading(270)
  robot.speed(2)
  robot.fd(50)
  detectLocation()

def reset():
  robot.clear()
  robot.speed(0)
  robot.setheading(90)
  robot.goto(startx,starty)
  robot.speed(2)

def detectLocation(): # used to detect if the robot passes a level
  print(robot.pos())
  if robot.pos() == (100,100) and wn.bgpic() == "maze1.png":
    reset()
    wn.bgpic("maze2.png")
  elif (robot.pos() == (0,50) or robot.pos() == (-0,50)) and wn.bgpic() == "maze2.png":
    reset()
    wn.bgpic("maze3.png")
  elif robot.pos() == (100,100) and wn.bgpic() == "maze3.png":
    reset()
    wn.bgpic("maze4.png")
  if robot.pos() == (100,100) and wn.bgpic() == "maze4.png":
    reset()
    wn.bgpic("maze1.png")

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

wn.bgpic("maze1.png")

# user input
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_left, "Left")
wn.onkey(move_down, "Down")
wn.onkey(move_right, "Right")
wn.onkey(reset, "r")
print("\nWelcome to Run Robot Run!\nUse arrow keys to move, press \"r\" to reset robot")

wn.mainloop()