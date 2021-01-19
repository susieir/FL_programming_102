"""Script that assigns players to a given team from a list"""

# Import modules
from random import choice

# Initialise player list
player_list = ['Harry', 'Ron', 'Hermione', 'Ginny', 'Neville', 'Draco', 'Fred', 'George']


# Create team selector
def team_selector(list):
    """Sorts players randomly into teams for a given list of names"""
    # Initialises empty team lists
    team_A = []  # Initialise team A
    team_B = []  # Initialise team B
    # Check list for issues
    if len(list) == 0:
        return "There are no players"
    elif len(list) == 1:
        return "You need more than one player for a game!"
    else:
        for player in list:
            if len(team_A) > len(team_B):
                team_B.append(player)
            elif len(team_A) < len(team_B):
                team_A.append(player)
            else:
                choice([team_A, team_B]).append(player)
        return team_A, team_B


print(team_selector(player_list))

### Testing
player_list2 = ['Harry', 'Ginny']
player_list3 = ['Harry']
player_list4 = []
player_list5 = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']

print(team_selector(player_list2))
print(team_selector(player_list3))
print(team_selector(player_list4))
print(team_selector(player_list5))
