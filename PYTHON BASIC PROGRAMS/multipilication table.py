#1 Python program to print multiplication table

# take inputs
num = int(input('Display multiplication table of: '))

# print multiplication table
for i in range(1, 11):
    print ("%d * %d = %d" % (num, i, num * i))




#2 Python program to print multiplication table

# take inputs
num = int(input('Display multiplication table of: '))

# print multiplication table
i = 1
while i <= 10:
    print ("%d * %d = %d" %(num, i, num * i))
    i = i+1




#3 Python program to print multiplication table from 1 to 10

print('Multiplication table from 1 to 10: ')
for i in range (1,11):
    print('\n')
    for j in range(1, 11 ):
        print (i*j, end='\t')



#4 Python program to print multiplication table in range

# take inputs
print('Display multiplication table')
start = int(input('Start: '))
end = int(input('End: '))

# print multiplication table
for i in range (start, end+1):
    print('\n\nMultiplication table of %d\n' %(i))
    for j in range(1, 11 ):
        print('%d * %d = %d\t' %(i, j, i*j))
