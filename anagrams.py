# check anagrams
#listen and silent
#in python
# 
name1=input("Enter first string:")    
name2=input("Enter second string:")
if sorted(name1)==sorted(name2):
    print("Anagrams")
else:   
    print("Not Anagrams")