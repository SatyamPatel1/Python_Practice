# 45+10=89 56/4=4 34*3=99
a = int(input("Enter first digit: "))
opr = input("Enter operator: ")
b = int(input("Enter second digit: "))

if opr == "+":
    if a == 45 and b == 10:
        print("89")
    else:
        print(a+b)
elif opr == "-":
    print(a-b)
elif opr == "*":
    if a == 34 and b == 3:
        print("99")
    else:
        print(a*b)
elif opr == "/":
    if a == 56 and b == 4:
        print("4")
    else:
        print(a/b)
else:
    print("invalid operator")
