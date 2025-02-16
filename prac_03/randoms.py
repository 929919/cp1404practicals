import random

print(random.randint(5, 20))  # line 1

# What did you see on line 1?
# It will print a random integer between 5 and 20 inclusive.

# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 5, and the largest could have been 19.
print(random.randrange(3, 10, 2))  # line 2

# What did you see on line 2?
# It will print a random number in the range from 3 to 10 with a step of 2 (possible numbers: 3, 5, 7, 9).

# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 3, and the largest could have been 9.
# Could line 2 have produced a 4?
# No, because the step value is 2, so only odd numbers (3, 5, 7, 9) are possible.

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# It will print a random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 2.5, and the largest could have been 5.5.
random_number = random.randint(1, 100)
print(random_number)
