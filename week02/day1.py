# 1) reading & writing, 2) attention to detail and 3) spotting differences are essential

# make a function that returns <n> number of 'moos'


# FUNCTIONS AND PARAMETERS
def moo(n):
	# print('moo' * n)
	return 'moo' * n

# we are calling the function by passing a parameter
# moo(0)
# moo(1)
# moo(2)

#programmers should be lazy; so instead of typing this 3 times, we can do something simpled
# this was more of a test to see if function moo woks; no need if you do unittests 
# for i in range(3):
# 	moo(i)

def ask_recurseively(question):
	print(question)
	reply = input('> ').lower()
	if reply == 'yes':
		return True
	if reply == 'no':
		return False
	else:
		print('Please nswer "yes" or "no.')
		ask_recurseively(question)

ask_recurseively('Do you wet the bed?')

# TESTING
# automated testing: you know your inputs and outputs and u want to make sure
# your program behaves the way you're expecting it
# check test_day1.py


# READING AND WRITING FILES
filename = "alice_in_wonderland.txt"
file = open(filename, 'r')

# for line in file:
# 	print(line)

raw = file.read()

print('from zero to sixty-fixe' + raw[:165])

print(raw[65:500])

print('AGAIN: ' + raw[0:65])
print(raw[65:500])

print('the length of Alice in Wonderland is: ' + str(len(raw)))

# 163815

print(raw[-163000:])

# calculate a table for each letter in the alphabet from a-z and count how many times each letter 
# appears in Alice in Wonderland
# a: 34,650 for example (fancy word for counting stuff is "frequency distribution")
# b: 5,027
# z: 895 





















