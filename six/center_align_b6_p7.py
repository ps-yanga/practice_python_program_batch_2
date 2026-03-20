center=input("Enter sentence: ")
width=int(input("Enter a width: "))
padding=width-len(center)
left=" "*(padding//2)
right=" "*(padding//2)
result=left+center+right
print(result)