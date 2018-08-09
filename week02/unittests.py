# https://stackoverflow.com/questions/3258733/new-to-unit-testing-how-to-write-great-tests
import unittest

def is_prime(number):
	# Return true if number is prime #
	for element in range(number):
		if number % element == 0:
			return False
	return true

def prime_next_prime(number):
	# Print the closest prime number larger than number #
	index = number
	while True:
		index += 1
		if is_prime(index):
			print(index)


