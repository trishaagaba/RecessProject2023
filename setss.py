#storemultiple items in a single variable 
#unchangeable but you can remove and add new items

setone = {"rice","matooke","irish"}
print(setone)

#duplicates in sets
setone = {"rice","matooke","irish","irish"}
print(setone)

#exercise find length,
#  datatype,accessing items of set,
# add items, 
# add two sets
#Length 
print(len(setone))
#and datatype
print(type(setone))

#add twosets
settwo = {"rogers","hadijah"}
print(setone | settwo)

#accessing items 
for y in setone:
    print (y)




