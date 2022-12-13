# Write a Python (or R) program that asks the user to enter an integer (X), then:
# Evaluate and print the equation Y=8X²+ 1, for X values from -5 to 5
# using the range function and for loop
'========================================================================================================'
def print_factors(x):
   print("\n--->The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print('->>',i)

# To take input from the user
X = int(input("\t\nEnter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if X > 1:
    # check for factors
    for i in range(2, X):
        if (X % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(X, "\nis not a prime number")
    print('\t\t----Here we check factors if number is not prime------\t')
    print_factors(X)
else:
    print(X, "is a prime number")

# Evaluate and print the equation Y=8X²+ 1, for X values from -5 to 5
print('\n\t\t--------Here the Evaluation---------\t')
for x in range(-5,5+1,1):
    print('->>',8*(x**2)+1)


print('\t\t\t---------THANK YOU ALL-----------')




