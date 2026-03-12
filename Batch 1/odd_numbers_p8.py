# count of odd numbers
odd = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        odd += 1
print("THE COUNT OF ODD NUMBER IS", odd)