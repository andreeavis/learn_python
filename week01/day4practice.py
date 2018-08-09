# for i in range(99):
# 	print("99 Bottles of Beer on the Wall")

# no_bottles = 99
# i = 99
# while i <= 99 and i >= 0:
# 	if i !=0:
# 		print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
# 		print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
# 		i = i - 1
# 	elif i == 1: 
# 		print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
# 		print("Take one down and pass it around, nore more bottles of beer on the wall.")
# 		i = i - 1
# 	elif i == 0: 
# 		print("No more bottles of beer on the wall, no more bottles of beer.")
# 		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
# 		i = i - 1




# https://pine.fm/LearnToProgram/chap_06.html

# n = 0
# def moo(n):
# 	print(n * 'moo')

# moo(3)

# def shout_grandma():
# 	reply = input("Say something to Granny: >> ")
# 	if not reply.isupper():
# 		print("HUH?! SPEAK UP, GIRL")
# 		shout_grandma()
# 	elif reply.isupper():
# 		from random import randint
# 		gran_year = randint(1930, 1950)
# 		print(f"NO, NOT SINCE {gran_year}!")

	
# shout_grandma()


# from random import randint

# def shout_grandma(question):
#     reply = input("Say something to Granny> ")
#     if reply.isupper():
#         gran_year = randint(1930, 1950)
#         print(f"NO, NOT SINCE {gran_year}!")
#     else: 
#         print("HUH?! SPEAK UP, GIRL")
#         shout_grandma(question)

# shout_grandma('')



# print("Hello! Type as many words as you like. When you get bored, press 'Enter' on an empty line: >> ")
# answer = 'word1'
# lst1 =[]

# while len(answer) > 0:
# 	answer = input()
# 	if answer != "":
# 		lst1.append(answer)
# print(sorted(lst1)) 


# print("Hello! Type as many words as you like. When you get bored, press 'Enter' on an empty line: >> ")
# answer = 'a'
# lst1 =[]
# while answer != '':
#     answer = input()
#     if len(answer) > 0:
#         lst1.append(answer)
# print(sorted(lst1))

	

# contents = "Table of Contents"
# chapter1 = ["Chapter 1: Getting Started", "page 1"] 
# chapter2 = ["Chapter 2: Numbers", "page 9"] 
# chapter3 = ["Chapter 3: Letters", "page 13"]
# print(contents.center(50))
# print(chapter1[0].ljust(0), chapter1[1].rjust(20))
# print(chapter2[0].ljust(20), chapter2[1].rjust(26))
# print(chapter2[0].ljust(20), chapter2[1].rjust(26))


# Table of contents. Write a table of contents program here. Start the program with a list holding 
# all of the information for your table of contents (chapter names, page numbers, and so on). 
# Then print out the information from the list in a beautifully formatted table of contents. 
# Use string formatting such as left align, right align, center.


# content_lst = ["Table of Contents", 
# 		["Chapter 1: Getting Started", "page", "1"], 
# 		["Chapter 2: Numbers", "page", "9"], 
# 		["Chapter 3: Letters", "page", "13"]]
# print(content_lst[0])
# print(content_lst[1][0].ljust(0), content_lst[1][1].rjust(20))
# print(content_lst[2][0].ljust(0), content_lst[2][1].rjust(28))
# print(content_lst[3][0].ljust(0), content_lst[3][1].rjust(29))


# content_lst = ["Table of Contents", 
# 		["Chapter 1: Getting Started", "page", "1"], 
# 		["Chapter 2: Numbers", "page", "9"], 
# 		["Chapter 3: Letters", "page", "13"]]
# print(content_lst[0])
# print(content_lst[1][0].ljust(0), content_lst[1][1].rjust(20), content_lst[1][2].rjust(2))
# print(content_lst[2][0].ljust(0), content_lst[2][1].rjust(28), content_lst[2][2].rjust(2))
# print(content_lst[3][0].ljust(0), content_lst[3][1].rjust(28), content_lst[3][2].rjust(0))



#try with count "BYE"; count_bye = 

# from random import randint

# reply = input("Say something to Granny: >> ")
# reply1 = ''
# reply2 = ''
# reply3 = ''

