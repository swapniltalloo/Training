# my_dict = {
#     "name":"Swapnil Talloo",
#     "professional": "developer",
#     "empid": 1001
# }
# print(my_dict)
# print(type(my_dict))



# my_dict={
#     101:"prashant",
#     102:"ashish",
#     "103":"Swapnil",
#     "104":"Manu",
#      101: "mono",
#      104: "joy" 
# }
# print(my_dict)

#with the help of key we have to print values

# a=my_dict[102]
# print(a)

#we will replace old value by new value
# my_dict[102]="daya"
# print(my_dict)

#only print key x=0,1

# for x in my_dict:
#     print(x)


# only print values
# for x in my_dict.values():
#     print(x)


# #  both key and values
# for x,y in my_dict.items():
#     print(x,y)


# # new key and value
# my_dict["mobile-no"]=9630506293
# print(my_dict)



mydict={
    101:"Swapnil",
    "professional":"developer",
     "empid" :1001

}
mydict.pop(101)
print(mydict)
#pop() method remove pair by specific key name

