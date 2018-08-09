#classes

# class Student():
# 	discord_id = "Andreea[Gold]"

# # instentiate using the constructor function that we got from the Class
# # this is a constuctor function

# s1 = Student()
# s2 = Student()
# s3 = Student()

# # dot notation 
# print(s1.discord_id)
# print(s2.discord_id)
# print(s3.discord_id)

# class Student():
# 	def __init__(self, firstname, lastname, email, countrycode, 
# 		phone_number, github, country,  
# 		discord_id, fav_food, dream):


class Student():
	def __init__(self, name, discord_id, fav_food, dream):
		self.name = name 
		self.discord_id = discord_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)


# instentiate using the constructor function that we got from the Class
# this is a constuctor function

s1 = Student("Andreea Vis", "Andreea[Gold]", "wontonmee", "Becoming a University teacher ;-)")
s2 = Student("Virginia Balseiro", "VirginiaGoldVolunteer", "pasta", "Moving to europe and working as a dev")
s3 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "pizza", "Becoming a President")
s4 = Student("Sacha Young", "sacha[Gold]", "french fries", "Becoming an artist")

# dot notation 
s1.my_print()
s2.my_print()
s3.my_print()
s4.my_print()

# update properties

s1.fav_food = "icecream"
s1.my_print()

# delete properties; but don't delete properties in classes!!!
# you will error out as my_print tries to access a non-existend attribute

# del s1.fav_food
# s1.my_print()
# print(s1)











