### DAY 1 ###

# write a program that telss you hours in a year
print(365 * 24)

# write a program that tells you minutes in a decade
print(10 * 365 * 24 * 60)

# write a program that tells you your age in seconds
print(365 * 37 * 24 * 60 * 60 + (30+31+30+17) * 24 * 60 * 60)

# write a program that tells you how many days it takes 
# for a 32-bit system to timeout if it has a but w/ integer overflow

# calculate n-bit integer
# n-bit integer = −(2^^n−1) to (2^^n−1 − 1)

max32_neg = -(2 ** (32-1) - 1)
max32_poz = (2 ** (32-1) - 1)

print(max(max32_poz, max32_neg))

time_run_out_32 = max32_poz / 100 / 60 / 60 / 24
print(time_run_out_32)
print(int(time_run_out_32))

# how about a 62-bit system
max64_neg = -(2 ** (64-1) - 1)
max64_poz = (2 ** (64-1) - 1)

print(max(max64_poz, max64_neg))

time_run_out_64 = max64_poz / 100 / 60 / 60 / 24
print(time_run_out_64)
print(int(time_run_out_64))

#calculate your age based on your b-day; time of day: 10:00 am
#birthday: 31.03.1981
import time
import datetime

#year, month, day, hour, minute, second
birthday = datetime.datetime(1981, 3, 31)
from datetime import datetime

age = datetime.today() - birthday 
print(age)

#year, month, day, hour, minute, second
my_bday = datetime.date(1981, 3, 31, 10, 15, 0)
bday_days = (datetime.date.now()  - my_bday)

bday_years = bday_days.days / 365

print("I am " + bday_years + " years old!") 


### DAY 3 ###

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
# Finally, it should greet the person using their full name.

first_name = input("What's your first name? ")
middle_name = input("What's your middle name? ")
last_name = input("What's your last name? ")
# # print(first_name)
# # print(middle_name)
# # print(last_name)
if (middle_name) != input():
	print("Have a good day, my dear " + first_name + " " + middle_name + " " + last_name + "!")
else:
	print("Have a good day, my dear " + first_name + " " + last_name + "!")


#Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
# Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
# (Do be tactful about it, though.)

fav_number = input("What is your favourite number? ")
x = int(fav_number)

print("That's a good number, but " + str(x+1) + " is a much better one!")

name = (input("What's your full name? "))
print("Did you know there are " + str(len(name)) + " characters in your name, " + name + "?")


# Angry boss. Write an angry boss program that rudely asks what you want. 
# Whatever you answer, the angry boss should yell it back to you and then fire you.
# "WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!"

# option 1: 
print("Hello Boss! I need to talk to you.")
print("Hmpf... what do you want, you midget?") # I'm quite small 
request = input()
print(f"{request}??????")
# request_long = input()
# print(f"Yes, {request_long}")
print(f'WHADDAYA MEAN "{request.upper()}"?!? YOU\'RE FIRED!!')

# option 2, simplified and more predictable (limits the user's answer options  
# and the result will be more predictable)
print("Hello Boss! I need to talk to you.")
print("Hmpf... what do you want, you midget?") # I'm quite small 
request = input("I want ")
# print(request)
print(f"You want {request}??????")
# request_long = input()
# print(f"Yes, {request_long}")
print(f'WHADDAYA MEAN "I WANT {request.upper()}"?!? YOU\'RE FIRED!!')



# Table of contents. Here’s something for you to do in order to play around more
# with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
			# Table of Contents
# Chapter 1: Getting Started        #page1    
# Chapter 2: Numbers 				#page 9 
# Chapter 3: Letters 				#page 13

contents = "Table of Contents"
chapter1 = ["Chapter 1: Getting Started", "page 1"] 
chapter2 = ["Chapter 2: Numbers", "page 9"] 
chapter3 = ["Chapter 3: Letters", "page 13"]
print(contents.center(50))
print(chapter1[0].ljust(0), chapter1[1].rjust(20))
print(chapter2[0].ljust(20), chapter2[1].rjust(26))
print(chapter2[0].ljust(20), chapter2[1].rjust(26))


