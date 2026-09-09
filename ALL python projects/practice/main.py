#data center is like a gramer it is all of the way you can type in python such as strings , integer , float , boolean 
#String is words , we need to use "" for it 
#Integer is numbers , we wont use "" for it
#Float is numbers that have decimal place , its called floating point number , like: 3234.24
#Boolean is used when the answer you wanna get is True or False
# len's job is to calculate the numbers of character of your string , like: print(len("ilia")) the conclusion is 4
#print(len(input("what is your name? ")))
#input is used when you want users write somthing , like: input("what is your name? ")
#subscript is when you want to get one letter from the world you wrote and it always starts with zero , like: print("hello"[0])
#sugestion for numbers :you can use under score _ bitween your numbers to easilly undrestand what number it is,like use 32_356_935 instead of 32356935
#hint : you cant use  diffrent types of data together , like: print("your name is" + 4 + "characters.")
#type is when you want to undrestand wich type of data you have, like:print(type(12)) the result will be class int
#converting data types is when you need diffrent types of data to work together so we need to convert all of them to one ,downbelow is the example
#  example:# name = 12 
# new_name = str(name)
# print("ilia" + new_name)
#hint in python when you divide a number it always becomes a float data , like 6 / 3 = 2.0

#practice
#two_digit_number = input("type a two digit number")
#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]
#result = int(first_digit) + int(second_digit)
#print(result)

#f_string is used when you wanna simply convert diffrent type of data into one type of data , you need to use curly braces {} and put f behind double couts f"

#another practice
#height =input("enter your height in m . ")
#weight =input("enter your weight in kg . ")
#new_height = float(height)
#new_weight = float(weight)
#print(new_weight / new_height ** 2 )

#age = input("what is your current age? ")
#age_as_int = int(age)
#years_remaining = 90 - age_as_int
# months_remaining = years_remaining * 12
#weeks_remaining = years_remaining * 52
#days_remaining = years_remaining * 365
#result = print(f"you have {years_remaining} years , {months_remaining} month , {weeks_remaining} weeks , {days_remaining} days left")
#print(result)

#print("welcome to the rollercoaster.")
#height = int(input("what is your hight in cm.\n"))
#if height>=120:
#    print("you can ride the rolercoaster.")
#else:
#    print("sorry , you have to grew taller before you ride")

#print("welcome to the odd or even calculator.")
#number = int(input("please type your number."))
#if number % 2 ==0:
#    print("your number is even.")
#else:
 #   print("your number is odd.")

#print("welcome to the rollercoaster.")
#height = int(input("what is your height in cm.\n"))
#if height>=120:
#    print("you can ride the rollercoaster")
#    age = int(input("what is your age\n"))
#    if age<12:
#        print("please pay $5")
#    elif age<=18:
#        print("please pay $7")
#    else:
#        print("please pay $12")
#else:
#    print("sorry , you have to grew taller before riding it.")

#print("welcome to the bmi calculator.")
#height = float(input("what is your height in m?\n"))
#weight = float(input("what is your weight?\n"))
#result = round(weight / height ** 2)
#if result<18.5:
#    print(f"your bmi is {result} , and you are underweight.")
#elif result<25:
#    print(f"your bmi is {result} , and you have a normal weight.")
#elif result<30:
#    print(f"your bmi is {result} , and you are overweight")
#elif result<35:
#    print(f"your bmi is {result} , and you are obese.")
#else:
#    print(f"your bmi is {result} , and you are clinically obese.")

#print("welcome to the leap year finder.")
#year = int(input("wich year do you want to check?\n"))
#if year % 4 ==0:
#    if year % 100 ==0:
#        if year % 400 ==0:
#            print("this is a leap year.")
#        else:
#            print("not a leap year")
#    else:
#          print("this is a leap year.")
#else:
#      print("not a leap year.")

