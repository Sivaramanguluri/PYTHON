#1 Python program to multiply two number

# take inputs
num1 = 3
num2 = 5

# calculate product
product = num1*num2

# print multiplication value
print("The Product of Number:", product)


#2 Python program to multiply two number

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# calculate product
product = num1*num2

# print multiplication value
print("The Product of Number: %0.2f" %product)


#3 Python program to multiply two numbers using function

def product_num(num1, num2):  #user-defind function
    num = (num1 * num2)   #calculate product
    return num   #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# function call
product = product_num(num1, num2)

# print multiplication value
print("The Product of Number: %0.2f" %product)


#4 Python program to multiply two number using recursion

def product_num(num1,num2):   #user-defined function
    if(num1<num2):
        return product_num(num2,num1)
    elif(num2!=0):
         return(num1+product_num(num1,num2-1))
    else:
         return 0

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# function call
product = product_num(num1, num2)

# print multiplication value
print("The Product of Number:", product)


#5 Python program to multiply two number using for loop

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# calculate product
product = 0
for i in range(1,num2+1):
    product=product+num1

# print multiplication value
print("The Product of Number:", product)


