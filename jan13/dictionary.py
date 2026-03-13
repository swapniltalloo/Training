
def add_key_value(d, key, value):
    d[key] = value
    return d
mydict = {}
add_key_value(mydict, "name", "Arnav")
add_key_value(mydict, "empid", 1001)
print(mydict)