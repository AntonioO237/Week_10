# For loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc. 

# Example 1: Prints the integers as x
for x in range(1,11):
    print(x)

# Example 2: Reverses the order of printing
for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR")

# Example 3: Allows you to skip every other z (x, y, z)
for x in range(1, 11, 3):
    print(x)
    
# Example 4: Allows for a variable to br printed as x
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# Example 5: Skips over set x's
for x in range(1, 21):
    if x == 13 or x == 15 or x == 18:
        continue
    else:
        print(x)

# Example 6: Stops the code at x
for x in range(1, 21):
    if x == 13 :
        break
    else:
        print(x)