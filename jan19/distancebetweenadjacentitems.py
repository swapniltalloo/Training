def distance_between_adjacent_items(lst):
    distances = []
    sum = 0
    for i in range(len(lst) - 1):
        distance = abs(lst[i] - lst[i + 1])
        sum=sum+distance
    return sum
lst = [10,11,7,12,14]
result = distance_between_adjacent_items(lst)
print(result)  

