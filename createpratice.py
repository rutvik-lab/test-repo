# variables anddata types
# name = 'rutvik'
# age=18
# height=5.8

# name , age, height = "rutvik", 18, 5.8


# print(name, age, height)


# print(name , age , height)
 
# a = 5 
# b =10 
# # a,b = b,a
# # print(a,b)


# c = 10.89
# d = "rutvik"
# e = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


# length = int(input("enter a length :" ))
# breadth = int(input("enter a breadth :"))

# print("area of reactangle :")
# print(length*breadth)

# try:
#     length = int(input("Enter a length: "))
#     breadth = int(input("Enter a breadth: "))
#     print("Length:", length)
#     print("Breadth:", breadth)
# except ValueError:
#     print("Input is invalid")
# print(length*breadth)
 

# try:
#     celsius = float(input("enter temp in degree celsius:"))
#     fahrenheit = (celsius*(9/5)) + 32 
#     print("Celsius:", celsius)
#     print("Fahrenheit:", fahrenheit)
# except:
#     print("input is invalid")

# a = int(input("enter a number:"))
# if a %2 == 0 :
#     print("Given Number is Even.")
# else:
#     print("Given Number is Odd")

# a = 10 
# b = 40
# if a < b :
#     print("b is greater than a")
# else:
#     print("a is greater then b ")


# a = int(input("enter a number: "))
# if a % 15 == 0 :
#     print("divisible by 3 and 5 both ")
# elif a % 3 == 0:
#     print("divisible by 3")
# elif a % 5 == 0:
#     print("divisible by 5")
# else:
#     print("not divisible by 3 and 5")


# # checking voting eligibility
# Age = int(input("enter age of person: "))
# if Age < 18 :
#     print("you are not eligible for voting.")
# else:
#     print("you are eligible for voting.")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# # your logic here
# if max(a, b, c) == c :
#     print("c is greater")
# elif max(a, b, c) == b:
#     print("b is greater")
# else :
#     print("a is greater")
    

# a = int(input("Enter number: "))

# if a < 0 :
#     print("Given Number is NEgative")
# elif a == 0:
#     print("Given Number is Zero")
# else:
#     print("Given NUmber is Positive")

# a = int(input("enter the year: "))

# if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0) :
#     print("leap year")

# else :
#     print("not leap year")
    

# i = 1
# while i < 21 :
#     print(i)    
#     i += 1
    

    
# i = 0
# while i < 51 :
#     print(i)
#     i += 2
    
# n = int(input("enter a natural number: " ))
# x = (n *(n+1))//2
# print(x)


# number = int(input("Enter a number for the multipliaction table: "))

# i = 1
# while i <= 10:
#     product = number*i
#     print(f"{number} X {i} = {product}")
#     i += 1 

# number = int(input("Enter a number for the multipliaction table: "))
# i = 1
# for i in range(1,11):
#     x = number*i
#     y = (f"{number} X {i} = {x}")
#     print(y)



# a = int(input("first number: "))
# b = int(input("second number: "))
# c  = int(input("third number: "))
# d = int(input("fourth number: "))
# e  = int(input("fifth number: "))

# if max(a, b, c, d, e) == a:
#     print("a is greater")
# elif max(a, b, c, d, e) == b:
#     print("b is greater")
# elif max(a, b, c, d, e) == c:
#     print("c is greater")
# elif max(a, b, c, d, e) == d:
#     print("d is greater")
# else:
#     print("e is greater")


# print("Greatest number is:", min(a, b, c, d, e))



# float('-inf') → negative infinity (safe for finding maximum).
# float('inf') → positive infinity (safe for finding minimum).

# largest = float('-inf')


# for i in range(3):
#     num = int(input("Enter number: "))
#     if num > largest:
#         largest = num

# print("Largest:", largest)

# fruits = [ "a", "b", "c", "d", "e"]
# for fruit in fruits:
#     print(fruit)

#or 

# for i in range(len(fruits)):
#     print(fruits[i])

