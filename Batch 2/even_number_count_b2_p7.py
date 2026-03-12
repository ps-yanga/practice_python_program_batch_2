even = 0
for i in range (10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even += 1
print("The count of even number is", even)