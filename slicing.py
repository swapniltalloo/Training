# name="swapniltalloo"
# # name2="anishgupta"
# print(name[0])
# print(name[1])            
# print(name[-1])
# print(name[1:4])  
# print(name[1:])
# print(name[:4])       
# print(name[:])
# print(name[1:4:2])
# print(name[::-1])
# # print(name2[::-1])


# s="python is a programming language" 
# # print(s.find("programming")) #index of first character of programming
# # print(s.find("python")) 
# # print(s.find("java")) #if substring is not found then it will return -1

# # d="swapnil","mono","naman"
# # m='|'.join(d)
# # print(m)



# # print(s.lower())
# # print(s.upper())
# # print(s.swapcase())
# # print(s.title())
# # print(s.capitalize())



# print('Subject Marks:')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} Math={}".format(phy,chem,math))
# print("physics{0} chemistry{1} Math{2}".format(phy,chem,math))
# print("physics={x} chemistry={y} Math={z}".format(x=phy,y=chem,z=math))
# total=phy+chem+math
# print("total",f"{total}")
# print("Rollno=","7".zfill(4))


# print('prashantjha777'.isalnum())   # True
# print('prashantjha'.isalpha())      # True
# print('777f'.isdigit())# False
# print('sdsdsdsd'.islower())# True
# print(''.islower())# False
# print('PRASHANT'.isupper())# True
# print('My Name Is Prashant'.istitle())# True
# print(''.istitle())# False
# print(' '.isspace())# True
# print("Hello".startswith("He"))# True
# print("Hello".endswith("lo"))#  True


# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)



name="Swapnil"
data=['a','e','i','o','u']
v=0
c=0

for i in name:
    if i in data:
    # if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
     v=v+1
    else:
       c=c+1

print(v)
print(c)  
