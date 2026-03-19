# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
numbers = []
while True:
    inp = input("Enter number: ")
    if not inp.isdigit():
        break
    numbers.append(int(inp))
print(max(numbers) if numbers else "No numbers")