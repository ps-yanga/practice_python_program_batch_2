word=input("Enter a word: ")
substr=input("Enter a substring: ")
pos=0
found=False
for i in range(len(word)):
    if word[i:i*len(substr)]==substr:
        pos=i
        found=True
        break
if found:
    print(pos)
else:
    print("Not found")