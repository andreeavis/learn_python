from datetime import date
def calculate_age(dtob):
	today = date.today()
	return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


print()
print(calculate_age(date(1981, 3, 31)))
print(calculate_age(date(2001, 5, 23)))
print()