myList=[5,2,9,7,5,6]
def search(x):
    for i in range(len(myList)):
        if myList[i]==x:
            return i
    return -1   
print(search(7)) #function call with argument, it will return the index of the element if found, otherwise it will return -1