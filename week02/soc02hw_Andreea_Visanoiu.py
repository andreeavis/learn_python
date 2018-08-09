# ---------------------------------> DAY1 <----------------------------------

# /1/ calculate a table for each letter in the alphabet from a-z and count how many 
# times each letter appears in Alice in Wonderland
# a: 34,650 for example (fancy word for counting stuff is "frequency distribution")
# b: 5,027
# z: 895 

filename = 'alice_in_wonderland.txt'

file = open(filename, 'r')
text = file.read()

def count_char(text):	
	text = text.lower()
	char_list = []
	for i in range(len(text)):
		if text[i].isalpha():
			counter = text.count(text[i])
			if [text[i], counter] not in char_list:
				char_list.append([text[i], counter])
	char_set = sorted(char_list)
	return char_set

print(count_char(text))


### OPTIONAL

#/1/ If you have already started Python the Hard Way, please choose 5 exercises 
# and write tests for those in unittest and make them pass. Take your ex.py 
# and your test_ex.py and zip them into a single file to upload for submission 
# via the Helpdesk. (also above)
 
 #I will tackle this exercise later on (going to Python The Hard Way now)


# /2/If you haven't started it and you have the .pdf then start the exercises. 
# e.g. 1 - 10 a day. Please note that exercises differ a lot: 
# some are very short, so you could complete more than one a day. 
# Some of them e.g. ex 37 are very long and have long lists of things to try 
# (almost like a reference) as well as many exercises within them. 
# These longer ones could take several days, if not weeks to complete fully.

# ----------------------DONE (17 Exercises)--------------------------

# ---------------------------------> DAY2 <----------------------------------

# /2/ There is something small that needs fixing. Can you spot it and fix it? 
# (Hint, we only want A-Z and a-z)
 
for i in range(65, 65+2*26):
	if chr(i).isalpha():
		print(i, " stands for", chr(i))

# /3/ Make a function that prints A-Z and a-z

for i in range(65, 123):
	if chr(i).isalpha():
		print(chr(i))


# /4/ Make a function that asks the user for a message, and turns it into a list of 
# numbers. (It's a cipher ;))

print("Hello, please write your message here >>")
message = input()
code = ''
# print(message)

for i in message:
	number = ord(i)
	# print(number)
	code += str(number)
print(code)


## /5/ Write a function that prints out all elements of the above board, 
# starting from the first element of the first line, till the end. 
# Each line should be read from beginning to end

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

# print(world[0][0])
# print(world[0][-10])
# print(world[0])
# print(world)

for sublist in world:
	for element in sublist:
		print(element)

# /6/ Now write a function that prints out all elements in reverse.

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


def reversed_world(world):
	world.reverse()
	# print(world)
	for sublist in world:
		sublist.reverse()
		for element in sublist: 
			print(element)

reversed_world(world)


# /7/ There is one small bug in the continent counter above. 
# Can you find it and fix it? (Hint: change the world so that the continent 
# borders the edge)

# n/a


# /8/ Write a function that generates an n x n sized board with either land or 
# water chosen randomly.

#n/a

## OPTIONAL ## 

# /3/ Optional: Write a function that does a ceaser cypher (Google), ask the 
# user a number, and shift their message by that number.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
print("Tell me your secret message, you wildling: ")
message = input()
print("Now tell me what key to code your message (must be a number): ")
key = int(input())
coded_message = ''
decoded_message = ''
# print(len(SYMBOLS))


for char in message:
	if char in SYMBOLS:
		char_index = SYMBOLS.find(char)
		coded_index = (char_index + key) % 66
		coded_message += SYMBOLS[coded_index]

	else:
		coded_message += char		

print(f"Your coded text is: {coded_message}")


for char in message:
	if char in SYMBOLS:
		char_index = SYMBOLS.find(char)
		decoded_index = (char_index - key) % 66
		decoded_message += SYMBOLS[decoded_index]
	else:
		decoded_message += char

print(f"Your decoded message is: {decoded_message}")

# /4/ Run your continent counter for a 20 x 20 board. How long does it take to run? 
# (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up 
# in a VERY LOOOONG WAIT) - make sure you know how to break a running program 
# as it may take a long time to complete and you might not have time to wait for it ;)

