remove=input("Enter a word: ")
suffix=input("Enter a suffix to remove: ")
if len(remove)>=len(suffix) and remove[-len(suffix):]==suffix:
    remove=remove[:-len(suffix)]
print(remove)