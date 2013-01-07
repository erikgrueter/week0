# Flower excercise (4.2) from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay=.01
def flower(t,n,length,z):
	for i in range(z):		 	
		angle = 360.0 / n
    		for i in range(n):
        		fd(t, length)
        		lt(t, angle)
		lt(bob,20)
flower(bob,7,70,20)

# This is where you put code to move bob
# Since i dont have access to math for some reason, I created a flower from the polygon.







wait_for_user()					

