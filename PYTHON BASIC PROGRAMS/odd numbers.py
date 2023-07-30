#1 Python program to check given number is an odd or not

# take inputs
num = 3

# check number is odd or not
if(num % 2 != 0):
 print('{0} is an odd number'.format(num))
else:
 print('{0} is not an odd number'.format(num))



#2 Python program to check given number is an odd or not

# take inputs
num = int(input('Enter a number: '))

# check number is odd or not
if(num % 2 != 0):
 print('{0} is an odd number'.format(num))
else:
 print('{0} is not an odd number'.format(num))



#3 Python program to check given number is an odd or not using function

# Returns true if num is odd, else not odd 
def isOdd(num):
 # check number is odd or not
 return (num % 2 != 0)

#take inputs
num = int(input('Enter a number: '))

# display result
if isOdd(num):
 print(num,"is an odd number")
else:
 print(num,"is not an odd number")



#4 Python program to print all odd numbers in given range 

# take range
start = int(input('Start: '))
end = int(input('End: '))

print('All odd number in the range')

for num in range(start, end + 1):
    # check number is odd or not
    if num % 2 != 0:
        print(num, end = " ")



#5 Python program to print all odd numbers in given range 

# take range
start, end = 1, 100

print('All odd number in the range')

for num in range(start, end + 1):
    # check number is odd or not
    if num % 2 != 0:
        print(num, end = " ")







