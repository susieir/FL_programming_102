## Guessing Game

max = 101
min = 0

print("Think of a number between 1 and 100")


middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 1 guess".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 2 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 3 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 4 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 5 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 6 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 7 guesses".format(middle))
  quit()

middle = int((max + min)/2)
answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
if answer == "H":
  min = middle
elif answer == "L":
  max = middle
else:
  print("Your number is {}, it took me 8 guesses".format(middle))
  quit()