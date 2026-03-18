#find the insertion of three arrays
def find_insertion(arr1, arr2, arr3):   
    for i in (arr1):
        if i  in arr2 and i  in arr3:
            return i
    return None
arr1 = [1,2,3]
arr2 = [3,4,5]  
arr3 = [3,6,7]
result = find_insertion(arr1, arr2, arr3)   
print(result)  # Output: 3  