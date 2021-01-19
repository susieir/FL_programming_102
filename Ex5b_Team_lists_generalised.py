"""Script that assigns players to a given team from a list"""

# Import modules
from random import choice, shuffle
from collections import defaultdict

# Initialise lists
hogwarts_players = ['Harry', 'Ron', 'Hermione', 'Ginny', 'Neville', 'Draco', 'Fred', 'George']
menace_league = ['Gnashers', 'Gnippers']


def team_picker(player_list, team_list):
    """ A function that iterates through the team list and randomly assigns players"""
    team_dict = defaultdict(list) # Initialise empty team dict
    while len(player_list) > 0:
        for team in team_list:
            shuffle(player_list)
            player_picked = choice(player_list)
            team_dict[team].append(player_picked)
            player_list.remove(player_picked)
    return team_dict


print(team_picker(hogwarts_players, menace_league))
