#1 Python program to find factors of a number

# take inputs
num = int(input('Enter number: '))

# find factor of number
print('The factors of', num, 'are:')
for i in range(1, num+1):
    if(num % i) == 0:
        print(i, end=' ')




#2 Python program to find factors of a number

# take inputs
num = int(input('Enter number: '))

# find factor of number
print('The factors of', num, 'are:')
i = 1
while (i <= num):
    if(num % i == 0):
        print(i, end=' ')
    i = i+1




#3 Python program to find factors of a number using function

def find_factors(num):  #user-defined function
   print('The factors of', num,'are:')
   for i in range(1, num + 1):
       if num % i == 0:
           print(i, end=' ')

# take inputs
num = int(input('Enter number: '))

# calling function
find_factors(num)









