#hoe to return multiple values from a function
from operator import add


def opp():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    sum = n1 + n2
    diff = n1 - n2  
    mul=n1*n2
    div=n1/n2               
    return sum, diff, mul, div


# sum, diff, mul, div = opp() #function call
# print("Sum is: ", sum)
# print("Difference is: ", diff)      
# print("Multiplication is: ", mul)
# print("Division is: ", div)

result=opp()
print("Result is: ", result) 