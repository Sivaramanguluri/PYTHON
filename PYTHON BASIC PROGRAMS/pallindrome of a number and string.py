Palindrome String in Python | If the reverse of the string is the same string then the string is called palindrome string.
Some examples of palindromic words are redivider, noon, civic, radar, level, rotor, kayak, reviver, racecar, redder, madam, and refer. The palindrome number is also based on the palindrome string.
The reverse of a number that is equal to the same number is called a palindrome number.



#1 Python program to check if string is Palindrome

# take inputs
string = input('Enter the string: ')

# find reverse of string
i = string
reverse = ''
while(len(i) > 0):
    if(len(i) > 0):
        a = i[-1]
        i = i[:-1]
        reverse += a

# compare reverse to original string
if(reverse == string):
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')



#2 Python program to check if number is Palindrome

n= int(input('enter a number'))
temp=n
reverse=0
while (n!=0):
    digit=n%10
    reverse= reverse*10+digit
    n=n//10
if reverse==temp:
    print("pallindrome")
else:
    print("not pallindrome")




Python program using Slicing
Syntax of slicing operation:- str(num) [::-1]

#3 Python program to check if string is Palindrome

# take inputs
string = input('Enter the string: ')

# find reverse of string
reverse = str(string)[::-1]

# compare reverse to original string
if(reverse == string):
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')



#4 Python program to check if string is Palindrome using recursion

def isPalindrome(s):  #user-defined function
    s = s.lower()
    length = len(s)
    
    if length < 2:
        return True
    
    elif s[0] == s[length-1]:
        # Call is pallindrome form substring(1,length-1)
        return isPalindrome(s[1: length-1])
 
    else:
        return False
 
# take inputs
string = input('Enter the string: ')

# calling function and display result
reverse = isPalindrome(string)
if reverse:
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')
























