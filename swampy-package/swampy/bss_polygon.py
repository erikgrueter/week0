# Polygon excercise from Week 0

# Name:Erik Grueter


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay=.01
# Bob making a square:
def square(t)
for i in range(4):
    fd(t, 100)
    lt(t)

square(bob)

# Polyline re-factored code
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

# couldnt run this myself. Having problems with math.pi!! 
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
# This is where you put code to move bob








wait_for_user()					