# total = 0 
# for i in range(5):
#     number = int(input(f"Enter a number {i+1}: "))
#     total += number
# average = total / 5

# print('Sum:', total)
# print('Average:', average)


# tuple = ("a","b","c","d")
# print(tuple)


# myset = {"apple", "bannana", "kiwi"}
# print(myset)


# myset1 = {"apple", "bannana", "kiwi", "apple"}
# print(myset1)

# mylist = ["apple", "banana", "cherry"]
# print(mylist)

# mylist.append("orange")
# print(mylist)


# mylist.remove("apple")
# print(mylist)



# students_marks ={
#     "Alice": 94,
#     "Bob": 43,
#     "Charlie": 94,
#     "David": 43,
#     "Eva": 86
# }

# for marks in students_marks.values():
#     print(marks)

# students_marks["rutvik"] ="100"

# print(students_marks)

# students_marks.update({"Eva": 78})
# print(students_marks)

# student_name = input("Enter student name to check: ")

# if student_name in students_marks:
#     print(student_name, "exists with marks:", students_marks[student_name])
# else:
#     print(student_name, " does not exist in the records: ")


# marks = students_marks.values()

# average_marks = sum(marks) // len(marks)

# print("Average marks of students:", average_marks)


# def my_function():
#     print(a**2)

# a = int(input("enter a number:"))

# my_function()



# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#          return True
#     if n % 2 == 0 :
#         return False
#     for i in range(3,int(n**0.5) + 1,2):
#         if n % i == 0:
#             return False
#     return True

# number = int(input("enter a nubmer: "))
# if is_prime(number):
#     print(number,"is a prime number")
# else:
#     print(number,"is not a prime number")

# number  = [ 212, 234, 3343, 3343]
# def is_largest():
#     x = max(number)
#     print("Largest number is: ", x )
# is_largest()

# or

# def is_largest():
#     return max(number)

# largest = is_largest()
# print("Largest number is:", largest)


# def my_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0 
#     for char in s :
#         if char in vowels:
#             count += 1
#     return count

# text = str(input("ENTERE A STRING: "))
# print("Nmber of vowels in the string: ", my_vowels(text))


# def to_celsius(S):
#     celsius = (5/9)*(S - 32)
#     return celsius

# S = float(input("enter tempature in fahrenheit: "))
# print("tempature in fahrenheit is: ", S)
# print("tempature in celsius: ",to_celsius(S))


# with open("myfile.txt", "w") as file:
#     file.write("line 1: Hello World!\n")
#     file.write("Line 2: Python is fun.\n")
#     file.write("Line 3: Learning file handling.\n")
#     file.write("Line 4: Writing lines to a file.\n")
#     file.write("Line 5: Task completed successfully.\n")

# print("File 'myfile.txt' created and 5 lines written successfully!")


# my_file = open("myfile.txt")
# print(my_file.read())
# my_file.close()


# with open ("myfile.txt") as my_file:
#     for x in my_file:
#         print(x) 

# with open("myfile.txt", "a") as f:
#     f.write("Now line 6 coming soon!")

# with open("myfile.txt") as f :
#     content = f.read()
#     word = content.split()
#     word_count = len(word)
# print("Number of words in the file:", word_count)   
#                                                                    



# def factorial(n):
#     if n < 0:
#         return "factorial not defined for negative number"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
    
# n = int(input("Enter a number: "))
# print(factorial(n))


# def is_prime(n):
    # if n<= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range (3, int(n**0.5) + 1,2 ):
#         if n % i == 0:
#             return False
#     return True
    
# number = int(input("enter a nubmer: "))
# if is_prime(number):
#     print(number,"is a prime number")
# else:
#     print(number,"is not a prime number")


# import math

# def nCr(n, r):
#     if r > n:
#         return 0 
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
# n = int(input("Enter a number n: "))
# r = int(input("Enter a number r: "))

# print("nCr:", nCr(n, r))

