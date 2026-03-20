cap=input("Enter a word: ")
casing=""
if cap:
    casing=cap[0].upper()+cap[1:].lower()
print(casing)