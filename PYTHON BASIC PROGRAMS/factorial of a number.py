General case for finding factorial
factorial(n) = n * factorial(n-1)

Factorial (n) =
1 * 2 * … * (n-1) * n
Or,
n * (n-1) * … * 2 * 1

The base case for finding factorial,
factorial(0) = 1
Or,
factorial(1) = 1
For example: The factorial of 4 is denoted as 4! = 1*2*3*4 or 4*3*2*1 = 24.
We can write it as,
4! = 4 * 3!
Similarly, we can write
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * 0!
0! = 1

Note:- The factorial of a negative number and float number doesn’t exist.
The value of 0! is 1, according to the convention for an empty product.



#1 Python program to find the factorial of a number

# take input
num = int(input("Enter number: "))

# check number is positive, negative, or zero
if num < 0:
   print('Factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
    # find factorial of a number
   fact = 1
   for i in range(1,num + 1):
       fact = fact*i
   print('The factorial of',num,'is',fact)



#2 Python program to find the factorial of a number

# take input
num = int(input("Enter number: "))

# check number is positive, negative, or zero
if num < 0:
   print('Factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
    # find factorial of a number
    fact = 1
    i = 1
    while(i <= num):
        fact = fact*i
        i = i+1
    print('The factorial of',num,'is',fact)




Python Math Factorial Program – math.factorial()

Syntax:-

math.factorial(num)
Parameter:-

num: Any positive integer. If the number is negative, or not an integer,
it returns a ValueError. If the value is not a number, it returns a TypeError
Returns:- factorial of desired number

#3 Python program to find the factorial of a number using math function

import math   #math module

# take input
num = 5

# find factorial of a number and display result
print('The factorial of',num,'is', math.factorial(num))



#4 Python program to find the factorial of a number using math function

import math   #math module

# take input
num = int(input("Enter number: "))

# find factorial of a number and display result
print('The factorial of',num,'is', math.factorial(num))


Factorial of a Number in Python using Recursion
Factorial of a number n is given by 1 * 2 * … * (n-1) * n and it’s denoted by n!
Example Factorial of 5! = 5*4*3*2*1 or 1*2*3*4*5

We can write it as,
5! = 5 * 4!
Similarly, we can write
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * 0!
0! = 1

So, in general, we can say that factorial of a positive integer n is the product of n and
factorial of (n-1).

n! = n * (n-1)!

Now, the problem of finding out factorial of (n-1) is similar to that of finding out factorial of n, but it is smaller in size. So, we have defined the solution of the factorial problem in terms of itself. We know that the factorial of 0 is 1 and similarly factorial of 1 is 1.
This can act as the terminating condition or the base case.


#5 Python program to find the factorial of a number using recursion

def recur_factorial(n):  #user-defined function
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

# take input
num = int(input("Enter number: "))

# check number is positive, negative, or zero
if num < 0:
   print('Factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
    # calling function
    print('The factorial of',num,'is', recur_factorial(num))



