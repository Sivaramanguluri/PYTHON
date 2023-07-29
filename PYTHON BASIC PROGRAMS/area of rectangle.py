#1 python program to find area of rectangle

# take inputs
length = 2
width = 5

# calculate area of rectangle
area = length * width

# display result
print('Area of rectangle = ',area)


#2 python program to find area of rectangle

# take inputs
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

# calculate area of rectangle
area = length * width

# display result
print('Area of rectangle = ',area)


#3 python program to find area of rectangle using functions

def area_of_rectangle(length, width):      # user-defined function
 area = length * width     # calculate area of rectangle
 return area            # return value

# store input
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

# display result
print('Area of rectangle = %.2f ' %area_of_rectangle(length, width))