# Research how to generate a random number in Python
#generate 11 random numbers, from 1-121; with module random
import random
for x in range(11):
	print(random.randint(1, 11*11))

print("Next experiment")

#generate 11 random numbers, that are multiple of 5
for x in range(10):
	print(random.randint(1, 21)*5)
print

#generate a random number with module random and function randint
print("Next experiment with randint")
from random import randint
print(randint(0, 121))

print("One more way of doing it with randint considering the range also + returning a list")
x = [randint(0, 121) for num in range(0, 10)]
print(x)

#generate a random number with "secrets" module; better for cryptography
from secrets import randbelow
print(randbelow(10))

#generate random num with random.shuffle
import random
nums = [x for x in range(10)]
random.shuffle(nums)
print(nums)

#random.sample(population, k) -> picks a k # of unique random elements, a samle, from a sequence
import random
c = list(range(0,25))
print(c)
print(random.sample(c, 3))

c = {1, 4, 6, 23, 11, 121}
print(random.sample(c, 2))


#random different function - simpler way to do it
print(random.random())   # prints a random number between 0-1


# “99 Bottles of Beer on the Wall.” 
# Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
i = 99
while i <= 99 and i >= 0:
	if i !=0:
		print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
		print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
		i = i - 1
	elif i == 1: 
		print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
		print("Take one down and pass it around, nore more bottles of beer on the wall.")
		i = i - 1
	elif i == 0: 
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
		i = i - 1


# Deaf grandma. Whatever you say to Grandma (whatever you type in), 
# she should respond with this: HUH?! SPEAK UP, GIRL!
# unless you shout it (type in all capitals). If you shout, she can hear you, and yells back:
# NO, NOT SINCE 1938!
# To make your program really believable, have Grandma shout a different year each time, 
# maybe any year at random between 1930 and 1950. 

from random import randint

def shout_grandma(question):
    reply = input("Say something to Granny: >> ")
    if reply.isupper() and reply != "BYE!":
        gran_year = randint(1930, 1950)
        print(f"NO, NOT SINCE {gran_year}!")
        shout_grandma(question)
    elif reply == "BYE!":
    	return
    else: 
        print("HUH?! SPEAK UP, GIRL")
        shout_grandma(question)

shout_grandma('')

# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, 
# she could pretend not to hear you. Change your previous program so that you have to shout BYE 
# three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, 
# you should still be talking to Grandma.

from random import randint

def shout_grandma(question):
    count_bye = 0
    while count_bye < 3:
        reply = input("Say something to Granny: >> ")
        if reply.isupper() and reply != "BYE!":
            gran_year = randint(1930, 1950)
            count_bye = 0
            print(f"NO, NOT SINCE {gran_year}!")
        elif reply == "BYE!":
            count_bye += 1
            if count_bye == 3:
                return
        else: 
            count_bye = 0
            print("HUH?! SPEAK UP, GIRL")

shout_grandma('')


# Leap years. Write a program that asks for a starting year and an ending year and then 
# puts all the leap years between them (and including them, if they are also leap years). 
# Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not 
# leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, 
# which were in fact leap years). What a mess!

start_year = int(input("Write down a start year! >> "))
end_year = int(input("Tell me an end year! >> "))

while start_year <= end_year:  
    if start_year % 400 == 0:
        print(start_year)
    elif start_year % 4 == 0 and start_year % 100 != 0:
        print(start_year)
    start_year += 1
       

# Find something today in your life, that is a calculation. Go for a walk, look around the park, 
# try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, 
# leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

# counting leafes in park
park = 100 * 100
leaves_per_10m =  1200

total_leaves_park = 1200 * 100 * 1000
print(total_leaves_park)



