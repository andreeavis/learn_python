# frequency_distribution = [
# ["a", 35000],
# "b", 8000],

# ...
# ["z", 450]
# ]

# this is difficult if you have millions of entries
# this is where dictionary come in

# dictionary is an unordered collection; you can't have repetition

# dictionary constructor function - creates a dictionaryname
andreea_vis = dict(name = "Andreea Vis", discord_id = "#3454", fav_food = "bread")

my_dict = {
	"a": 35000,
	"b": 8000,
	"z": 450
}

print(my_dict)

# access
print(my_dict["a"])


# add
my_dict["Rocio"] = "pretty"
print(my_dict["Rocio"])
print(my_dict)


# modify
my_dict["a"] = 50
print(my_dict["a"])
print(my_dict)

# delete item
print(len(my_dict))
del(my_dict["a"])
print(my_dict)
print(len(my_dict))

# delete whole dictionary 


















