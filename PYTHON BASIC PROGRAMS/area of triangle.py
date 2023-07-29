#1 python program to find the area of the right-angle triangle

# take inputs
base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

# calculate area of triangle
area = (1/2) * base * height

# display result
print('Area of triangle = ',area)


#2 python program to find the area of the triangle

# take inputs
a = float(input('Enter the first side of the triangle: '))
b = float(input('Enter the second side of the triangle: '))
c = float(input('Enter the third side of the triangle: '))

# must be smaller than the third side.  
if (a < 0 or b < 0 or c < 0 or 
                 (a+b <= c) or (a+c <=b) or (b+c <=a) ):  
    print('Not a valid triangle')
    
else:

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate area of triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # display result
    print('Area of triangle = %0.2f' %area)


#3 python program to find the area of the triangle

import math   # math file

# take inputs
a = float(input('Enter the first side of the triangle: '))
b = float(input('Enter the second side of the triangle: '))
c = float(input('Enter the third side of the triangle: '))

# must be smaller than the third side.  
if (a < 0 or b < 0 or c < 0 or 
                      (a+b <= c) or (a+c <=b) or (b+c <=a) ):  
    print('Not a valid triangle')
    
else:

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate area of triangle
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # display result
    print('Area of triangle = %0.2f' %area)


#4 python program to find the area of the triangle

import math   # math file

def area_of_triangle(a, b, c):      #user-defined function
    
    # must be smaller than the third side.  
    if (a < 0 or b < 0 or c < 0 or 
                       (a+b <= c) or (a+c <=b) or (b+c <=a) ):  
        print('Not a valid trianglen')
        
    else:
        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # calculate area of triangle
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# take inputs
a = float(input('Enter the first side of the triangle: '))
b = float(input('Enter the second side of the triangle: '))
c = float(input('Enter the third side of the triangle: '))

# display result
print('Area of triangle = %0.2f' %area_of_triangle(a, b, c))
