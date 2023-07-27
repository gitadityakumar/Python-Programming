# Range Method
# for a in range(0, 5):
# print(a)


# for a in range(0, 100, 10):  # in range we can define the step we can also use list  items
# print(a)

# now lets write the program to find PrimeNumber in python

n = int(input("Enter the number you wanna check: "))
isPrime = True
if n > 1:
    for i in range(2, n):
        if (n % i == 0):
            isPrime = False
            break
if (n <= 1):
    print("no is not prime ")
elif (isPrime):
    print("number is prime")
else:
    print("no is not prime")
