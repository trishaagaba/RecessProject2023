# #Lecture two
# #


#CONTROL FLOW
# #if gen_gender_sex:
# #    print('Male')
# #else:
#   
 # print('Female')

#   #  if condition1:
#  #       print('True')
# #elif condition2:
# #print('False')
# #else:
# #print('Falsess')

# #example
# # age = 19
# # if age<18:
# #     print ("You are underage")
# # elif age>=18 and age <=65:
# #     print("Youre an adult")
# # else:
# #     print("Youre a senior citizen")
# #  # loops for, while

        
# #  for i in sequence:
# #     print i
# #     #


# # cars = ["tesla","jeep","ford","toyota","bmw"]
# # for car in cars:
# #     print (car)

# # fruits = ["mango","orange","pear","guava"]
# # fruit_count = 0
# # while fruit_count < len(fruits):
# #     print(fruits[fruit_count])
# # for fruit in fruits:
# #     print(fruit)    

# # x=0
# # while x<5:
# #     print(x)
# #     x+=1

#     # break and continue statements

# for number in range(1,10):
#     if number == 5:
#         continue  #it will skip 5 and continue with the rest, 
#     #if it is Break, it stops on the 5
#     print(number)
#     if number ==8:
#         break
#     print(number)


# # Exception handling(try,except,finally)
# # try block: youre telling python to monitor a block
# # and find the error there
# # and handle it using except,it raises an exception for ex, if
# # i have written a wrong password

# # Except: what should be printed if the block in try hhas an error
# # Finally: runs 

# try: 
#     x= 10/0
#     print(x)
# except ZeroDivisionError:
#     print('Error: Division by Zero')
# finally:
#     print('This is always executed')

# try:
#     x= int(input("Enter a number"))
#     y =int(input("Enter another number"))
#     print (x/y)
# except ValueError:
#     print("invalid value, enter another value")
# except Exception as e:
#     print("An error has occurred",str(e))

# #example 5
# #dict is a dictionary{}

# emotion = {
#     "happy" : "Iam glad to hear youre happy",
#     "sad": "I am sorry to hear that youre feeling sad",
#     "angry" : "Take a deep breathe and stay alive",
#     "fearful" : "I understand that fear can be challenging",
#     "disgusted ": "Thats unfortunate"
#     }
# #prompt the userto enter their feeling
# user_emotion = input("How are you feeling today?")

# user_emotion = user_emotion.lower()

# if user_emotion in emotion:
#     print(emotion[user_emotion])

# else:
#     print("iam sorry i dont understand your emotion")

    # Exercise
    # write program to ask students about their mental health

State = {
   1 : "You need to talk to your close family and friends about how youre feeling",
   2:"You are strong ",
   3:"You are loved",
   4:"Take a walk",
   5:"Hang in there, it gets easier",
   6:"Hang in there, it gets easier with time ",
   7:"Hang in there, it gets much easier than you think",
   8:"Keep up the good work youre doing",
   9:"Great,keep up the good work youre doing on yourself",
   10:"Share your happiness with other"
}

userinput = input("On a scale of 1-10,kindly rate your mental health ")
userinput = int(userinput)

try: 
    if userinput in State:
        print(State[userinput])
    else:
         print ("Please enter a value btn 1-10")
        

except ValueError:
    print ("Please enter a correct valuevalue btn 1-10")
finally:
    print("Thank you for your feedback")