#n/a

# /5/ Write test coverage in unittest and/or trace for Continent Counter.

#n/a

# ---------------------------------> DAY3 <----------------------------------

# /9/ Modify "a" for another name in my_dict. Hint: you will have to create a 
# new key-value pair, copy in the value, and then delete the old one.

my_dict = {
	"a": 35000,
	"b": 8000,
	"z": 450
}
print(my_dict)

#option 1:
del my_dict['a']
print(my_dict)

my_dict['a'] = 55555
print(my_dict)

#option 2
print('<>' * 10)
my_dict = {
	"a": 35000,
	"b": 8000,
	"z": 450
}
print(my_dict)

my_dict['a'] = 55555
print(my_dict)

# /10/ Redo the frequency distribution of alice_in_wonderland.txt and 
# save your result in a dictionary.

filename = 'alice_in_wonderland.txt'

file = open(filename, 'r')
text = file.read()

def count_char(text):	
	text = text.lower()
	char_list = []
	for i in range(len(text)):
		if text[i].isalpha():
			counter = text.count(text[i])
			if [text[i], counter] not in char_list:
				char_list.append([text[i], counter])
	char_set = sorted(char_list)
	return dict(char_set)

print(count_char(text))


# /11/ Create a dictionary with your own personal details, feel free to be 
# creative and funny so for example, you could include key-value pairs with 
# quirky fact, fav quote, pet. Practice adding, modifying, accesing.

andreea_dict = {
	'age': 37,
	'job': 'Scrum Master',
	'passion': 'coding',
	'favourite music': 'nursery rhymes',
	'favourite food ': 'Dim Sum',
	'dream': 'become a University professor',
	'pet': 'a dog called little prick'
}

# access
print(andreea_dict['dream'])
# print(andreea_dict['coding'])  # error, as you can only print by key, not value

# add
andreea_dict['laptop'] = "MacBook Air"
andreea_dict['phone'] = 'all things Apple!!!'
andreea_dict['country'] = 'the way too hot Malaysia'
andreea_dict['sports'] = 'yoga'
# print(andreea_dict)

# modify 
andreea_dict['dream'] = 'build awesome products with Python'
# print(andreea_dict)
andreea_dict['passion'] = 'reading allll the boooks'
# print(andreea_dict)
del andreea_dict['country']
print('~~~~~~'*10)
print(andreea_dict)
del andreea_dict['favourite music']
print('~~~~~~'*10)
print(andreea_dict)

# clears a dictionary but doesn't erase it
andreea_dict.clear()
print(andreea_dict)

# /12/ Review the chat reply of today's beautiful class interaction and instantiate 
# a student variable for everyone who shared their dream.

class Student():
	def __init__(self, name, discord_id, fav_food, dream):
		self.name = name
		self.discord_id = discord_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + ' ' + self.discord_id + ' ' + self.fav_food + ' ' + self.dream) 


s1 = Student('Virginia Balseiro', 'yesvirginia', 'pasta', 'moving to Europe')
s2 = Student('Andreea Visanoiu', 'Andreea[Gold]', 'wontonmee', 'university professor')
s3 = Student('Cristina Tarantino', 'CristyTarantino[Gold]', 'pasta', 'being an amazing developer')
s4 = Student("Jessi_RS", "Jessi_RS[Gold]#7015", "pasta", "work as developer by end of the year")
s5 = Student("alteredco", "alteredco[GOLD]", "sushi", "dream big")
s6 = Student("Deb Cupitt", "Deb[GOLD]", "chocolate", "gender equity")
s7 = Student("Marwa Qabeel", "Marwa Qabeel[GOLD]", "", "Data Analyst")
s8 = Student("Sacha Young", "sacha[Gold]", "French fries", "return to research")
s9 = Student("Bituin Callanta", "bituin [gold]", "sashimi", "lessen the gender wage gap")

s1.my_print()
s2.my_print()
s3.my_print()
s4.my_print()
s5.my_print()
s6.my_print()
s7.my_print()
s8.my_print()
s9.my_print()


