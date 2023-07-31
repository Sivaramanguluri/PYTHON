#1 Python program to find prime factors of a number
 
# take inputs
num = int(input('Enter number: '))

# find prime factors
for i in range(2, num + 1):
    if(num % i == 0):
        isPrime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isPrime = 0
                break
        if (isPrime == 1):
            print(i,end=' ')
print('are the prime factors of number',num)



#2 Python program to find prime factors of a number
 
# take inputs
num = int(input('Enter number: '))

# find prime factors
i = 1
while(i <= num):
    count = 0
    if(num % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
        if (count == 2):
            print(i,end=' ')
    i = i + 1
    
print('are the prime factors of number',num)



#3 Python program to find prime factors of a number using function

def primeNumber(num):  # user defind function
    # find prime factors
    for i in range(2, num + 1):
        if(num % i == 0):
                isPrime = 1
                for j in range(2, (i //2 + 1)):
                    if(i % j == 0):
                        isPrime = 0
                        break
                if (isPrime == 1):
                    print(i,end=' ')
    print('are the prime factors of number',num)

# take inputs
num = int(input('Enter number: '))

# calling function
primeNumber(num)



