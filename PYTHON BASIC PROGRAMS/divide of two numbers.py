#1 Python program to divide two numbers

# take inputs
num1 = 10
num2 = 2

# Divide numbers
division = num1/num2

# print value
print("The division of {0} and {1} is {2}"
               .format(num1,num2,division))


#2 Python program to divide two numbers

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Divide numbers
division = num1/num2

# print value
print("The division of {0} and {1} is {2}"
                .format(num1,num2,division))


#3 Python program to divide two numbers using function

def div_Num(num1, num2):  #user-defined function
    div = (num1/num2)   #divide numbers
    return div   #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# function call
division = div_Num(num1, num2)

# print value
print("The division of {0} and {1} is {2}"
                .format(num1,num2,division))


#4 Python program to divide two numbers using recursion

def div_Num(x,y): #user-defined function
    if (y==0):
        return 0;
    elif (x-y==0):
        return 1;
    elif (x<y):
        return 0;
    else:
        return (1+div_Num(x-y,y));

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# function call
division = div_Num(num1, num2)

# print value
print("The division of {0} and {1} is {2}"
               .format(num1,num2,division))