#print("welcome to the roller coaster.")
#height =int(input("what is your height in cm?\n"))
#bill = 0
#if height>120:
#    print("you can ride the rollercoaster.")
#    age =int(input("how old are you?\n"))
#    if age<12:
#       bill = 5
#       print("child tickets are $5")
#    elif age<=18:
#        bill = 7
#        print("teenager tickets are $7")
#    elif age>=45 and age<=55:
#        print("everything is going to be ok , have a free ride on us!")
#    else:
#        bill = 12
#        print("adult tickets are $12")
#   photo = input("do you want photos Y or N ?")
#   if photo== "Y":
#        bill+= 3
#   print(f"your final biil is ${bill}")
#else:
#    print("sorry , you cant ride it.")

#bill = 0
#print("welcome to the looloo piza.")
#size =input("what size pizza do you want? S , M or L \n")
#peperoni =input("do you want extra peperoni? Y or N\n")
#cheese =input("do you want extra cheese? Y or N\n")
#if size == "S":
#    bill+=15
#elif size == "M":
#    bill+= 20
#else:
#    bill+=25
#if peperoni == "Y":
#   if size == "S":
#        if size == "M" "L":
#             bill+=3
#    bill+=2
#if cheese == "Y":
#    bill+=1
#    print(f"your totall bill is ${bill}")

#print("welcome to the love calculator.")
#name1 = input("what is your name?\n")
#name2 = input("what is their name?\n")
#combined = name1 + name2
#lower_case_string = combined.lower()
#t = lower_case_string.count("t")
#r = lower_case_string.count("r")
#u = lower_case_string.count("u")
#e = lower_case_string.count("e")
#true = t + r + u + e
#l = lower_case_string.count("l")
#o = lower_case_string.count("o")
#v = lower_case_string.count("v")
#e = lower_case_string.count("e")
#love = l + o + v + e
#love_score = int(str(true) + str(love))
#love_score = int(love_score)
#if love_score<10 or love_score>90:
#    print(f"your score  is {love_score}, you go together like coke and pepsi.")
#elif love_score>=40 and love_score<=50:
#    print(f"your score is {love_score}, you are alright together.")
#else:
#    print(f"your score is {love_score}.")

#import random
#import my_module   it doesnt work
#random_integer = random.randint(1, 10)
#print(random_integer)
#print(my_module.pi)

#import random 
#coin =random.randint(0 , 1)
#if coin==1:
#    print("heads")
#else:
#    print("tails")

#import random
#names_string= input("Give me everybopdy's name, seperated by a comma. \n")
#names = names_string.split(",")
#times = len(names)
#random_names =random.randint(0, times - 1)
#paying_person = names[random_names]
#print(paying_person + " is the person who will pay.")

#print("welcome to the treasure map!.")
#row1 = ["⬜" , "⬜" , "⬜"]
#row2 = ["⬜" , "⬜" , "⬜"]
#row3 = ["⬜" , "⬜" , "⬜"]
#map = [row1 , row2 , row3]
#print(f"{row1}\n{row2}\n{row3}\n")
#position =input("where do you want to put the treasure? ")
#horizonal = int(position[0])
#vertical = int(position[1])
#selected_place = map[vertical - 1]
#selected_place[horizonal - 1] = "X"  how did this work?
#rint(f"{row1}\n{row2}\n{row3}\n")

#student_heights = input("input a list of student heights. ").split()
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
#print(student_heights)
#sum = sum(student_heights)
#len = len(student_heights)
#answer = sum / len
#print(round(answer))
#total_height = 0
#for x in student_heights:
#    total_height+=x
#print(total_height)
#total_number = 0 
#for n in student_heights:
#    total_number+=1
#print(total_number)
#print(round(total_height / total_number))

#student_scores = input("input a list of student scores.\n").split()
#for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
#print(student_scores)    
#highest_score = 0
#for score in student_scores:
#    if score > highest_score:
#        highest_score = score
#print(f"the highest sore is {highest_score}.")

#total = 0 
#for number in range(1, 101):
#    total+=number
#print(total)
 
#total_even = 0
#for even in range(1, 101):
#    if even % 2 ==0:
#        total_even += even
#print(total_even)
# we could solve this in the under solution as well 
#total_even2 = 0
#for even in range(2, 101, 2):
#    total_even2 += even
#print(total_even2)

