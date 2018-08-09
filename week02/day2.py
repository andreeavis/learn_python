# # the chr() 
for i in range(65, 65+2*26):
	print(i, " stands for", chr(i))

# # fix the above so it prints only A-Z and a-z (Figure out what to do with 91-96)

# for i in range(65, 256):
# 	print(i, " stands for", chr(i))


M = 'land'
o = 'water'
world = [
		 [o, o, o, o, o, o, o, o, o, o, o, o],
		 [o, o, o, o, M, M, o, o, o, o, o],
		 [o, o, o, o, o, o, o, o, M, M, o], 
		 [o, o, o, M, o, o, M, M, o, o, o],
		 [o, o, o, o, M, M, M, M, M, M, o],
		 [o, M, o, o, o, o, o, M, o, o, o],
		 [o, M, M, M, M, o, M, o, o, o, o],
		 [M, M, M, M, M, M, M, M, M, M, M],
		 [M, o, o, o, o, o, M, o, o, o, o],
		 [o, o, o, o, o, o, o, o, o, o, o]
		 ]

def continent_counter(world, x, y):
	if world[y][x] != 'land':
		return 0
	
	size = 1
	world[y][x] = 'counted land'
	# now we count all neihboring tiles
	# row bove
	size = size + continent_counter(world, x-1, y-1)
	print('First recursion: ', size)
	size = size + continent_counter(world, x  , y-1)
	size = size + continent_counter(world, x+1, y-1) 
	# same row
	size = size + continent_counter(world, x-1, y ) 
	size = size + continent_counter(world, x+1, y ) 
	# row below
	size = size + continent_counter(world, x-1, y+1) 
	size = size + continent_counter(world, x  , y+1) 
	size = size + continent_counter(world, x+1, y+1)
	return size 

print(continent_counter(world, 5, 5))




# a = 'Elle J'
# b = 'Sarah Alkhateeb'
# c = 'Paula Bernal'
# d = 'Melinda Gates'
# students = [a, b, c, d]

# print(students)

# sisters = ['Cristina Tarantino', 'Jesse RS', 'alteredco', 'LamboFantastico']
# print(sisters)

# members = [students, sisters]

# # if I want "LamboFantastico"

# print(members[1][3])

















