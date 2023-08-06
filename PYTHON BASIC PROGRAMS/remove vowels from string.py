#1 Python program to remove all vowels from string

def removeVowels(string):
    vowel = 'aeiou'
    #find vowel in string
    for ch in string.lower():
        if ch in vowel:
            #remove vowels
            string = string.replace(ch, '')

    #print string without vowels
    print(string)

string = input('String: ')
removeVowels(string)



Python Code to Remove Vowels from a String

#2 Python program to remove all vowels from string

import re  #importing regular expression

# function for remove vowels from string
def removeVowels(string):
    return (re.sub('[aeiouAEIOU]','',string))

string = input('String: ')
print(removeVowels(string))



#3 Python program to remove all vowels from string

# function for remove vowels from string
def removeVowels(string):
    remove_str = ''.join([x for x in string if x.lower() not in 'aeiou'])
    #print string without vowels
    print(remove_str)

string = input('String: ')
removeVowels(string)


#4 Python program to remove all vowels from string

# function for remove vowels from string
def removeVowels(string):
    vowels = 'AEIOUaeiou'
    #remove vowels
    translate = str.maketrans(dict.fromkeys(vowels))
    remove_str = string.translate(translate)
    #print string without vowels
    print(remove_str)

string = input('String: ')
removeVowels(string)



