# print("hello world")


    
# # day 9 

# # Python automatically converts
# # a to int
# a = 7
# print(type(a))
 
# # Python automatically converts b to float
# b = 3.0
# print(type(b))
 
# # Python automatically converts c to float as it is a float addition
# c = a + b
# print(c)
# print(type(c))



# day 10

# variable=int(input())
# variable=float(input())

# a=input("Enter the name: ")
# print(a)

# a = input("Enter your name: ")
# print("My name is", a)

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(x  + y)

# print(int(x) + int(y))


# day 11

# If our string has multiple lines, we can create them like this:

# a = """Lorem ipsum dolor sit amet,
# # consectetur 'adipiscing' elit,
# # sed do eiusmod tempor incididunt
# # ut labore et dolore magna aliqua."""
# print(a)

# name = "Harry"
# friend = "Rohan"
# anotherFriend = 'Lovish'
# apple = '''He said, 
# Hi Harry
# hey I am good
# "I want to eat an apple'''
 
# print("Hello, " + name)
# # print(apple) 
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# # print(name[5]) # Throws an error
# print("Lets use a for loop\n")
# for character in apple:
#     print(character)

# day 12

# fruit = "Mango"
# mangoLen = len(fruit)
# print(mangoLen)
# # print(fruit[0:4]) # including 0 but not 4
# # print(fruit[1:4]) # including 1 but not 4
# # print(fruit[:5])
# # print(fruit[0:-3])
# # print(fruit[:len(fruit)-3])
# print(fruit[-1:len(fruit) - 3])
# print(fruit[-3:-1])



# pie = "ApplePie"
# print(pie[:5])      #Slicing from Start
# print(pie[5:])      #Slicing till End
# print(pie[2:6])     #Slicing in between
# print(pie[-8:])     #Slicing using negative index


# Strings are arrays and arrays are iterable. Thus we can loop through strings.


# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)



# day 13
# strings are immutable 

# a = "Rutvik "
# print(len(a))
# print(a.upper())
# print(a.lower())

# the rstrip() removes any trailing characters.

# a="!!!!!Rutvik!!!!!!!"
# print(a.rstrip("!"))
# print(a.replace("Rutvik", "parmar"))

# a1= "rutvik parmar 1223"
# print(a1.split(" "))

# capitalize()

# name = "paarmaAr"
# print(name.capitalize())
# name1 ="rUTBik"
# print(name1.capitalize())

# a2 = "Welcome to the pc"
# print(a2.center(80))

# a2 = "Welcome to the pc"
# print(a2.count("e"))

# # str1 = "Welcome to the Console !!!"
# # print(str1.endswith("!!!"))

# # The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.


# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("Daniel"))

# # The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Daniel"))
# output ValueError: substring not found
 
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.


# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

# str1 = "Welcome"
# print(str1.isalpha())

# str1 = "Welco00me"
# print(str1.isalpha())

# The islower() method returns True if all the characters in the string are lower case, else it returns False.

# str1 = "hello world"
# print(str1.islower())


# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())

# str1 = "We wish you a Merry Christmas \n"
# print(str1)
# print(str1.isprintable())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# str1 = "World Health Organization\n" 
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# The isupper() method returns True if all the characters in the string are upper case, else it returns False

# str1 = "WORLD HEALTH ORGANIZATION" 
# print(str1.isupper())

# The endswith() method checks if the string starts with a given value. If yes then return True, else return False

# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())

# The title() method capitalizes each letter of the word within the string.
# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.title())







# day 14


# a = int(input("Enter your age:  "))
# print("Your age is:", a )
# # Conditional operators 
# # >, <, >=, <=, ==, !=
# # print(a>18)
# # print(a<=18)
# # print(a==18)
# # print(a!=18)
  

# if(a>18):
#     print("You can drive ")
# else:
#     print("You cannot drive ")

# num = 0
# if (num < 0):
#     print("Number is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")


# num = 1856
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")



# day 15

# import time
# timestamp = time.strftime('%H:%M:%S:%p:%u')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# timestamp = time.strftime('%p')
# print(timestamp)
# timestamp = time.strftime('%u')
# print(timestamp)



# day 16

# # match variable_name:
# #             case ‘pattern1’ : //statement1
# #             case ‘pattern2’ : //statement2
# #             …            
# #             case ‘pattern n’ : //statement n


# # x = 4
# # # x is the variable to match
# # match x:
# #     # if x is 0
# #     case 0:
# #         print("x is zero")
# #     # case with if-condition
# #     case 4 if x % 2 == 0:
# #         print("x % 2 == 0 and case is 4")
# #     # Empty case with if-condition
# #     case _ if x < 10:
# #         print("x is < 10")
# #     # default case(will only be matched if the above cases were not matched)
# #     # so it is basically just an else:
#     # case _:
#     #     print(x)



# # day 19

# # for i in range(1,101,1):
# #     print(i ,end=" ")
# #     if(i==50):
# #         break
# #     else:
# #         print("Mississippi")
# # print("Thank you")

# # for i in [2,3,4,6,8,0]:
# #     if (i%2!=0):
# #         continue
# #     print(i)


# # day 20


# # def function_name(parameters):
# #   pass
# #   # Code and Statements


# # def name(fname, lname):
# #     print("Hello,", fname, lname)

# # name("Sam", "Wilson")


# def calculateGmean(a, b):
#   mean = (a*b)/(a+b)
#   print(mean)

# def isGreater(a, b):
#   if(a>b):
#     print("First number is greater")
#   else:
#     print("Second number is greater or equal")

# def isLesser(a, b):
#   pass
  

# a = int(input("enter :"))
# b = int(input( "enter:"))
# isGreater(a, b)
# calculateGmean(a, b)
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# c = int(input( "enter:"))
# d = int(input( "enter:"))
# isGreater(c, d)
# calculateGmean(c, d)
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)

# day 42

