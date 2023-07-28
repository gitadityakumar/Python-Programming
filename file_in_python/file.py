# create a empty text file
# in current directory
# fp = open('sales.txt', 'x')
# fp.close()

def fact(n):
    if(n == 0):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))