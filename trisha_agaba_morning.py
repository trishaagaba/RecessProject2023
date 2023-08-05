# # inheritance

# class Animal:
#     def __init__(self,name)
#         self.name = name

    
#     def eat(self):
#         print(f"{self.name} is eating...")


# class Vehicle:
#     def __init__(self,brand,color):
#         self.brand =brand
#         self.color = color

#     def display_info(self):
#         super().display_info()
#         print("No. of wheels: ". self.num_wheels)


# demonstrate using inheritance calc area of circle n rect

# class Shape:
#     def __init__(self,length):
#         self.length = length
       

# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__(radius)
#         self.radius = radius
        
#     def area(self):
#         print(f"{self.radius*self.radius*3.14}")
#     # print(f"The area is : {self.r})
        

# class Rect(Shape):
#     def __init__(self,length,width):
#         super().__init__(length,width)
#         self.width = width
#         self.length= length

        
#     def area(self):
#         return self.length*self.width  

# circle2 = Circle(5)
# circle2.area()
# # Method overriding,-occurs when a derived class(child class)provides
# #  its own implementation of a method that is already defined in its subclass
# #  method overloading - allows a class to have multiple methods within the same name
# #  but diff parameters
# # polymorphism allows you to write code that can work in different objects

# class Shape:
#     def calculate_area(self):
#         pass

# class Rect(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def calc_area(self):
#         return self.length*self.width
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calc_area(self):
#         return 3.14*self.radius**2
    
#     def calc_circumference(self):
#         return 2*3.14*self.radius
    
# # create shape obj
# rect1= Rect(5,5)
# circle1 = Circle(5)

# # Calc and display area
# print("Area" , rect1.calc_area())

# # overloading

# class Calculator:
#     def add(self,x,y):
#         return x+y
    
#     def add(self, x,y,c):
#         return x+y+c
    
#     # create object
# calculator1 = Calculator()

# # display output
# print(calculator1.add(1,2))

# Abstraction
# Allows you to focus on essential features and hide them from unnecessary details
# 



# Create a receipt printing program with a GUI interface,
# a more advanced detail earns u more points
#In this program we do not at units to our quantity and cuurency to our price
    
import tkinter as tk
from tkinter import messagebox

def print_receipt():
    # Get input values from the entry fields
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    # Validate the input fields
    if customer_name == "":
        messagebox.showerror("Error", "Please enter name of the customer.")
        return

    if item_name == "":
        messagebox.showerror("Error", "Please enter name of the item.")
        return

    if quantity == "" or not quantity.isdigit():
        messagebox.showerror("Error", "Please enter a quantity that is valid.")
        return

    if price == "" or not price.replace(".", "").isdigit():
        messagebox.showerror("Error", "Please enter a price that is valid.")
        return

    # The ttl cost is then calculated
    total_cost = float(quantity) * float(price)

    # Create the receipt message
    receiptmsg = f"Customer Name: {customer_name}\n"
    receiptmsg += f"Item selected: {item_name}\n"
    receiptmsg += f"Quantity: {quantity}\n"
    receiptmsg += f"Price of items: {price}\n"
    receiptmsg += f"Total Cost of items: {total_cost}\n"

    # The receipt message in a message box is then displayed
    messagebox.showinfo("Receipt", receiptmsg)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create labels and entry fields for input
customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_label.pack()
customer_name_entry = tk.Entry(window)
customer_name_entry.pack()

item_name_label = tk.Label(window, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(window)
item_name_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Price of items:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Then Create the Print Receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Start the Tkinter event loop
window.mainloop()


    




