# # Exercise 1: claculate the area and circumference of a circle



# class Circle:

#     def __init__(self, radius):

#         self.radius = radius



#     def area(self):

#         return 3.14 * self.radius * self.radius

    

#     def circumference(self):

#         return 2 * 3.14 * self.radius

    

# circle1 = Circle(radius=7)

# print(circle1.area())

# print(circle1.circumference())



# # exercise 2: 

# # calculate and display employees(0.5 of salary) bonuses

# # employee 1 salary = 150000

# # employee 2 salary = 230000



# class Employee:

#     def __init__(self, name, salary):

#         self.name = name

#         self.salary = salary

#         self.bonus = 0.5 * self.salary

    

#     def details(self):

#         print("Name: ", self.name)

#         print("Salary: ", self.salary)

#         print("Bonus: ", self.bonus)



# #creating objects
# employee1 = Employee("Trisha", 40000)
# employee2 = Employee("Agaba", 20000)

# employee1.details()
# employee2.details()





#3. ENCAPSULATION

"""

Goals of encapsulation are;

1. For Data hiding
2. protect objects from ext changes
3. For code organization and modularity

"""



# # Example: with bank accounts

# class BankAccount:

#     def __init__(self, account_number, balance):
#         self._account_number = account_number # encapsulates the account number attribute
#         self._balance = balance # encupsuates the balance attribute

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if self._balance >= amount :
#             self._balance -= amount
#         else :
#             print("Insufficient funds")

#     def get_balance(self):
#         return self._balance

    

# #create new object
# my_bank = BankAccount(78, 25000)

# #access the bank object and modify its properties
# print(my_bank.get_balance())

# my_bank.deposit(80000)
# print(my_bank.get_balance())
# my_bank.withdraw(12000)
# print(my_bank.get_balance())


# #Exercise 2. Convert temperature from celsius to fahrenheit


# class Temperature:

#     def __init__(self, celsius):
#         self._celsius = celsius
#         self._fahrenheit = (celsius * 9 / 5) + 32


#     def get_fahrenheit(self):
#         return self._fahrenheit


# #creating an object
# my_temperature = Temperature(25)
# print(my_temperature.get_fahrenheit())





# ASSIGNMENT 1. Show encapsulation with employee informatiom to give a pay incrementatio
#Salary with employee informatiom to new_salary eg from 850000 to 1000000



class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def newsalary(self):
        newsalary = self._salary + (self._salary + 150000)
        return newsalary

    
    def details(self):
        print( self._name)
        print("My old Salary is: ", self._salary)
        print("My New Salary is: ", self.newsalary())



#creating an object

my_employee = Employee("Trisha", 850000)
my_employee.newsalary()
my_employee.details()



    