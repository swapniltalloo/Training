#move zeroes to the end
def moveZeroes(nums):
    index= 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)  
#list = [0, 1, 0, 3, 12]
 
