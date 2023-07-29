#1 Python program to swap two variables using temporary variable

# take inputs
a = input('Enter the value of a: ')
b = input('Enter the value of b: ')

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# create a temporary variable and swap the value
temp = a
a = b
b = temp

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)


#2 Python program to swap two numbers using + and – operator

# take inputs
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = a + b
b = a - b
a = a - b

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)


#3 Python program to swap two numbers using * and / operator

# take inputs
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = a * b
b = a / b
a = a / b

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)


#4 Python program to swap two numbers using XOR operator

# take inputs
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = a ^ b
b = a ^ b
a = a ^ b

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)


#5 Python program to swap two numbers using 
# bitwise and arithmetic operators

# take inputs
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swapping of the numbers
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)


