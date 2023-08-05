# day 06
# advanced topics in python 
#  summary

# regular expressions
# generators and iterators
# decorators
# context managers
# multithreading and multiprocessing

# datascience, machine learning, web devt

# Regular expressions

# \d matches any digit(0-9)
# \w matches any alphanumeric characters (a-z, A-Z. 0-9 and underscore)
# \s matches any whitespace character(space ,tab or newline)
# . matches any character except a new line
# * matches zero or more occurences of a proceeding charachters or group
# + matches one or more occurences
# ? matches zero or one
# [ ] within the sq brackets
# [^ ] not within
# ^  matches the start of a line
#  $ matches the end of a line


# Matching and searching= regular expression
# regex  re.match(), re.search() , re.findall()

# Ex1 Demonstrate regex , match first word,match group word, match all numbers

# import re 
# text = "hello, my name is Trisha Agaba. I am a programmer w 15 years of experience"

# # match first word
# match = re.search(r"\b\w+\b", text)

# if match:
#     print("Matches: ", match.group())

# matches = re.findall(r"\d+", text)
# print("Matches:", matches)

# Ex2 validate email format or email address jeff.geoff@gmail.com                                            
# import re

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern,email):
#         return True
    
#     else:
#         return False

# # Ex usage
# email1 = "jeff.geoff@gmail.com"
# email2 = "jeff.geoff@gmailcom"

# print(validate_email(email1))
# print(validate_email(email2))

# # Generator and iterators
# # 'yield' generator
# # iterator '__iter__' "__next__" iterator

# def factorial(n):
#     # return the factorial of a number
#     if n == 0:
#         yield 1
#     else:
#         # yield n*factorial(n-1)
#         fact=1

#         for i in range(1,n+1):
#             fact *= i
#             yield fact    
# # print factorial of a number from 1-10

# for i in range(1,10):
#     print(*factorial(i))

# Ex3
# Generate function that yields the sq of numbers from 1 to 10

# def squares():
#     for i in range(1,10):
#         yield i ** 2

# # create an iterator obj that yields the sq of numbers 1-10

# squares_iterator = squares()

# # print first 5 sqs of numbers frm 1-10

# for i in range(5):
#     print(next(squares_iterator))


# decorators @my_decorato
# Decorators in python allow you to modify the behaviour of functions or classes without 
# directly changing their source code+

def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner
    
@my_decorator
def outer_decorator():
    print("This is outer decorator")

outer_decorator()

Context managers- provide a way to manage resouces,
ensuring that they are properly set up and cleaned up.
They are commonly used with the 'with' statement


