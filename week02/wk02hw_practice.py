# /1/ calculate a table for each letter in the alphabet from a-z and count how many 
# times each letter appears in Alice in Wonderland
# a: 34,650 for example (fancy word for counting stuff is "frequency distribution")
# b: 5,027
# z: 895 

# filename = 'alice_in_wonderland.txt'

# file = open(filename, 'r')
# text = file.read()

# def count_char(text):	
# 	text = text.lower()
# 	char_list = []
# 	for i in range(len(text)):
# 		if text[i].isalpha():
# 			counter = text.count(text[i])
# 			if [text[i], counter] not in char_list:
# 				char_list.append([text[i], counter])
# 	char_set = sorted(char_list)
# 	return char_set

# print(count_char(text))


# 1.  convert to all lowercase
# 2.  you can use text.count('a') - count number of a's in the whole text
# 3. count only if its alpha
# 4. now append ['a', count] into another list.
# 5. append only if this pair doesnt exist.(edited)

# def count_letters_list(text):
#     # generate a list of the alphabet in Python
#     text = text.lower()
#     char_list= []
#     for i in range(len(text)):
#         value = text.count(text[i])
#         if [text[i],value] not in char_list:
#             char_list.append([text[i],value])
    
#     char_set = sorted(char_list)
#     return (char_set)

# for line in file:
# 	print(line)

# print('from zero to sixty-fixe' + raw[:165])

# print('the length of Alice in Wonderland is: ' + str(len(raw)))
 
# for line in raw:
# 	for char.lower() in line:
# 		if char == 'a':
# 			char_count +=1
# print(char_count)
	
# ---------------------------------> DAY3 <----------------------------------
# /9/ Modify "a" for another name in my_dict. Hint: you will have to create a 
# new key-value pair, copy in the value, and then delete the old one.

# my_dict = {
# 	"a": 35000,
# 	"b": 8000,
# 	"z": 450
# }
# print(my_dict)

# #option 1:
# del my_dict['a']
# print(my_dict)

# my_dict['a'] = 55555
# print(my_dict)

# #option 2
# print('<>' * 10)
# my_dict = {
# 	"a": 35000,
# 	"b": 8000,
# 	"z": 450
# }
# print(my_dict)

# my_dict['a'] = 55555
# print(my_dict)



# /10/ Redo the frequency distribution of alice_in_wonderland.txt and 
# save your result in a dictionary.

# filename = 'alice_in_wonderland.txt'

# file = open(filename, 'r')
# text = file.read()

# def count_char(text):	
# 	text = text.lower()
# 	char_list = []
# 	for i in range(len(text)):
# 		if text[i].isalpha():
# 			counter = text.count(text[i])
# 			if [text[i], counter] not in char_list:
# 				char_list.append([text[i], counter])
# 	char_set = sorted(char_list)
# 	return dict(char_set)

# print(count_char(text))


# /11/ Create a dictionary with your own personal details, feel free to be 
# creative and funny so for example, you could include key-value pairs with 
# quirky fact, fav quote, pet. Practice adding, modifying, accesing.

# andreea_dict = {
# 	'age': 37,
# 	'job': 'Scrum Master',
# 	'passion': 'coding',
# 	'favourite music': 'nursery rhymes',
# 	'favourite food ': 'Dim Sum',
# 	'dream': 'become a University professor',
# 	'sleep time': '10 pm because baby'
# }

# # access
# print(andreea_dict['dream'])
# # print(andreea_dict['coding'])  # error, as you can only print by key, not value

# # add
# andreea_dict['laptop'] = "MacBook Air"
# andreea_dict['phone'] = 'all things Apple!!!'
# andreea_dict['country'] = 'the way too hot Malaysia'
# andreea_dict['sports'] = 'yoga'
# # print(andreea_dict)

# # modify 
# andreea_dict['dream'] = 'build awesome products with Python'
# # print(andreea_dict)
# andreea_dict['passion'] = 'reading allll the boooks'
# # print(andreea_dict)
# del andreea_dict['country']
# print('~~~~~~'*10)
# print(andreea_dict)
# del andreea_dict['favourite music']
# print('~~~~~~'*10)
# print(andreea_dict)

# # clears a dictionary but doesn't erase it
# andreea_dict.clear()
# print(andreea_dict)


