# #works when you want to specify a variable type
# h = int(29)
# #Strings and multiline strings
# w= "Afternoon"
# y= """Iam offering ghjtngbdghnv fbggnbv
# gnmfgb"""

# #Strings as arrays
a= "Afternoon"
print(a[0]) #prints A

#Exercise one-use the len()function
print(len(a))

#Exercise two-ex using the for loop in a string

for i in range(len(a)):
    print (a[i])

#give an ex of slicing in strings
print(a[:3]) #this slice starts from the beginning of the list upto index 2

#Modify strings and concatenation
print (a.lower())
b= "Class"
d= a+b
print(d)
#format -works when one wants to combine a string and int
age=23
name= "Trish"
detail= "My name is {1} and I am {0}"
print(detail.format(age,name))

#boolean
print(20>50)
print(20==60)
r="Martha"
print(bool(r))

#exercise use a condition to show use of booleans
x=3
y=4
if x>y:
    print("True")
else:
    print("False")
#list -store many items using a single variable
afternoon = ["Trevor","Peter","Blessing"]
print(afternoon)

#duplicates in lists
afternoon = ["Trevor","Peter","Trevor","Blessing"]
print(afternoon)
print(len(afternoon))
#access list items using index
print(afternoon[1])#peter
print(afternoon[-3])#peter
print(afternoon[3:4])#prints blessing
print(afternoon[:3])#trevor,peter,trevor --dont include the third
print(afternoon[1:])#peter,trevor,blessing
#add items
afternoon.append("jane")
afternoon.insert(3,"ian")
#removing usung index
afternoon.pop[3]
afternoon.remove("blessing")
print(afternoon)
