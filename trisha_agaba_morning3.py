# Logical 'NOT'
# Assign value "="
# Subtract and assign '-='
# *=
# /=

# Membership operators
# 'in' operator : checks if a value exits in a sequence
# 'not in'

# identity operator
# 'is' = checks if two values are the same

# addition
# x= 50+45
# print(x)

# subtraction
# x=50-45
# print(x)

# multiplication
# x=50*4
# print(x)

# division
# x=50//8

# exponention
# d= 2 ** 4



# example and assignment
# create a simple calc to add,subtr,multiply, divide 

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

def main():
    print('Trish simple calc')
    number1 = float(input("Enter the first no."))
    number2 = float(input("Enter the sec no."))
    operator = input("Enter the operator: (' +, *, /, -')")

    if operator == '+':
        result=add(number1,number2)
    elif operator == '-':
        result=add(number1,number2)
    elif operator == '-':
        result=subtract(number1,number2)
    elif operator == '*':
        result=multiply(number1,number2)
    elif operator == '/':
        result=divide(number1,number2)
    else:
        print('Invalid operator')
        return
    print("The result is " ,result)

if __name__ == '__main__':
        main()



    # print("Addition: " , add(a,b))
    # print("Subtraction: " , subtract(a,b))
    # print("Division: " , divide(a,b))
    # print("Multiplication: " , multiply(a,b))
    
    # tkinter learning

    # create a simple calc prog with a gUI interface. make your title of the calc progr window w your name 


