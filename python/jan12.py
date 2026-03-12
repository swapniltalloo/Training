#nested if else statement
# 3 marks are given to a student in math,english and science. we have to find out which subject has the highest marks and which subject has the lowest marks


# math = int(input("Enter first value: "))
# eng= int(input("Enter second value: "))
# science = int(input("Enter third value: "))


# if(math>eng):
#     if(math>science):
#         print(math,"math","is greatest")
#     else:
#         print(science,"science","is greatest")
# else:
#     if(eng>science):
#         print(eng,"eng","is greatest")
#     else:
#         print(science,"science","is greatest")


# 3 marks are given to a student in math,english and science. we have to find out which subject has the highest marks and which subject has the lowest marks

math = int(input("Enter first value: "))
eng= int(input("Enter second value: "))
science = int(input("Enter third value: "))


if(math<eng):
    if(math<science):

        print(math,"math","is smallest")
    else:
        print(science,"science","is smallest")
else:
    if(eng<science):
       
        print(eng,"eng","is smallest")
    else:
        print(science,"science","is smallest")


        #else if ladder
# wap to accept percentage and if per>90 then print grade A, if per>80 then print grade B, if per>60 then print grade C, if per<60 then print grade fail

per=float(input("Enter percentage:"))
if per>=90:  
    print("Grade A")
elif per>=80 and per<90:
    print("Grade B")        
elif per>=60 and per<80:
    print("Grade C")    
else:
    print("Grade Fail")

