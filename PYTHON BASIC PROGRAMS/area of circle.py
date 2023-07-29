Area of Circle

Area of circle = ℼ * radius * radius = ℼr2
Where,
ℼ = pi = 3.14
r is radius of circle


#1 python program to find area of circle

# take inputs
r = 10

# calculate area of circle
area = 3.14 * r * r

# display result
print('Area of circle = ',area)


#2 python program to find area of circle

# store input
r = float(input('Enter the radius of the circle: '))

# calculate area of circle
area = 3.14 * r * r

# display result
print('Area of circle = %.2f ' %area)


#3 python program to find area of circle using math file

import math   # math file

# store input
r = float(input('Enter the radius of the circle: '))

# calculate area of circle
area = math.pi * r * r

# display result
print('Area of circle = %.2f ' %area)


#4 python program to find area of circle using functions

import math     # math file

def area_of_circle(r):      #user-defined function
 area = math.pi * r * r     # calculate area of circle
 return area            #return value

# store input
r = float(input('Enter the radius of the circle: '))

# display result
print('Area of circle = %.2f ' %area_of_circle(r))
