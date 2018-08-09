# write a program that telss you hours in a year
print(365 * 24)

# write a program that tells you minutes in a decade
print(10 * 365 * 24 * 60)

# write a program that tells you your age in seconds
print(365 * 37 * 24 * 60 * 60 + (30+31+30+17) * 24 * 60 * 60)

# write a program that tells you how many days it takes 
# for a 32-bit system to timeout if it has a but w/ integer overflow

# calculate n-bit integer
# n-bit integer = −(2^^n−1) to (2^^n−1 − 1)

max32_neg = -(2 ** (32-1) - 1)
max32_poz = (2 ** (32-1) - 1)

print(max(max32_poz, max32_neg))

time_run_out_32 = max32_poz / 100 / 60 / 60 / 24
print(time_run_out_32)
print(int(time_run_out_32))

# how about a 62-bit system
max64_neg = -(2 ** (64-1) - 1)
max64_poz = (2 ** (64-1) - 1)

print(max(max64_poz, max64_neg))

time_run_out_64 = max64_poz / 100 / 60 / 60 / 24
print(time_run_out_64)
print(int(time_run_out_64))

#calculate your age based on your b-day; time of day: 10:00 am
#birthday: 31.03.1981

# b_year_hours = 275 * 24 + (24-10)

# every 4 years; starts with 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016
import datetime
