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
print(first_name)
print(middle_name)
print(last_name)
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
request_long = input()
print(f"Yes, {request_long}")
print(f'WHADDAYA MEAN "{request.upper()}"?!? YOU\'RE FIRED!!')

# option 2, simplified and more predictable (limits the user's answer options  
# and the result will be more predictable)
print("Hello Boss! I need to talk to you.")
print("Hmpf... what do you want, you midget?") # I'm quite small 
request = input("I want ")
print(request)
print(f"You want {request}??????")
request_long = input()
print(f"Yes, {request_long}")
print(f'WHADDAYA MEAN "I WANT {request.upper()}"?!? YOU\'RE FIRED!!')



# Table of contents. Here’s something for you to do in order to play around more
# with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started        #page1    
# Chapter 2: Numbers 				#page 9 
# Chapter 3: Letters 				#page 13





























