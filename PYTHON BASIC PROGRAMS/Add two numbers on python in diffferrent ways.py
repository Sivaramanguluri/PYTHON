#1 python program to add two numbers

# take inputs
num1 = 5
num2 = 10

# add two numbers
sum = num1 + num2

# displaying the addition result
print('{0} + {1} = {2}'.format(num1, num2, sum))



#2 python program to add two numbers with user input

# store input numbers
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

# add two numbers
# User might also enter float numbers
sum = float(num1) + float(num2)

# displaying the adding result
# value will print in float
print('The sum of numbers {0} and {1} is {2}'
                      .format(num1, num2, sum))



#3 Python program to add two numbers using function

def add_num(a,b):   #user-defined function
    sum = a + b   #adding numbers
    return sum   #return value

# take input
num1 = float(input('Enter first number : '))
num2 = float(input('Enter second number : '))

# function call
print('The sum of numbers {0} and {1} is {2}'
       .format(num1, num2, add_num(num1, num2)))




#4 Python program to add two numbers in one line
# Without using any variables

print('The sum is %.2f' %(float(input('Enter First Number: ')) 
                       + float(input('Enter Second Number: '))))



#5 Python program to add two numbers without using + operator

def add_num(a,b):   #user-defined function
   if a!=b:
      return (a*a-b*b)/(a-b)
   else:
      return 2*a

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calling function
sum = add_num(num1, num2)

# print sum of numbers
print('The sum of numbers {0} and {1} is {2}'
                      .format(num1, num2, sum))



#6 Python program to add two numbers without using + operator

def add_num(a,b):   #user-defined function
   while b != 0:
      c = a & b   #using and operator
      a = a ^ b   #using XOR operator
      b = c << 1
   return a

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# calling function
sum = add_num(num1, num2)

# print sum of numbers
print('The sum of numbers {0} and {1} is {2}'
                      .format(num1, num2, sum))
