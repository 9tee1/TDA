from game_data import list_of_positions


# this will get the list of directions
def get_directions(position: str) -> dict:
    return list_of_positions[position]['directions']

# check if the cat is in the room
def check_room(position: str) -> bool:
    return list_of_positions[position]['isThereCat']

# returns true if user is in position F, I or H and have found the cat
def backtracking_required(position: str, found_cat: bool) -> bool:
    return (position in ('F', 'I', 'H')) and found_cat

def check_is_position_last(position: str) -> bool:
    return bool(list_of_positions[position]['positions'])

# check if position is G and the cat is not found
def check_permission(next_position: str, found_cat: bool) -> bool:
    return next_position == 'G' and found_cat is False