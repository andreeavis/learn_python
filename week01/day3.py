name = 'Andreea Visanoiu'
result = ''

# for i in range(0, len(name)):
# 	print(name[i])


# for i in range(0, len(name)):
# 	if i % 2 == 0:
# 		print(name[i])
# 		result = result + name[i]
# 		print('Result changed to ' + result)


# print("The final result for all even indexed letters in name is: " + result + '! Drumroll please!! Thank you. I would like to thank the Academy!')


# change elements in the formula above: the %, 0, the loop, etc and experiment with it

# 'x' land, 'o' water; 11x11 continent; this is 1x1 => world = 'x' and world = 'o' is the solution
world = 'ooxxxxxooxxoxoxox'
# count 1

world = 'o'


###### HOMEWORK DAY 3 #########

# HW 1: print your name, middle name, last name 

# first_name = input("What's your first name? ")
# middle_name = input("What's your middle name? ")
# last_name = input("What's your last name? ")
# # # print(first_name)
# # # print(middle_name)
# # # print(last_name)
# if (middle_name) != input():
# 	print("Have a good day, my dear " + first_name + " " + middle_name + " " + last_name + "!")
# else:
# 	print("Have a good day, my dear " + first_name + " " + last_name + "!")


# HW 2: print favourite number input + add one to it when you return it to user 

# fav_number = input("What is your favourite number? ")
# x = int(fav_number)

# print("That's a good number, but " + str(x+1) + " is a much better one!")

# name = (input("What's your full name? "))
# print("Did you know there are " + str(len(name)) + " characters in your name, " + name + "?")

# var1 = 'stop'
# var2 = 'stressed'
# var3 = 'Can you pronounce this sentence backwards?'

# print(str(reversed(var1)))

# HW3: Angry boss print "WHADDAYA MEAN < Argument here ->>>"I WANT A RAISE"?!?> YOU'RE FIRED!!"

# version 1
# print("Hello Boss! I need to talk to you.")
# print("Hmpf... what do you want, you midget?") # I'm quite small 
# request = input()
# print(f"{request}??????")
# # request_long = input()
# # print(f"Yes, {request_long}")
# print(f'WHADDAYA MEAN "{request.upper()}"?!? YOU\'RE FIRED!!')

# version 2, simplified
# print("Hello Boss! I need to talk to you.")
# print("Hmpf... what do you want, you midget?") # I'm quite small 
# request = input("I want ")
# # print(request)
# print(f"You want {request}??????")
# # request_long = input()
# # print(f"Yes, {request_long}")
# print(f'WHADDAYA MEAN "I WANT {request.upper()}"?!? YOU\'RE FIRED!!')


# HW 4: 
# Table of Contents
# Chapter 1: Getting Started        #page 1    
# Chapter 2: Numbers 				#page 9 
# Chapter 3: Letters 				#page 13

# contents = "Table of Contents"
# chapter1 = ["Chapter 1: Getting Started", "page 1"] 
# chapter2 = ["Chapter 2: Numbers", "page 9"] 
# chapter3 = ["Chapter 3: Letters", "page 13"]
# print(contents.center(50))
# print(chapter1[0].ljust(0), chapter1[1].rjust(20))
# print(chapter2[0].ljust(20), chapter2[1].rjust(26))
# print(chapter2[0].ljust(20), chapter2[1].rjust(26))

# generate a random number in python

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








