low=input("Enter a word: ")
casing=True
for char in low:
    if char.isalpha() and not ('a'<=char<='z'):
        casing=False
        break
print(casing)