# /12/ Review the chat reply of today's beautiful class interaction and instantiate 
# a student variable for everyone who shared their dream.

# class Student():
# 	def __init__(self, name, discord_id, fav_food, dream):
# 		self.name = name
# 		self.discord_id = discord_id
# 		self.fav_food = fav_food
# 		self.dream = dream

# 	def my_print(self):
# 		print(self.name + ' ' + self.discord_id + ' ' + self.fav_food + ' ' + self.dream) 


# s1 = Student('Virginia Balseiro', 'yesvirginia', 'pasta', 'moving to Europe')
# s2 = Student('Andreea Visanoiu', 'Andreea[Gold]', 'wontonmee', 'university professor')
# s3 = Student('Cristina Tarantino', 'CristyTarantino[Gold]', 'pasta', 'being an amazing developer')
# s4 = Student("Jessi_RS", "Jessi_RS[Gold]#7015", "pasta", "work as developer by end of the year")
# s5 = Student("alteredco", "alteredco[GOLD]", "sushi", "dream big")
# s6 = Student("Deb Cupitt", "Deb[GOLD]", "chocolate", "gender equity")
# s7 = Student("Marwa Qabeel", "Marwa Qabeel[GOLD]", "", "Data Analyst")
# s8 = Student("Sacha Young", "sacha[Gold]", "French fries", "return to research")
# s9 = Student("Bituin Callanta", "bituin [gold]", "sashimi", "lessen the gender wage gap")

# s1.my_print()
# s2.my_print()
# s3.my_print()
# s4.my_print()
# s5.my_print()
# s6.my_print()
# s7.my_print()
# s8.my_print()
# s9.my_print()

# /13/ Translate the real world 1MWTT student into a Student class, decide on all 
# the attributes that would be meaningful.

# class Student():
# 	def __init__(self, firstname, lastname, email, country, countrycode, phone, github, programming_level, course_objective):
# 		self.firstname = firstname
# 		self.lastname = lastname
# 		self.email = email
# 		self.country = country
# 		self.countrycode = countrycode
# 		self.phone = phone
# 		self.github = github
# 		self.programming_level = programming_level
# 		self.course_objective = course_objective



# --------------------------------DAY1--------------------------------------------

#/1/ If you have already started Python the Hard Way, please choose 5 exercises 
# and write tests for those in unittest and make them pass. Take your ex.py 
# and your test_ex.py and zip them into a single file to upload for submission 
# via the Helpdesk. (also above)



# --------------------------------DAY2--------------------------------------------


# /2/ There is something small that needs fixing. Can you spot it and fix it? 
# (Hint, we only want A-Z and a-z)
# for i in range(65, 125):
# 	if chr(i).isalpha():
# 		print(chr(i))


# # /3/ Make a function that prints A-Z and a-z
# for i in range(65, 125):
# 	if chr(i).isalpha():
# 		print(chr(i))


# /4/ Make a function that asks the user for a message, and turns it into a list of 
# numbers. (It's a cypher ;))

# print("Hello, please write your message here >>")
# message = input()
# code = ''
# # print(message)

# for i in message:
# 	number = ord(i)
# 	# print(number)
# 	code += str(number)
# print(code)


## /5/ Write a function that prints out all elements of the above board, 
# starting from the first element of the first line, till the end. 
# Each line should be read from beginning to end

# "M" is visually more dense than  "o"
M = 'land'
o = 'water'
world = [[o,o,o,o,o,o,o,o,o,o,o],
		[o,o,o,o,M,M,o,o,o,o,o],
		[o,o,o,o,o,o,o,o,M,M,o],
		[o,o,o,M,o,o,o,o,o,M,o],
		[o,o,o,M,o,M,M,o,o,o,o],
		[o,o,o,o,M,M,M,M,o,o,o],
		[o,o,o,M,M,M,M,M,M,M,o],
		[o,o,o,M,M,o,M,M,M,o,o],
		[o,o,o,o,o,o,M,M,o,o,o],
		[o,M,o,o,o,M,o,o,o,o,o],
		[o,o,o,o,o,o,o,o,o,o,o]]


# for index in range(len(world), 0, -1):
# 	print(world[index])
	

# print(world[0][0])
# print(world[0][-10])
# print(world[0])
# print(world)

# def reversed_world(world):
# 	world.reverse()
# 	# print(world)
# 	for sublist in world:
# 		sublist.reverse()
# 		for element in sublist: 
# 			print(element)

