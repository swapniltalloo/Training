val1=4
val2=5
# temp=val1
# val1=val2
# val2=temp
# print("which was 4 now ",val1)
# print("which was 5 now ",val2)

val1=val1+val2
val2=val1-val2  
val1=val1-val2
print("which was 4 now ",val1)
print("which was 5 now ",val2)

#reverse A seven digit number

num=1234567
rev=0   
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10 
print("rev ",rev)