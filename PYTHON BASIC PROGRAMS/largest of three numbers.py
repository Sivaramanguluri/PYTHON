#1 Python program to find largest of 3 numbers

# take inputs
num1 = 5
num2 = 3
num3 = 9

# find largest numbers
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# display result
print('The largest number = ', largest)



#2 Python program to find the largest of three numbers

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# find largest numbers
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# display result
print('The largest number = ', largest)



#3 Python program to find the largest among 
# three numbers using max() function

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# find largest numbers and display result
print('The largest number = ', max(num1, num2, num3))



#4 Python program to find greatest of three numbers using function

def findLargest(num1, num2, num3):  #user-defined function
    # find largest numbers
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest  #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# function call
maximum = findLargest(num1, num2, num3)

# display result
print('The largest number = ',maximum)



