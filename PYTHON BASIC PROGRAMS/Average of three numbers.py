#1 Python program to find average of three numbers

# take inputs
num1 = 3
num2 = 5
num3 = 14

# calculate average
avg = (num1 + num2 + num3)/3

# display result
print('The average of numbers = %0.2f' %avg)


#2 Python program to find average of three numbers

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# calculate average
avg = (num1 + num2 + num3)/3

# display result
print('The average of numbers = %0.2f' %avg)


#3 Python program to find average of three numbers using function

def avg_num(num1, num2, num3):   #user-defined function
    avg = (num1 + num2 + num3)/3   #calculate average
    return avg    #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# function call
average = avg_num(num1, num2, num3)

# display result
print('The average of numbers = ',average)
