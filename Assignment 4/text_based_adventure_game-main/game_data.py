list_of_positions = {
    'A': {'positions': ('B', 'C'), 'directions': {'N': 'B', 'W': 'C', 'E': None, 'S': None}, 'question': 'Welcome to the Game, You are in the top floor of the building and the fire alarm has gone off! choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'B': {'positions': ('A'), 'directions': {'N': None, 'W': None, 'E': None, 'S':'A'}, 'question': 'There is no way out from here. Please go back! Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'C': {'positions': ('A', 'D'), 'directions': {'N': 'D', 'W': None, 'E': 'A', 'S': None}, 'question': 'Quick, the stairs are there! Don\'t use the lift! Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'D': {'positions': ('C', 'E', 'F'), 'directions': {'N': 'E', 'W': 'F', 'E': None, 'S': 'C'}, 'question': 'You are now on floor 2 by the stairway. Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'E': {'positions': ('D'), 'directions': {'N': None, 'W': None, 'E': None, 'S': 'D'}, 'question': 'There is no way out from here. Please go back! Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'F': {'positions': ('D', 'G', 'H', 'I'), 'directions': {'N': 'G', 'E': 'D', 'W': 'H', 'S': 'I'}, 'question': 'You are now on the first floor, and there are three doors. We heard a meow; there is a cat in one of the rooms. Please rescue the cat too. Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'G': {'positions': ('F', 'J'), 'directions': {'N': None, 'W': None, 'E': 'J', 'S': 'F'}, 'question': 'You have found the cat so you can move on. Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'H': {'positions': ('F'), 'directions': {'N': None, 'E': 'F', 'W': None, 'S': None}, 'question': 'You have found the cat! Great job! Choose a direction to escape: N, E, S or W ', 'isThereCat': True},
    'I': {'positions': ('F'), 'directions': {'N': 'F', 'W': None, 'E': None, 'S': None}, 'question': 'The cat is not in here. Please go back! Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'J': {'positions': ('G', 'K', 'L', 'N'), 'directions': {'N': 'K', 'W': 'G', 'E': 'N', 'S': 'L'}, 'question': 'You are now on floor G. Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'K': {'positions': ('J', 'M'), 'directions': {'N': None, 'W': 'M', 'E': None, 'S': 'J'}, 'question': 'Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'L': {'positions': ('J', 'M'), 'directions': {'E': 'M', 'W': None, 'N': 'J', 'S': None}, 'question': 'There is no way out from here. Please go back! Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'M': {'positions': ('K', 'L'), 'directions': {'N': None, 'S': None, 'E': 'K', 'W': 'L'}, 'question': 'This is an empty room. Choose a direction to escape: N, E, S or W ', 'isThereCat': False},
    'N': {'positions': (), 'directions': {'N': None, 'W': None, 'E': None, 'S': None}, 'question': 'You have escaped! ', 'isThereCat': False, 'requiredCat': False}
    }

found_cat = False
starting_position = 'A'