# import math 

# def nCr(n, r):
#     return  math.comb(n, r)
# n = int(input("Enter a number n: "))
# r = int(input("Enter a number r: "))
# print(nCr(n, r))

# def greet(name="User"):
#     print(f"Hello, {name}! Welcome aboard")

# greet("Rutvik")
# greet()


# def introduce(name="guest", age=18, city="unknown"):
#     print(f"my name is {name}, I am {age} years old, from {city}.")

# introduce("rutvik", 19, "Halol")
# introduce("anya")
# introduce()

# def add_number(*args):
#     total = 0
#     for num in args:
#         total += num 
#     return total

# print(add_number(1, 2, 3, 4))

# def greet_all(*args):
#     for name in args:
#         print(f"Hello, {name}! 👋")


# greet_all("Rutvik", "Anya", "Raj")


# def introduce(greeting, *args):
#     for name in args:
#         print(f"{greeting}, {name}!")

# introduce("Good Morning", "Rutvik", "Anya", "Raj",)

# def multipty_all(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result

# print(multipty_all(2, 3, 4, 5))
# print(multipty_all(5, 19, 10))

# def sub_all(*args):
#     if not args:
#         return 0
#     result = args[0]
#     for num in args[1:]:
#         result -= num
#     return result

# print(sub_all(10, 2,4))

# def divide_all(*args):
#     if not args:
#         return None
#     result = args[0]
#     for num in args[1:]:
#         if num == 0:
#             return "Division by zero not allowed!"
#         result /= num
#     return result

# print(divide_all(100, 2, 5))   


# def stu_pro(name, **kwargs):
#     print(f"Name: {name}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# stu_pro("Rutvik", age=18, city="Pune",grade="A+")

# def con_app(**kwargs):
#     defaults = {"theme": "light", "notifications": True}
#     defaults.update(kwargs)
#     return defaults

# print(con_app(theme="dark", font="Arial")) 

# def order(*items, **details):
#     print("Items ordered:", items)
#     print("Order details:", details)

# order("Pizza", "Coke", address="Mumbai", payment="UPI")

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# greet(name="Rutvik", age=18, goal="IIT Bombay")

# def intro(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# intro("Hello", "World", name="Rutvik", exam="JEE")

# def student_info(course="JEE", **kwargs):
#     print(f"Course: {course}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# student_info(name="Rutvik", rank="Top 100", Target="AIR 1")
# student_info(name="Rajesh", rank="Top 100", Target="AIR 2")

# def find_largest(number):
#     largest = number[0]
#     for num in number:
#         if num > largest:
#             largest = num

#     return largest
# nums = [ 12, 32, 23, 434, 4343]
# print("Largest number is:", find_largest(nums))



# def find_max(nums):
#     return max(nums)
# nums = [12, 343, 43, 545]
# print("Largest number is:", find_max(nums))

# memo = {}
# def fibonacci(n):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#     memo[n] = result
#     return result
# for i in range(10):
#     print(fibonacci(i), end=" ")

# def reverse_string(s):
#     return s[::-1]
# text ="BharatBrain"
# print("Original:", text)
# print("Reversed:", reverse_string(text))

# def reverse_string(S):
#     reversed_str = ""
#     for char in S:
#         reversed_str =char + reversed_str
#     return reversed_str
# print(reverse_string("Rutvik"))


# def count_vowels_consonants(s):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     consonant_count = 0
#     for char in s:
#         if char.isalpha():
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1

#     return vowel_count, consonant_count 

# text = input("Enter a text or word: ")
# v, c = count_vowels_consonants(text)

# print("Vowels:", v)
# print("Consonants:", c)



def count_vowels_consonants(S):
    vowels = "aieouAEIOU"
    vowels_count = sum(1 for ch in S if ch in vowels)
    consonant_count = sum(1 for ch in S if ch.isalpha() and ch not in vowels)
    return vowels_count, consonant_count
print(count_vowels_consonants("Bharatbrain"))