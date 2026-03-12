# # #python is dynamically typed language
# # math=40
# # pi=3.14
# # name='SWAPNIL'
# # print(type(math))
# # print(type(pi))
# # print(type(name))    

# #typecasting
# print(2+2)
# print("2"+"2")
# print(int("2")+int("2"))
# print(str(2)+str(2))
# val1=input("Enter first number:")#by default input is string
# val2=input("Enter second number:")      
# print(val1+val2) #concatenation
# print(int(val1)+int(val2)) #addition

# # #type conversion
# print(int(3.14)) #float to int
# print(int(True))
# print(int(False))
# print(int(4))
# # print(int("3.14")) #error
# print(int("3")) #string to int
# print(int("swap")) #string to int ValueError: invalid literal for int() with base 10: 'swap'




#float
# print(float(3)) #int to float
# print(float(True))      
# print(float(False))
# print(float(3.14))      
# print(float("3.14")) #string to float
# print(float("swap")) #string to float ValueError: could not convert string to float: 'swap'
# print(float(50+2j)) #complex    to float error: can't convert complex to float  




# #Complex
# print(complex(3)) #int to complex
# print(complex(3.14)) #float to complex      
# print(complex(True))
# print(complex(False))
# print(complex("3.14")) #string to complex
# # print(complex("swap")) #string to complex ValueError: complex() arg is a malformed
# print(complex(50+2j)) #complex to complex
# print(complex("6"))
# print(complex(5,-3)) #real,imaginary    



# #Boolean if we want to convert any value to boolean then we can use bool() function but if we pass 0 in flot ,imaginary,boolean
#  then it will return False otherwise it will return True if we pass zero ,empty string and false value then it will return False otherwise it will return True

#WAP for simple interest
p=int(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=int(input("Enter time in years:"))    
si=(p*r*t)/100
print("Simple Interest is:",si)
#wap to centigrade to fahrenheit
c=float(input("Enter temperature in centigrade:"))  
f=(c*9/5)+32
print("Temperature in fahrenheit is:",f)
