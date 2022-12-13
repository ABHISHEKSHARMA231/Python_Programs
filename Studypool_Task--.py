# Create a program that allows the user to do some basic functions.
# First, ask the user if they would like to find out sqrt, log or factorial of a number, then return the results.
# Here is the sample output:
# Welcome to the simple math helper.
# What would you like to calculate?
# 1. Sqrt
# 2. Log
# 3. Factorial
# > 1
# Enter the number to sqrt:
# >9
# 3
# =====================================================================================================================
import math

print('\n-->Welcome to simple maths helper.\n-->What would you like to calculate?')

a,b,c='1','2','3'
print('\t'+a+'-Sqrt','\n\t'+b+'-log','\n\t'+c+'-Factorial')

z=input('Enter your choice here:-')

if z==a:
    x = int(input('Enter the number to calculate:-'))
    print(math.sqrt(x))

elif z==b:
    x = int(input('Enter the number to calculate:-'))
    Q=str(math.log(x,10))
    W=str(math.log(x))
    print(' Here is your log with base of 10-->'+Q,'\n Here is your natural log-->'+W)

elif z==c:
    x = int(input('Enter the number to calculate:-'))
    print(math.factorial(x))

else:
    print('😊Sorry you have enter wrong choice')
print()


