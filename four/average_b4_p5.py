# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average
numbers = []
while True:
    num = input("Enter number: ")
    if not num.isdigit():
        break
    numbers.append(int(num))
avg = sum(numbers) / len(numbers)
print(avg if numbers else 0)