first = int(input("enter your first number"))
operator = input("enter operator(+,-,*,/,% : ")
second = int(input("enter second number"))

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
elif operator == "/":
    print(first / second)
else:
    print("please choose the correct option")
