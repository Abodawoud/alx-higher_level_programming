#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"last digit of {number}", end=" ")
if (number < 0) and (number %10 != 0):
    lastdigit = (number * -1) % 10
    print(f"is -{lastdigit}", end=" ")
else:
    lastdigit = number % 10
    print(f"is {lastdigit}", end=" ")

if (lastdigit == 0):
    print("and is 0")
elif (lastdigit > 5):
    print(f"and is greater than 5")
else:
    print(f"and is less than 6 and not 0")


# if (number < 0) and (number %10 != 0):
#     number = number * -1
#     lastdigit = number % 10
#     if lastdigit < 5:
#         print(f"is -{lastdigit} and is less than 6 and not 0")
# else:
#     lastdigit = number % 10
#     if lastdigit > 5:
#         print(f"is {lastdigit} and is greater than 5")
#     else:
#         print(f"is {lastdigit} and is 0")
