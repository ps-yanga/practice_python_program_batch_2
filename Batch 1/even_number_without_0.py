num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(num2 - num1 - 1):
    num1 += 1
    if num1 % 2 == 0 and num1 % 10 != 0:
            print(num1, end=",")