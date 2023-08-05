#storemultiple items in a single variable , unchangeable but one can remove and add new items

setone = {"rice","matooke","irish"}
print(setone)

#duplicates in sets
setone = {"rice","matooke","irish","irish"}
print(setone)

#exercise find length, datatype,accessing items of set,add items, add two sets
#Length and type
print(len(setone))
print(type(setone))

#add twosets
settwo = {"ariho","agaba"}
print(setone | settwo)

#accessing items -- you cant use an index
for y in setone:
    print (y)




