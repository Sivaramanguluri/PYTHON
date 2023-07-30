#1 Python program to convert kilometers to miles

# take inputs
km = float(input('Enter distance in kilometers: '))

# conversion factor
conv_fac = 0.621371

# calculate Miles
mile = km * conv_fac

# display result
print('%0.2f kilometers is equal to %0.2f miles' %(km, mile))



#2 Python program to convert miles to kilometers

# take inputs
mile = float(input('Enter distance in miles: '))

# conversion factor
conv_fac = 1.60934

# calculate kilometers
km = mile * conv_fac

# display result
print('%0.2f miles is equal to %0.2f kilometers' %(mile, km))



