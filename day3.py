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


# fav_number = input("What is your favourite number? ")
# x = int(fav_number)

# print("That's a good number, but " + str(x+1) + " is a much better one!")

# name = (input("What's your full name? "))
# print("Did you know there are " + str(len(name)) + " characters in your name, " + name + "?")

var1 = 'stop'
var2 = 'stressed'
var3 = 'Can you pronounce this sentence backwards?'

print(str(reversed(var1)))