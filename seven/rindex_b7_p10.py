word=input("Enter word:")
substr=input("Enter substring: ")
pos=-1
for i in range(len(word)):
    if word[i:i+len(substr)]==substr:
        pos=i
if pos!=-1:
    print(pos)
else:
    print("Not found ")