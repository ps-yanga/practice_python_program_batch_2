# even number (1-100)
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
for i in range(num2-num1-1):
    num1+=1
    if num1 % 2 == 0:
        print(num1, end=",")