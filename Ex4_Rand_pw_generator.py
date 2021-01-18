""" Generates random password"""

import random
import string

charac_list = []  # Initialise list of empty characters

letters = [a for a in string.ascii_letters]
charac_list.append(letters)

numbers = [i for i in range(1,10)]
charac_list.append(numbers)

special_charac = [z for z in '!@#$%^&*()_']
charac_list.append(special_charac)

charac_list = [item for sublist in charac_list for item in sublist]

def generate_pw(pw_len=10):
    pw = []  # Create empty list
    for i in range(pw_len):
        pw.append(str(random.choice(charac_list)))
    pw_str = ''.join(pw)
    return pw_str

print(generate_pw())