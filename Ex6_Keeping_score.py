import random

""" Variation 1 - Count scores that equal a target"""
def count(target, list):
    """ Function that counts"""
    counter = 0  # Initialise counter
    for item in list:
        if item == target:
            counter += 1
    return counter

scores = []

for x in range (0, 30):
  scores.append(random.randint(0, 10))

print(scores)

top_scorers = count(10, scores) # Count function called here

print("{0} learners got top marks".format(top_scorers))




""" Variation 2 - Count occurrences of a given item in a string"""
def count_char(target_char, string):
    """ Function that counts"""
    counter = 0  # Initialise counter
    for char in string:
        if char == target_char:
            counter += 1
    return counter

word = "supercalifragilisticexpialidocious"
char = "p"
number_l = count_char(char, word) # Count function called here
print("{} appears {} times in {}".format(char, number_l, word))



""" Variation 2 - Count numbers in a given range"""

min_pass = 6
def count_fails(min_pass_score, list):
    fail_count = 0  # Initialise fail count
    for item in list:  # Iterate through scores
        if item < min_pass_score:  # Add fails to fail_count
            fail_count += 1
    return fail_count

scores = []

for x in range (0, 30):
  scores.append(random.randint(0, 10))

print(scores)

number_fails = count_fails(min_pass, scores) # Count function called here

print("{0} learners failed".format(number_fails))


