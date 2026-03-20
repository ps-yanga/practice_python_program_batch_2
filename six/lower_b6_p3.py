lower=input("Enter a sentence: ")
casing=""
for char in lower:
    if 'A' <= char <= 'Z':
        casing+=chr(ord(char)+32)
    else:
        casing+=char
print(casing)