# def shout_grandma():
#     while reply1 != 'BYE!' and reply2 != 'BYE!' and reply3 != 'BYE!':
#         while reply1 != 'BYE':
#             if reply1.isupper():
#                 gran_year = randing(1930, 1950)
#                 print(f"NO, NOT SINCE {gran_year}!")
#                 shout_grandma()
#             else:
#                 print("HUH?! SPEAK UP, GIRL")
#                 shout_grandma()
#         while reply2 != 'BYE!':
#             if reply2.isupper():
#                 gran_year = randing(1920, 1950)
#                 print(f"NO, NOT SINCE {gran_year}!")
#                 shout_grandma()
#             else:
#                 print("HUH?! SPEAK UP, GIRL")
#                 shout_grandma()
#         while reply3 != 'BYE!':
#             if reply3.isupper():
#                 gran_year = randint(1920, 1950)
#                 print(f"NO, NOT SINCE {gran_year}!")
#                 shout_grandma()
#             else: 
#                 print("HUH?! SPEAK UP, GIRL")
#                 shout_grandma()
    
#     return


# shout_grandma()

# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, 
# she could pretend not to hear you. Change your previous program so that you have to shout BYE 
# three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, 
# you should still be talking to Grandma.    

# from random import randint

# def shout_grandma(question):
#     count_bye = 0
#     while count_bye < 3:
#         reply = input("Say something to Granny: >> ")
#         if reply.isupper() and reply != "BYE!":
#             gran_year = randint(1930, 1950)
#             count_bye = 0
#             print(f"NO, NOT SINCE {gran_year}!")
#         elif reply == "BYE!":
#             count_bye += 1
#             if count_bye == 3:
#                 return
#         else: 
#             count_bye = 0
#             print("HUH?! SPEAK UP, GIRL")

# shout_grandma('')


# Leap years. Write a program that asks for a starting year and an ending year and then 
# prints all the leap years between them (and including them, if they are also leap years). 
# Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not 
# leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, 
# which were in fact leap years). What a mess!


# start_year = int(input("Write down a start year! >> "))
# end_year = int(input("Tell me an end year! >> "))

# while start_year <= end_year:  
#     if start_year % 400 == 0:
#         print(start_year)
#     elif start_year % 4 == 0 and start_year % 100 != 0:
#         print(start_year)


#     start_year += 1
       

# Old school Roman numerals
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string 
# containing the proper old-school 
# Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
# Make sure to test your method on a bunch of different numbers.
# For reference, these are the values of the letters used: 

# def old_roman(num):
#     m, d, c, l, x, v, i = 0, 0, 0, 0, 0, 0, 0
#     if num >= 1000:
#         m = num // 1000
#         num = num % 1000
#     if num >= 500:
#         d = num // 500
#         num = num % 500
#     if num >= 100:
#         c = num // 100
#         num = num % 100
#     if num >= 50:
#         l = num // 50
#         num = num % 50
#     if num >= 10:
#         x = num // 10
#         num = num % 10
#     if num >= 5:
#         v = num // 5
#         num = num % 5
#     if num < 5:
#         i = num // 1
#         num = num % 10
#     print('M' * m + 'D' * d + 'C' * c + 'L' * l + 'X' * x + 'V' * v + 'I' * i)

# old_roman(1555)
        

# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number 
# before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. 
# Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, 
# it should return 'IV', 90 should be 'XC' etc.

# def modern_roman(num):
#     m, cm, d, cd, c, xc, l, xl, x, ix, v, iv, i = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#     if num >= 1000:
#         m = num // 1000
#         num = num % 1000
#     if num >= 900:
#         cm = num // 900
#         num = num % 900
#     if num >= 500:
#         d = num // 500
#         num = num % 500
#     if num >= 400:
#         cd = num // 400
#         num = num % 400
#     if num >= 100:
#         c = num // 100
#         num = num % 100
#     if num >= 90:
#         xc = num // 90
#         num = num % 90
#     if num >= 50:
#         l = num // 50
#         num = num % 50
#     if num >= 40:
#         xl = num // 40
#         num = num % 40
#     if num >= 10:
#         x = num // 10
#         num = num % 10
#     if num >= 9:
#         ix = num // 9
#         num = num % 9
#     if num >= 5:
#         v = num // 5
#         num = num % 5
#     if num >= 4:
#         iv = num // 4
#         num = num % 4
#     if num < 5:
#         i = num // 1
#         num = num % 10
#     print('M' * m + 'CM' * cm + 'D' * d + 'CD' * cd + 'C' * c + 'XC' * xc + 'L' * l 
#         + 'XL' * xl +'X' * x + 'IX' * ix + 'V' * v + 'IV' * iv + 'I' * i)
    

# modern_roman(1944)
# modern_roman(400)
# modern_roman(444)
# modern_roman(900)
# modern_roman(999)
# modern_roman(99)
# modern_roman(9)
# modern_roman(44)
# modern_roman(4)
# modern_roman(3999)
# modern_roman(2000)
# modern_roman(222)















