A year is called leap year if the year is divisible by four, except for the years which are divisible by 100 but not divisible by 400.
Therefore, the year 2000 was a leap year, but the years 1700, 1800, and 1900 were not.
The complete list of leap years in the first half of the 21st century is 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036,
2040, 2044, and 2048.



#1 Python program to check year is a leap year or not

# take input
year = int(input('Enter a year: '))

# check leap year or not
if (year % 400) == 0:
    print('{0} is a leap year'.format(year))
elif (year % 100) == 0:
    print('{0} is not a leap year'.format(year))
elif (year % 400) == 0:
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))




#2 Python program to check year is a leap year or not

# take input
year = int(input('Enter a year: '))

# check leap year or not
if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print('{0} is a leap year'.format(year))
        else:
            print('{0} is not a leap year'.format(year))
    else:
        print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))




#3 Python program to check year is a leap year or not using function

def checkYear(year):   #user-defined function
    # check leap year or not
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

# take input
year = int(input('Enter a year: '))

# function call and display result
if(checkYear(year)):
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))




#4 Python program to check leap year or not in a single line

def checkYear(year):
    # check leap year or not
    return ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))
	
# take input
year = int(input('Enter a year: '))

# function call and display result
if(checkYear(year)):
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))




#5 Python program to check leap year or not using calender

def checkYear(year):
    # check leap year or not
    import calendar
    return(calendar.isleap(year)) 	
# take input
year = int(input('Enter a year: '))

# function call and display result
if(checkYear(year)):
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))









