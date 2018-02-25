import math

# Reads the diameter of the sphere and stores in diameter variable
diameter = float(input('Enter diameter of the sphere: '))
# Calculates the radius of the sphere and stores in radius variable
radius = diameter/2
volume = (4/3) * (math.pi * radius*radius*radius)
print("Volume of the spehere is: ", volume)