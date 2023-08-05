# EXCEDPTION HANDLING and FILEHANDLING

# Exceptions
# 1.IndexError
# 2.NameError
# 3.IOError
# 4.ImportError
# 5.ZeroDivisionError
# 6.FileNotFoundError
# 7.ImportError
# 8.TypeError

# ZeroDivisionError
try:   
    x= 20/0
except ZeroDivisionError:
    print("Cannot divide by zero")

# IndexError
try:
    y=[1,2,3]
    print(y[4])
except IndexError:
    print("Index out of bounds")

# importerror
# Value error
# TypeError
try:
    num = int(input("Enter a number: "))
    result = 100/num
    import unknownvariable

except ValueError:
    print("Invalid input")

except ImportError:
    print("No module named 'unknownvariable'")


# TypeError
try:
    result1= "hello" + 7
except TypeError:
    print("Unsupported operand type for +: 'str' and 'int'")

# FileNotFoundError - We obtain this exception when we are trying to read a file
#  that does not exist - With Reading a file
try:
    file = open("nonexistentfile.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")

# Permission error with Writing to a file
try:
    file = open("example.txt", "w")  # Open the file in write mode
    file.write("Hello My name is Trisha")  # Write content to the file
    file.close()  # Close the file
except PermissionError:
    print("Permission denied.")






