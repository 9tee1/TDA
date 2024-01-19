from typing import Union
from game_data import list_of_positions, found_cat, starting_position
from game_utils import get_directions, backtracking_required, check_room, check_is_position_last, check_permission

# this function will take the user direction and if the direction is from the dict then if will return direction
def get_direction(user_input: str, position: str) -> Union[None, str]:
    directions = get_directions(position)
    valid_directions = [directions[direction] for direction in user_input if direction in directions]
    if valid_directions:
        return valid_directions[0]
    else:
        print("Invalid direction entered")
        return None

# this function will check if the user has found the cat and return if the cat is found
def find_cat(position: str) -> Union[None, bool]:
    global found_cat
    cat_in_room = check_room(position)
    if cat_in_room:
        print("you found the cat")
        found_cat = True

# once the condition is met where they found the cat the message will changed
def give_instructions(question: str, position: str) -> str:
    if backtracking_required(position, found_cat):
        response = input('There is no way out from here. Please go back! Choose a direction to escape: N, E, S or E ')
    else:
        response = input(question)
    return response

# The recursive function will keep calling itself until the specified condition is met
def get_position(position: str = starting_position) -> None:

    keep_playing = check_is_position_last(position)
    print("Your current position: ",position)

    # If the game hasn't reached the last position, keep playing
    while keep_playing:
        user_input = give_instructions(list_of_positions[position]['question'], position)

        print("Direction given by you: ", user_input)

        #step 2) ask user for direction
        next_position = get_direction(user_input, position)
        if next_position is not None:
            find_cat(next_position)
            is_movement_allowed = check_permission(next_position, found_cat)
            if is_movement_allowed:
                print("you need to find the cat before you can move on")
                get_position('F')
                continue
            else:
                #step 3) pass in the next position
                get_position(next_position)
        else:
            print("The direction does not lead anywhere. Please try again.")
            continue
        break
    #step 4) game stops when reached final position
    if not keep_playing:
        end_game()

def start_game() -> None:
    get_position()

def end_game() -> None:
    print('You have now escaped!')

if __name__ == "__main__":
    # step 1) call this function first
    start_game()
