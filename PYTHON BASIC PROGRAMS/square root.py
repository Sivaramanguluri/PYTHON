#1 Python program to find square root of the number
 
# take inputs
num = 25
 
# calculate square root
sqrt = num ** 0.5
 
# display result
print('Square root of %0.2f is %0.2f '%(num, sqrt))



#2 Python program to find square root of the number

# take inputs
num = float(input('Enter the number: '))

# calculate square root
sqrt = num ** 0.5

# display result
print('Square root of %0.2f is %0.2f '%(num, sqrt))



#3 Python program to find square root of the number

import math  # math module

# take inputs
num = float(input('Enter the number: '))

# display result
print('Square root = ',math.sqrt(num))



#4 Python program to find square root of complex nuumber

import cmath  # math module

# take inputs
num = 1+2j

# calculate square root
sqrt = cmath.sqrt(num)

# display result
print('The square root of {0} is {1:0.2f}+{2:0.2f}'.format(num, 
                             sqrt.real,sqrt.imag))



#5 Python program to find square root of complex nuumber

import cmath  # math module

# take inputs
num = eval(input('Enter the number: '))

# calculate square root
sqrt = cmath.sqrt(num)

# display result
print('The square root of {0} is {1:0.2f}+{2:0.2f}'.format(num, 
                            sqrt.real,sqrt.imag))
