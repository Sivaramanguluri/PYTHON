#1 Python program to check given number is an even or odd

# take inputs
num = 5

# check number is even or odd
if(num % 2 == 0):
 print('{0} is an even number'.format(num))
else:
 print('{0} is an odd number'.format(num))



#2 Python program to check given number is an even or odd

# take inputs
num = int(input('Enter a number: '))

# check number is even or odd
if(num % 2 == 0):
 print('{0} is an even number'.format(num))
else:
 print('{0} is an odd number'.format(num))



#3 Python program to check given number is an even or odd

# Returns true if num is even, else odd 
def oddEven(num):
 # check number is even or odd
 return (num % 2 == 0)

# take inputs
num = int(input('Enter a number: '))

# display result
if oddEven(num):
 print('{0} is an even number'.format(num))
else:
 print('{0} is an odd number'.format(num))



#4 Python program to print all even and odd numbers in given range 

# take range
start = int(input('Start: '))
end = int(input('End: '))

for num in range(start, end + 1):
    # check number is odd or not
    if num % 2 == 0:
        print(num, end = ':Even ')
    else:
        print(num, end = ':Odd ')



#5 Python program to print all even and odd numbers in given range 

# take range
start, end = 1, 100

for num in range(start, end + 1):
    # check number is odd or not
    if num % 2 == 0:
        print(num,end = ':Even ')
    else:
        print(num, end = ':Odd ')
