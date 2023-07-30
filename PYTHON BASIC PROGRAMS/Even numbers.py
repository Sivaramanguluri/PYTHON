#1 Python program to check given number is an even or not

# take inputs
num = 10

# check number is even or not
if(num % 2 == 0):

 print('{0} is an even number'.format(num))
else:
 print('{0} is not an even number'.format(num))



#2 Python program to check given number is an even or not

# take inputs
num = int(input('Enter a number: '))

# check number is even or not
if(num % 2 == 0):
 print('{0} is an even number'.format(num))
else:
 print('{0} is not an even number'.format(num))



#3 Python program to check given number is an even or not using function

# Returns true if num is even, else not even 
def isEven(num):
 # check number is even or not
 return (num % 2 == 0)

#take inputs
num = int(input('Enter a number: '))

# display result
if isEven(num):
 print(num," is an even number")
else:
 print(num," is not an even number")



#4 Python program to print all even numbers in given range 

# take range
start, end = 1, 10

print('All even number in the range')

for num in range(start, end + 1):
    # check number is even or not
    if num % 2 == 0:
        print(num, end = " ")



#5 Python program to print all even numbers in given range 

# take range
start = int(input('Start: '))
end = int(input('End: '))

print('All even number in the range')

for num in range(start, end + 1):
    # check number is even or not
    if num % 2 == 0:
        print(num, end = " ")
