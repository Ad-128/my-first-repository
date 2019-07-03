# This file has different patterns to print
# Author : Ad-128
# Date : 03/07/2019

# Pattern-1
# Print a pattern like this -
# 1
# 1 2
# 1 2 3
# 1 2 3 4

star='&'
space=' '
pattern=star+space
print("*")
print("* *")
print("* * *")
print("* * * *")

for i in range(1,5):
    print(i*pattern)




