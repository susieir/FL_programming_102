## Guessing Game


def middle(max, min):
    "Returns the middle of range"
    return int((max + min) / 2)

def num_guesses_response(n, max, min):
    """ Returns reponse to "S" with number and number of guesses"""
    if n > 1:
        return print("Your number is {}, it took me {} guesses".format(middle(max, min), n))
    else:
        return print("Your number is {}, it took me {} guess".format(middle(max, min), n))


def generate_input(max, min):
    """ Generates input for a given range"""
    return input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle(max, min))).upper()


def main(max, min):
    max = 101
    min = 0

    print("Think of a number between 1 and 100")

    for n in range(1, 9):
        answer = generate_input(max, min)
        if answer == "H":
            min = middle(max, min)
        elif answer == "L":
            max = middle(max, min)
        else:
            num_guesses_response(n, max, min)
            quit()


main(101, 0)

