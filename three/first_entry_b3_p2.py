# # Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
print("ALL NUMBERS:",*numbers)
print("NO DUPLICATE:",*dict.fromkeys(numbers))
