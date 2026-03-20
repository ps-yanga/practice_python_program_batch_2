swap=input("Enter a word(s): ")
case=""
for char in swap:
    if 'A' <= char <= 'Z':
        case+=chr(ord(char)+32)
    elif 'a' <= char <= 'z':
        case+=chr(ord(char)-32)
    else:
        case+=char
print(case)