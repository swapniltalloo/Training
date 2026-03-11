# mylist=["prasant","Ashish","Satyarth","Rohit","swapnil"
#         ]
# # print(mylist)
# # print(type(mylist))
# # print(mylist[0])
# # print(mylist[1])        
# # print(mylist[-1])
# # print(mylist[1:4])
# # print(mylist[1:])   
# # print(mylist[:4])
# # print(mylist[:])    
# # print(mylist[1:4:2])
# # print(mylist[::-2])


# mylist.append('harsh')
# mylist.append('JOY')
# print(mylist)
# mylist.insert(1,'priyanshu')    
# print(mylist)
# mylist.remove("harsh")  
# print(mylist)  

# newlist=mylist.copy()#cloning
# print(mylist)
# print(newlist)



# mylist=[['Swapnil',"Talloo"],['24.00'],[9630506293,"yyy"]]
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])     
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])



# list1=['Swapnil','Talloo']
# print(list1*2)

# list2=[50,60]
# print(list1+list2)


#particular index delete
# mylist=["prasant","Ashish","Satyarth","Rohit","swapnil"
#         ]   
# del mylist[1]
# print(mylist)
# mylist.clear()
# print(mylist)   


# name ="swapnil"
# print(name)
# myname=list(name)#tyoecasting string to list
# print(myname)


# mylist=[22,45,67,667,98]
# mylist.sort()#sort in ascending order
# print(mylist)
# mylist.sort(reverse=True)#sort in descending order
# print(mylist)
# #we know that list should contain same type of data but if we have different type of data then we can not sort it else it will give typeerror



# math=19
# phy=19
# print(id(math))#it will give the memory address of the variable math
# print(id(phy))#it will give the memory address of the variable phy      
# # in python small integers are cached and reused, so math and phy point to the same memory location for the value 19. This is an optimization technique used by Python to save memory and improve performance.  



# mylist=[22,45,67,667,98]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))


#there membership operator 
#  1) in ,  2) not in
# name="swapnil"
# print('s' in name)
# print('z' in name)

# for i in range(1,6):
#     print(i)
    
# for i in range(6):
#     print(i)
# for i in range(2,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(10,1,-2):
#     print(i)

# for i in range(2,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# check whether a entered number is +ve ,-ve or 0


# num=int(input("enter num:"))
# if num>0:
#     print(num,"is a positive number")
# if num<0:
#     print(num,"is a negative number")
# if num==0:
#     print(num,"is zero") 

#Wap to accept days and check whether it is weekday or weekend


day=(input("enter day:"))
if day=="saturday" or day=="sunday"or day=="SATURDAY" or day=="SUNDAY":
    print(day,"is a weekend")   
else:    
    print(day,"is a weekday")

#Wap to accept three paper marks and calculate total,percentage and if percantage is greater than 60 then he/she is eligible for placement

# paper1 = int(input("Enter marks for Paper 1: "))
# paper2 = int(input("Enter marks for Paper 2: "))
# paper3 = int(input("Enter marks for Paper 3: "))

# total_marks = paper1 + paper2 + paper3
# percentage = (total_marks / 300) * 100


# print(f"\nTotal Marks: {total_marks}")
# print(f"Percentage: {percentage:.2f}%")


# if percentage > 60:
#     print("Status: Eligible for placement")
# else:
#     print("Status: Not eligible for placement")



#WAP to accept 5 diffent value in 5 different var and check max value and print by using "simple if statement"
# WAP to accept 5 different values in 5 different var 
# and check max value using "simple if statement"

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))

if a >= b and a >= c and a >= d and a >= e:
    print("Max value is:", a)

if b >= a and b >= c and b >= d and b >= e:
    print("Max value is:", b)

if c >= a and c >= b and c >= d and c >= e:
    print("Max value is:", c)

if d >= a and d >= b and d >= c and d >= e:
    print("Max value is:", d)

if e >= a and e >= b and e >= c and e >= d:
    print("Max value is:", e)

