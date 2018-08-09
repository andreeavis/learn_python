text = ''

# while text != 'bye':
# 	text = input('say something please ')
# 	print('you said ' + text + '.')
# 	if text == 'bye':
# 		print('good bye to you too')
# 		break

# the above more elegant
while text != 'bye':
	text = input('say something please : ')
	print('you said ' + text + '.')
	
# print('good bye to you too') # as soon as the while is finished, it says good bye 
		


i = 1
while  i < 11:
	print(i)
	i = i + 1

# #if i write it without an increment statement, i'm creating an infinite loop
# # as i will always be 1, 1 is always < 11

j = 0
while j < 11:
	print(j) # will print 1-2-3
	if j == 3:
		break
	# print(j) = #with print here, j reaches 3 before it is printed
	j += 1   # same as j = j + 1



for x in range(10):
	print(x)

for x in range(5, 10):
	print(x)

for x in range(5, 50, 3):
	print(x)



students = ['AndreeaV', 'Jessi RS', 'Marta B', 'Cristina Tarantino', 'Mary J']
for s in students:
	if len(s) > 7:
		print(s + ' is an amazing Pythonista and has a very long name!')
		if len(s) > 20:
			print('Supercalifragilisticexpialidicious')
	elif len(s) == 6:
		print(s + ' is an amazing Pythonista and has a 6 char long name!')
	else: 
		print(s + ' is an amazing Pythonista and is a minimalist!')



# for s in students: #we tend to use the first letter of a list as variable 
# examples: for c in characters; for c in cars; for m in members ... and so on (human convention)


students = ['AndreeaV', 'Jessi RS', 'Marta B', 'Cristina Tarantino', 'Mary J']

for s in students:
	print(s)

#list comprehension
# usernames = [dosomething(element) for everyelement in list]

usernames = [print(s) for s in students]

usernames = [s + "@1mwtt" for s in students]

print(usernames)

print(usernames.sort())

students.append("Mariaelena")
print(students)

students.pop()
print(students)

students.sort()
print(students)
