# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))
dups = {n for n in numbers if numbers.count(n) > 1}
print("Duplicates:", *dups)