a = b = c = d = e = f =12
print(c)

x,y,z = 1, 2, 76 #represented as a typle
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data= 1, 2, 76
x,y,z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [1, 2, 76]
#data_list.append(15) #crashes because unpack to 3 variables with 4 items
p,q,r = data_list
print(p)
print(q)
print(r)
