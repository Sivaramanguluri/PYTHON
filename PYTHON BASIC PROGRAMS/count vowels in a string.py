#1 Python program to count vowels in a string

def countVowels(string):
    num_vowels=0
    # to count the vowels
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

# take input
string = input('Enter any string: ')

# calling function and display result
print('No of vowels =',countVowels(string))



#2 Python program to count vowels in a string using while loop

def countVowels(string):
    count = 0
    num_vowels = 0
    
    # to count the vowels
    while count < len(string):
        if string[count] == "a" or string[count] == "e" or 
            string[count] == "i" or string[count] == "o" or 
             string[count] == "u" or string[count] == "A" or 
              string[count] == "E" or string[count] == "I" or 
               string[count] == "O" or string[count] == "U":
           num_vowels = num_vowels+1
        count = count+1
    return num_vowels

# take input
string = input('Enter any string: ')

# calling function and display result
print('No of vowels =',countVowels(string))



#3 Python program to count the number of each vowel

def countVowels(string):
    # make it suitable for caseless comparisions
    string = string.casefold()
      
    # make a dictionary with each vowel a key and value 0
    count = {i:0 for i in 'aeiou'}
      
    # to count the vowels
    for char in string:
        if char in count:
            count[char] += 1    
    return count

# take input
string = input('Enter any string: ')

# calling function and display result
print(countVowels(string))



Using a list and a dictionary Comprehension

#4 Python program to count the number of each vowel

def countVowels(string):
    # make it suitable for caseless comparisions
    string = string.casefold()
      
    # to count the vowels
    count = {x:sum([1 for char in string if char == x]) for x in 'aeiou'}
    print(count)

# take input
string = input('Enter any string: ')

# calling function
countVowels(string)