# Building and sorting an array. Write the program that asks us to type as many words as we want 
# (one word per line, continuing until we just press Enter on an empty line) and then repeats the words 
# back to us in alphabetical order. 

print("Hello! Type as many words as you like. When you get bored, press 'Enter' on an empty line: >> ")
answer = 'word1'
lst1 =[]

while len(answer) > 0:
	answer = input()
	if answer != "":
		lst1.append(answer)
print(sorted(lst1)) 


# Table of contents. Write a table of contents program here. Start the program with a list holding 
# all of the information for your table of contents (chapter names, page numbers, and so on). 
# Then print out the information from the list in a beautifully formatted table of contents. 
# Use string formatting such as left align, right align, center.

content_lst = ["Table of Contents", 
		["Chapter 1: Getting Started", "page", "1"], 
		["Chapter 2: Numbers", "page", "9"], 
		["Chapter 3: Letters", "page", "13"]]
print(content_lst[0])
print(content_lst[1][0].ljust(0), content_lst[1][1].rjust(20))
print(content_lst[2][0].ljust(0), content_lst[2][1].rjust(28))
print(content_lst[3][0].ljust(0), content_lst[3][1].rjust(29))


content_lst = ["Table of Contents", 
		["Chapter 1: Getting Started", "page", "1"], 
		["Chapter 2: Numbers", "page", "9"], 
		["Chapter 3: Letters", "page", "13"]]
print(content_lst[0])
print(content_lst[1][0].ljust(0), content_lst[1][1].rjust(20), content_lst[1][2].rjust(2))
print(content_lst[2][0].ljust(0), content_lst[2][1].rjust(28), content_lst[2][2].rjust(2))
print(content_lst[3][0].ljust(0), content_lst[3][1].rjust(28), content_lst[3][2].rjust(0))


# Write a function that prints out "moo" n times.

def moo(n):
	print(n * 'moo')


# Old school Roman numerals
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school 
# Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
# Make sure to test your method on a bunch of different numbers.

def old_roman(num):
    m, d, c, l, x, v, i = 0, 0, 0, 0, 0, 0, 0
    if num >= 1000:
        m = num // 1000
        num = num % 1000
    if num >= 500:
        d = num // 500
        num = num % 500
    if num >= 100:
        c = num // 100
        num = num % 100
    if num >= 50:
        l = num // 50
        num = num % 50
    if num >= 10:
        x = num // 10
        num = num % 10
    if num >= 5:
        v = num // 5
        num = num % 5
    if num < 5:
        i = num // 1
        num = num % 10
    print('M' * m + 'D' * d + 'C' * c + 'L' * l + 'X' * x + 'V' * v + 'I' * i)

old_roman(1555)

# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number 
# before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. 
# Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, 
# it should return 'IV', 90 should be 'XC' etc.

def modern_roman(num):
    m, cm, d, cd, c, xc, l, xl, x, ix, v, iv, i = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if num >= 1000:
        m = num // 1000
        num = num % 1000
    if num >= 900:
        cm = num // 900
        num = num % 900
    if num >= 500:
        d = num // 500
        num = num % 500
    if num >= 400:
        cd = num // 400
        num = num % 400
    if num >= 100:
        c = num // 100
        num = num % 100
    if num >= 90:
        xc = num // 90
        num = num % 90
    if num >= 50:
        l = num // 50
        num = num % 50
    if num >= 40:
        xl = num // 40
        num = num % 40
    if num >= 10:
        x = num // 10
        num = num % 10
    if num >= 9:
        ix = num // 9
        num = num % 9
    if num >= 5:
        v = num // 5
        num = num % 5
    if num >= 4:
        iv = num // 4
        num = num % 4
    if num < 5:
        i = num // 1
        num = num % 10
    print('M' * m + 'CM' * cm + 'D' * d + 'CD' * cd + 'C' * c + 'XC' * xc + 'L' * l 
        + 'XL' * xl +'X' * x + 'IX' * ix + 'V' * v + 'IV' * iv + 'I' * i)