#total = 0
#for fizzbuzz in range(1, 101):
#    total +=1
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#    else:
#        print(total)    
# in this project we didn't need to calculate the total because the range function calculate it by itself but to undrestand it better i usesd it.

#def my_function():
#    print("hello")
#    print("world")
#my_function()                  

#import random
#word_list = ["ardvark", "baboon", "camel"]
#chosen_word =random.choice(word_list)
#guess = input("guess a letter. ").lower()
#for letter in chosen_word:
#    if letter == guess:
#      print("correct")
#    else:
#        print("wrong")


# import random
# word_list = ["sheep", "queen", "dog", "dimond", "blue", "face", "shark", "bag", "lock", "luck", "easy", "pizza"]
# chosen_word =random.choice(word_list)
# print(f"pssst, the solution is {chosen_word}.")            
# display = []
# for x in chosen_word:
#     display += "_"
# print(display)

# the_end = False 
# while not the_end:
#     guess = input("guess a letter: ").lower()
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if "_" not in display:
#         the_end == True
#         print("you win!")

# def greet():
#     print("welcome")
#     print("rase youre hand ")
#     print("jump")
# greet()

#parameter is the name of something , like a storage 
#arguement is the value in the parameter , it's the thing inside parameter
# def greet_with(name, location): this is called parameter 
#     print(f"hello {name}")  
#     print(f"your location is {location}")
# greet_with("ilia","esfahan")  , this is called positional arguement
# greet_with(name = "ilia", location = "esfahan") , this is called keyword arguement

# import math
# def cans(height, width, cover):
#     area = height * width
#     number_of_cans =math.ceil(area / cover)
#     print(f"you will need {number_of_cans} cans.")
# test_h =int(input("enter the height of wall\n"))
# test_w = int(input("enter the width of wall\n"))
# coverage = 5
# cans(height =test_h, width = test_w, cover = coverage)

# def prime_checker(number):
#     is_prime = True
#     for x in range(2, number):
#         if number % x ==0:
#             is_prime = False
#     if is_prime:
#         print("this is a prime number.")
#     else:
#         print("this is not a prime number.")
# n = int(input("check this number: "))
# prime_checker(number=n)

# students_scores = {
#     "Harry" : 81 ,
#     "Ron" : 78 ,
#     "Hermione" : 99 , 
#     "Draco" : 74 ,
#     "Neville" : 62, 
# }
# student_grades = {}
# for name in students_scores:
#     score = students_scores[name]
#     if score > 90:
#         student_grades[name] = "outstanding"
#     elif score > 80:
#         student_grades[name] = "exceeds expectations"
#     elif score > 70:
#         student_grades[name] = "Acceptable"
#     elif score <= 70:
#         student_grades[name]="Fail"  
# print(student_grades)




# travel_log = [
# {
#         "country" : "france",
#         "visits" : 12,
#         "cities" : ["paris", "lille" ,"dijon"]
# },
# {
#         "country" : "germany",
#         "visits" : 5,
#         "cities" : ["berlin", "humburg", "stuttgart"]
# },
# ]

# def add_new_country(country, times, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = times
#     new_country["cities"] = cities
#     travel_log.append(new_country)

# add_new_country("russa", 2, ["moscow", "saint petersburg"])
# print(travel_log)

# def format_name(f_name , l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# print(format_name("looloo" ,  "LOOLOOYI")) 
# note::::there is no difrence between just putting an argument or put the parameter equal to argumet the result is the same 
# for example in line '381'  i used positional argument but i also could use _____ argument :
# format_name(f_name = looloo , l_name = LOOLOO) 

# def is_leap(year):                                    from this 
#     if year % 4 : 
#         if year % 100:
#             if year % 400:
#                 return True
#             else:
#                 return False 
#         else:
#             return True
#     else:
#         return False
    
# def days_in_month(year , month):
#     month_days = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]       
# year = int(input("inter a year"))
# month = int(input("inter a month"))
# days = days_in_month(year , month)
# print(days)                                            to this     do this later

# def x():
#     """x is four plus thirty four"""
#     4+34
# x()                               you can ducuament your functions like this




