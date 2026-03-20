name=input("enter your fullname:")
pascal_case="".join(word.capitalize() for word in name.split())
print(pascal_case)