# /13/ Translate the real world 1MWTT student into a Student class, decide on all 
# the attributes that would be meaningful.

class Student():
	def __init__(self, firstname, lastname, email, country, countrycode, phone, github, programming_level, course_objective):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.country = country
		self.countrycode = countrycode
		self.phone = phone
		self.github = github
		self.programming_level = programming_level
		self.course_objective = course_objective




## OPTIONAL ## 

# --------------- Do Python the Hard Way ex. 39 exercise ------------------------

# /6/ Mapping with cities and states/regions in your country or some other country.

counties = {
	"Bucuresti": "Buc",
	"Arges": "AG",
	"Maramures": "MR",
	"Olt": "OT",
	"Constanta": "CT",
	"Brasov": "BV",
	"Cluj-Napoca": "CJ",
	"Sibiu": "SB",
	"Timis": "TM",
	"Bihor": "BH"
}

#create a basic set of states and some cities in them
towns = {
	"AG": "Pitesti",
	"SB": "Sibiu",
	"OT": "Slatina",
	"TM": "Timisoara",
	"BH": "Oradea",
	"CJ": "Cluj",
	"Buc": "Bucuresti"

}

# add some more cities
towns["TM"] = "Timisoara"
towns["MR"] = "Baia Mare"
towns["CT"] = "Constanta"
towns["MR"] = "Baia Mare"
towns["CT"] = "Constanta"
towns["BV"] = "Brasov"


# print some cities 
print('*' * 30)
print(towns["TM"], " is a town in the county of Timis, Romania.")
print("Arges county has as city ", towns["AG"], ".")
print("Oradea is situated in the county", counties["Bihor"], ".")

# print some states
print('*' * 30)
print("Bucuresti abbreviation is", counties["Bucuresti"], ".")
print("The abbreviation of Cluj-Napoca is", counties["Cluj-Napoca"],".")

# do it by using the state and cities dict
print('*' * 30)
print("Arges has:", towns[counties["Arges"]])
print("Timis has:", towns[counties["Timis"]])
print("Bihor has:", towns[counties["Bihor"]])

# print every state abbreviation
print('*' * 30)
for county, abbrev in list(counties.items()):
	print(f"{county} is abbreviated as {abbrev}")


# print every city in state
print('*' * 30)
for abbrev, town in list(towns.items()):
	print(f"{abbrev} has the town {town}.")

# now do both at the same time
print('*' * 30)
for county, abbrev in list(counties.items()):
	print(f"{county} county is abbreviated as {abbrev}.")
	print(f"and has city {towns[abbrev]}")
	

# safely get a abbreviation by state that might not be there
print('*' * 30)
county = counties.get("Teleorman")

if not county:
	print("Sorry, no Teleorman")

# get a city with a default value
print('*' * 30)
town = towns.get("TL", "Doesn't exist")
print(f"The city for the county of 'TL' is {town}")

# /7/ Find the Python documentation for dictionaries and try to do even more 
# things to them.

# create a dictionary
released = {
	"iPhone": 2007,
	"iPhone 3G": 2008,
	"iPhone 4": 2010,
	"iPhone 5": 2012,
	"iPhone 6": 2013,
	"iPhone 7": 2015,
	'iPhone X': 2017
} 
# print(released)

# add a value to the dictionary
released["iPhone 8"] = 2016
# print(released)

# remove a key-value pair with the del operator
del released["iPhone 3G"]
# print(released)

# check the length  = the number of pairs
print(len(released))

# check if a key exists in the dictionary
for item in released:
	if "iPhone 11" in released:
		print("Key found!")
		break
	else:
		print("No keys found with that value.")
		break

# get a value of a specific key
print(released.get("iPhone", 'none'))


# print all keys with a for loop
print('*' * 30)
print('iPhone releases so far: ')
print('_' * 10)
for release in released:
	print(release) 

# print all keys and values
print("<>" * 30)
for key, val in released.items():
	print(key, "===>", val)

# get only the keys from the dictionary
print("<<>>" * 20)
phones = released.keys()
print(phones)

print("This dictionary contains these keys:"," ".join(released))
print("This dictionary containes these keys:", " ", released.keys())

