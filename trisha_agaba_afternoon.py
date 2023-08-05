

# EXERCISE 1 : Lists
# 1
people = ["james", "fatuma", "derrick", "fred"]
# 2
people[0]= "tim"
print (people[0])
# 3
people.append("jim")
print(people)

# 4
print(people[-1])

# 5
people.pop(3)
print(people)

# 6
print(people[-1])

# 7
people= ["trish", "conrad", "rogers", "owen","ben"]
print(people[2:4])

# 8 write list of countries and make a copy of it
country = ["USA", "Russia","Mexico", "Egypt"]
countrycopy = country.copy()
print(countrycopy)

# 9 write python program to loop through
for countries in country:
    print("countries")

# 10 write list of animals names and sort thrm in both ascending and descending order
animals = ["dog", "cat", "cow", "goat"]
# ascending
animals.sort()
print(animals)
# descending
animals.sort(reverse=True)
print(animals)

# 11 using the list write python program to output only animal names with the letter 'a in them
for animal in animals:
    if "a" in animal:
        print(animal)

# 12 write two lists, one containg yo first' names and other second, join the two lists
first_names = ["owen", "trisha", "conrad","rogers" ]
second_names = ["kata.", "jones", "smith", "agaba"]
print(first_names + second_names)

# EXERCISE TWO
# 1
phones = ("samsung", "iphone", "techno", "redmi")
print("My fav brand is" ,phones[1])

# 2
print(phones[-3])

# 3
phoneslist = list(phones)

phoneslist[1] = "itel"
phonestuple = tuple(phoneslist)
print(phonestuple)

# 4
phonelist = list(phones)
phonelist.append("Huawei")
phone2= tuple(phonelist)
print(phone2)

# 5
for phone in phones:
    print(phone)

# 6
deletinglist = list(phones)
deletinglist.pop(0)
newphones = tuple(deletinglist)
print(phone)

# 7
tuple3 = tuple(["Kampala", "Jinja", "Kabale", "Gulu"])
print(tuple3)

# 8
names = ("Trisha", "Martha")
first_name, last_name = names
print(first_name)
print(last_name)

# 9
tuple3 = tuple(["Kampala", "Jinja", "Kabale", "Gulu"])
print(tuple3[1:])

# 10
first_name = "Trisha"
sec_name = "Agaba"
full_name = first_name + sec_name
print(full_name)

# 11
colors = ("red", "pink","blue")
multiplied = colors*3
print(multiplied)

# 12
thistuple = (1,3,7,8,7,5,4,6,8,5)
numberoftimes = thistuple.count(8)
print(numberoftimes)


# EXERCISE THREE

# 1
beverages = set(("juice", "water", "smirnoff"))
print(beverages)

# 2
beverages.add("porridge")
beverages.add("tea")
print(beverages)

# 3
mySet = {"oven","kettle","microwave","refrigerator"}
print("microwave" in mySet)

# 4
mySet.remove("kettle")
print(mySet)

# 5
for item in mySet:
    print(item)

# 6
mySet = {"oven","kettle","microwave","refrigerator"}
mySecondSet = {"cup","glass"}
x= set(mySecondSet)
print(mySet.union(x))

# 7
ages= {4,6,3}
first_name= {"Trisha", "Esther", "Michaela"}
joint_set = ages.union(first_name)
print(joint_set)

# EXERCISE 4
# 1
x = 6
y= "Trisha"

print(str(6) +y)

# 2
txt=" Hello, Uganda!"
print(txt.strip())

# 3
print(txt.upper())

# 4
replaced = txt.replace('U', 'V')
print(replaced)

# 5
y= "I am proudly Ugandan"
print(y[1:4])

# 6
x = ''


           

# 6
p= "All 'Datascientists' are cool"
print(p)



# EXERCISE 5
# 1
shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40
}
print(shoes["size"])

# 2
shoes["brand"] = "Adidas"

# 3
shoes["type"] = "sneakers"

# 4
keys = shoes.keys()
print(keys)

# 5
values = shoes.values()
print(values)

# 6
if "size" in keys:
        print("Exists in keys")

# 7
for i in shoes:
     print(shoes[i])
# for key,value in shoes.items():
#         print(f"{key} : {value}")

# 8
shoes.pop("color")
print(shoes)
# shoes.__delitem__("color")

# 9
shoes.clear()
print(shoes)

# 10
person = {
     "name" :"Agaba Trisha",
     "age" :21,
     "hobby" : "Shopping"
}
other_person = person.copy()

# 11
nestedfamily = {
                # "child1" : { "name" : "Brenda", "year"=8},
                # "child2" : { "name" : "Ben", "year"=9},
                # "child3" : { "name" : "Hana", "year"=4}}
     "first" : other_person, "second": other_person, "hobby" : other_person}
print(nestedfamily["first"]["hobby"])

# 

                  










