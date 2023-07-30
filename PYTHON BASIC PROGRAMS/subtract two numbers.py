#1 Python program to subtract two numbers

# take inputs
num1 = 10
num2 = 7

# subtract two numbers
sub = num1 - num2

# print the subtraction result
print('The subtraction of numbers =', sub)



#2 Python program to subtract two numbers

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# subtract two numbers
sub = num1 - num2

# print the subtraction result
# value will print in float
print('The subtraction of numbers = %0.2f' %sub)


#3 Python program to subtract two numbers

def sub_num(num1, num2):  #user-defined function
    #subtract two numbers
    return num1-num2
    
# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calling function and print the subtraction value
print('The subtraction of numbers = %0.2f' %sub_num(num1, num2))


#4 In this program, we are using a built-in function to subtract numbers.
The numpy.subtract() function is used when we want to compute the difference
between two numbers or arrays. It returns the difference of numbers.

# Python program to subtract two numbers

#importing numpy.subtract() function
import numpy

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# subtract two numbers
sub = numpy.subtract(num1, num2)

# print the subtraction result
# value will print in float
print('The subtraction of numbers = %0.2f' %sub)


#5 This python program also performs the same task but in different ways.
In this program, we subtract two numbers without using (-) operator.

# Python program to subtract two numbers

def subtract_num(a,b):   #user-defined function
   if (b == 0):
      return a
   return subtract_num(a ^ b, (~a & b) << 1)

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# calling function
subtract = subtract_num(num1, num2)

# print subtract of numbers
print('The subtract of numbers {0} and {1} is {2}'
                       .format(num1, num2, subtract))


