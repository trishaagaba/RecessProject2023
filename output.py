# # imput('prompt')
# # ex

# name = input("Enter your  name: ")
# print("My name is, " + name)

# # ex 2
# number= int(input("Enter a value: "))
# product = number * 10
# print(product)

# # ex3 - multiple inpu
# s,r,w = map(int(input("Enter the values: ").split()))
# print("The values are: ", end = " ")
# print(s,r,w)

# # how to capture input from tuple
# W = (2,4,5,6,8)
# print("Current tuple")
# print(W)

# E= list(W)
# E.append(int(input("Enter new value: ")))
# W = tuple(E)
# print("updated tuple")
# print(W)

# Capturing input 
myList = ["trisha","martha","jenny"]
# myList= list(map(
#  input("Enter your required names: ").split()))
myList.append(input("Enter your required names: ").split())
mySet = set(map(int,input("Enter the set values: ").split()))

print(myList)
print(type(myList))
print(mySet)
print(type(mySet))

