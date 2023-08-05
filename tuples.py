#used to share items in a single variable
#are ordered and unchangeable

phones= ("iphone","samsung")
print(len(phones))
tuple1= (2,5,67,54)
print(tuple1)

#how to access tuples
print(tuple1[0])

#add items -first change to list, add then changr back
z= list(phones)
z.append("nokia")
phones = tuple(z)
print(phones)

#another way to add
new_phone = "bberry"
phones= phones + (new_phone,) #we add that comma because the tuple has a single element so you APPEND a trailing cooma

#add 2 tuples together
laptops= ("dell", "hp")
laptop = ("samsung",) #add coma if the tuple has one element

laptops += laptop
print(laptops)

Newstock = laptops +laptop
for y in phones:
    print(y)
    