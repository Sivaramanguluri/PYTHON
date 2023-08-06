# Python program to print vowels in a string using for loop

def printVowels(string):
    # to print the vowels
    for char in string:
        if char in "aeiouAEIOU":
            print(char, end=', ')
    return char

# take input
string = input('Enter any string: ')

# calling function
printVowels(string)
