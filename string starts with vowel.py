Python to Check if Word Starts with Vowel
In this program, we use the if-else statement to check if a word starts with a vowel or consonant. First, we have taken the string. Then,
check if the string starts with a vowel in python using the if-else statement. Finally, the result will be displayed on the screen.




#1 Python program to check if string starts with vowel

# take inputs
string = input('Enter the String: ')

# vowel alphabet
vowel = 'aeiou'

# check string starts with vowel or consonant
if string[0].lower() in vowel:
   print(string,'starts with vowel',string[0])
else:
   print(string,'starts with consonant',string[0])



Write a Program Which Extracts all the Words Which Starts with the Vowel in Python

#2 Python program to extract the words that start with a vowel from a list

# take list
words = ['String','Egg','know','Open','program','animal']

# vowel alphabet
vowel = 'A','E','I','O','U','a','e','i','o','u'

# check words and display result
print([w for w in words if w.startswith(vowel)])



#3 Python program to accept strings starting with a vowel
  
# Function to check if first character is vowel
def Vowel(string):
  
    if (string[0] == 'A' or string[0] == 'a'
        or string[0] == 'E' or string[0] == 'e'
        or string[0] == 'I' or string[0] == 'i'
        or string[0] == 'O' or string[0] == 'o'
        or string[0] == 'U' or string[0] == 'u'):
        return 1
    else:
        return 0
  
# Function to check
def check(string):
    if (Vowel(string)):
        print('Accept')
    else:
        print('Not Accept')

# take input
character = input('Enter the String: ')

# calling function and display result
check(character)



