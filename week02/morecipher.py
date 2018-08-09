
message = "This is my message to be coded."
key = 1
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
coded = ''

for symbol in message:
	if symbol in SYMBOLS:
		symbol_index = SYMBOLS.find(symbol)
		# print(symbol_index)

		coded_index = symbol_index + key

		if coded_index >= len(SYMBOLS):
			coded_index = coded_index - len(SYMBOLS)
		elif coded_index < 0:
			coded_index = coded_index + len(SYMBOLS)

		coded += SYMBOLS[coded_index]
	else:
		coded = coded + symbol	
	
print(coded)


message = "Uijt!jt!nz!nfttbhf!up!cf!dpefeA"
key = 1
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
coded = ''

for symbol in message:
	if symbol in SYMBOLS:
		symbol_index = SYMBOLS.find(symbol)
		# print(symbol_index)

		coded_index = symbol_index - key

		if coded_index >= len(SYMBOLS):
			coded_index = coded_index - len(SYMBOLS)
		elif coded_index < 0:
			coded_index = coded_index + len(SYMBOLS)

		coded += SYMBOLS[coded_index]
	else:
		coded = coded + symbol	
	
print(coded)