# print the values
print(">><<" * 20)
print(released["iPhone"])
print("Values")

# printint with ppprint
print("<>" * 30)
import pprint
pprint.pprint(released)

# sort the dictionary
print("/\\" * 20)
for key, value in sorted(released.items()):
	print(key, value)

print("/\\" * 20)
for phones in sorted(released, key = len):
	print(phones, released[phones])

# counting
print("@" * 40)
count = {}
for element in released:
	count[element] = count.get(element, 0) + 1 
print(count)


# /8/ Find out what you can't do with dictionaries. A big one is that they do not 
# have order, so try playing with that.
# an ordered dictionary - .OrderedDict

import collections

print("Regular dicionary: ")
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
	print(k, v)

print("\nOrderedDict:")
d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
	print(k, v)

import collections

print('dict       :',)
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict:',)

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)


# /9/ Write a test to check the outcome of the alice_in_wonderfland task: one test for 
# list of lists, and one test for dictionary output.

# n/a

# /10/ Come up with a whole taxonomy of Classes for 1MWTT
# Person()
# Student()
# Mentor()
# Volunteer()
# Employer() 
# Feel free to suggest/invent and also use mixing, decorators, and any other design patterns that you see would help reach 
# the mission of 1 million women to tech by 2020.

#n/a


# -------------- Python the Hard Way ex 40 Study Drills -----------------


# /11/ Write some more songs using this and make sure you understand that you're 
# passing a list of strings as the lyrics.

class MySong(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def play_song(self):
		for line in self.lyrics:
			print(line)


eminem_stan = MySong(["The tea's run cold, I wonder why",
					"Got out of bed at all",
					"The morning rain clouds up my window",
					"And I can't see at all",
					"But even if I could it would all be gray",
					"But your picture on my wall",
					"It reminds me, that it's not bad, it's not so bad"
					])


pink_sober = MySong(["I'm safe, up high, nothing can touch me",
					"But why I feel this party's over",
					"No pain inside, you're my protection",
					"But how do I feel so good sober"
					])


gwen_just_a_girl = MySong(["'Cause I'm just a girls, the little ol' me",
						   "Well don't let me out of your sight",
						   "Oh, I'm just a girl, all pretty and petite",
						   "So don't let me have any rights",
						   "Oh, I've had it up to here!"
							])

aretha_respect = MySong(["R-E-S-P-E-C-T",
						"Find out what it means to me",
						"R-E-S-P-E-C-T",
						"Take care, TCB"
						])

eminem_stan.play_song()
print("<>" * 10)
pink_sober.play_song()
print("<>" * 10)
gwen_just_a_girl.play_song()
print("<>" * 10)
aretha_respect.play_song()


# /12/ Put the lyrics in a separate variable, then pass that variable to the 
# class to use instead.

class MySong(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def play_song(self):
		for line in self.lyrics:
			print(line)

my_lyrics = (["'Cause I'm just a girls, the little ol' me",
 						   "Well don't let me out of your sight",
 						   "Oh, I'm just a girl, all pretty and petite",
 						   "So don't let me have any rights",
 						   "Oh, I've had it up to here!"
 							])

gwen_just_a_girl = MySong(my_lyrics)
print(gwen_just_a_girl.play_song())

# /13/ See if you can hack on this and make it do more things. Don't worry if you 
# have no idea how, just give it a try, see what happens. Break it, trash it, 
# thrash it, you can't hurt it.

# ----- need more study for this one ------------- 

# /14/ Search online for "object-oriented programming" and try to overflow your brain 
# with what you read. Don't worry if it makes absolutely no sense to you. 
# Half of that stuff makes no sense to me too.

#.DONE---------------------------




# ---------------------------------> DAY3 <----------------------------------

# /15/ install pip, NLTK, Anaconda and Jupyter Notebook
# DONE----------------------------

# /16/ Exercise #5 from http://www.nltk.org/book/ch01.html ☼ Compare the lexical diversity scores 
# for humor and romance fiction in 1.1. Which genre is more lexically diverse?

#I decided for now not to get into nltk, as there is no realy time and I'd rather continue 
# with Python. So I won't do the exercises related to nlp. 











