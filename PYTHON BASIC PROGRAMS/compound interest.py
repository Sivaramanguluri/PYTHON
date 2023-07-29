principal = 1000
rate = 10
time = 5
number = 6

rate = rate/100
amount = principal * pow( 1+(rate/number), number*time)
ci = amount - principal

print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)




#2 Python program to find compound interest

# store the inputs
principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times that 
                            interest is compounded per year: '))

# convert rate
A = P(1 + r/n) ^ (n * t)
Where,
A is the future value of the investment/loan, including interest
P is the principal amount
r is the annual rate of interest
n is the number of times that interest is compounded per unit t and
t is the time the money is invested (number of years)

The above formula gives the total amount. To find the compound interest use,
Compound interest = A – P

#1
rate = rate/100

# calculate total amount
amount = principal * pow( 1+(rate/number), number*time)
# calculate compound interest
ci = amount - principal

# display result
print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)





#3 Python program to calculate compound interest using function

def compound_interest(principal, rate, time, number):
    # calculate total amount
    amount = principal * pow( 1+(rate/number), number*time)
    return amount;

# store the inputs
principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times that 
                            interest is compounded per year: '))

# convert rate
rate = rate/100

# calling function 
amount = compound_interest(principal, rate, time, number)
# calculate compound interest
ci = amount - principal

# display result
print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)                     