# reversed_world(world)

# /6/ Now write a function that prints out all elements in reverse.



# /7/ There is one small bug in the continent counter above. 
# Can you find it and fix it? (Hint: change the world so that the continent 
# borders the edge)

M = 'land'
o = 'water'
world = [[o,o,o,o,o,o,o,o,o,o,o],
		[o,o,o,o,M,M,o,o,o,o,o],
		[o,o,o,o,o,o,o,o,M,M,o],
		[o,o,o,M,o,o,o,o,o,M,o],
		[o,o,o,M,o,M,M,o,o,o,o],
		[o,o,o,o,M,M,M,M,o,o,o],
		[o,o,o,M,M,M,M,M,M,M,o],
		[o,o,o,M,M,o,M,M,M,o,o],
		[o,o,o,o,o,o,M,M,o,o,o],
		[o,M,o,o,o,M,o,o,o,o,o],
		[o,o,o,o,M,o,o,o,o,o,o]]

def continent_counter(world, x, y):
	if world[y][x] != 'land':
		return 0

	size = 1 
	world[y][x] = 'counted land'
	size = size + continent_counter(world, x-1, y-1)
	# print(size)
	size = size + continent_counter(world, x, y-1)
	# print(size)
	size = size + continent_counter(world, x+1, y-1)
	# print(size)
	size = size + continent_counter(world, x-1, y)
	# print(size)
	size = size + continent_counter(world, x+1, y)
	# print(size)
	size = size + continent_counter(world, x-1, y+1)
	# print(size)
	size = size + continent_counter(world, x, y+1)
	# print(size)
	size = size + continent_counter(world, x+1, y+1)
	# print(size)
	return size 

print(continent_counter(world, 5, 5))


# /8/ Write a function that generates an n x n sized board with either land or 
# water chosen randomly.



## OPTIONAL ## 

# /3/ Optional: Write a function that does a ceaser cypher (Google), ask the 
# user a number, and shift their message by that number.

# message = "This is my message to be coded."
# key = 1
# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# coded = ''

# for symbol in message:
# 	if symbol in SYMBOLS:
# 		symbol_index = SYMBOLS.find(symbol)
# 		print(symbol_index)

# 		coded_index = symbol_index + key

# 		if coded_index >= len(SYMBOLS):
# 			coded_index = coded_index - len(SYMBOLS)
# 		elif coded_index < 0:
# 			coded_index = coded_index + len(SYMBOLS)

# 		coded += SYMBOLS[coded_index]
# 	else:
# 		coded = coded + symbol	
	
# print(coded)


# message = "Uijt!jt!nz!nfttbhf!up!cf!dpefeA"
# key = 1
# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# coded = ''

# for symbol in message:
# 	if symbol in SYMBOLS:
# 		symbol_index = SYMBOLS.find(symbol)
# 		print(symbol_index)

# 		coded_index = symbol_index - key

# 		if coded_index >= len(SYMBOLS):
# 			coded_index = coded_index - len(SYMBOLS)
# 		elif coded_index < 0:
# 			coded_index = coded_index + len(SYMBOLS)

# 		coded += SYMBOLS[coded_index]
# 	else:
# 		coded = coded + symbol	
	
# print(coded)




# /4/ Run your continent counter for a 20 x 20 board. How long does it take to run? 
# (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up 
# in a VERY LOOOONG WAIT) - make sure you know how to break a running program 
# as it may take a long time to complete and you might not have time to wait for it ;)


# /5/ Write test coverage in unittest and/or trace for Continent Counter.




# --------------------------------DAY3--------------------------------------------


# /9/ Write a test to check the outcome of the alice_in_wonderfland task: one test for 
# list of lists, and one test for dictionary output.



# /10/ Come up with a whole taxonomy of Classes for 1MWTT
# Person()
# Student()
# Mentor()
# Volunteer()
# Employer() 
# Feel free to suggest/invent and also use mixing, decorators, and any other design patterns that you see would help reach 
# the mission of 1 million women to tech by 2020.


# --------------------------------DAY4--------------------------------------------



# /16/ Exercise #5 from http://www.nltk.org/book/ch01.html ☼ Compare the lexical diversity scores 
# for humor and romance fiction in 1.1. Which genre is more lexically diverse?

