import random
from math import sqrt


board_height = 9
board_width = 9

x_key = random.randint(1, board_width)
y_key = random.randint(1, board_height)

x_player = random.randint(1, board_width)
y_player = random.randint(1, board_height)

key_position = [x_key, y_key]
player_position = [x_player, y_player]

session_record = 99

number_of_moves = 0
distance_before_move = sqrt(
    (x_key - player_position[0]) ** 2 + (y_key - player_position[1])**2)


while player_position != key_position:

    number_of_moves += 1
    move = input("""Choose where to move: 

                    W - Up
                    
           A - Left         D - Right

                    S - Down
                                    B - leave game
    """)

    if move.lower() == 'w':
        if player_position[1] < board_height:
            player_position[1] += 1
            print(player_position)
        else:
            print('Cant make this move you are at the wall')
            print(player_position)
            continue

    elif move.lower() == 'a':
        if player_position[0] > 0:
            player_position[0] -= 1
            print(player_position)
        else:
            print('Cant make this move you are at the wall')
            print(player_position)
            continue

    elif move.lower() == 's':
        if player_position[1] > 0:
            player_position[1] -= 1
            print(player_position)
        else:
            print('Cant make this move you are at the wall')
            print(player_position)
            continue

    elif move.lower() == 'd':
        if player_position[0] < board_width:
            player_position[0] += 1
            print(player_position)
        else:
            print('Cant make this move you are at the wall')
            print(player_position)
            continue
    elif move.lower() == 'b':
        print('Exiting game...')
        break

    else:
        print('Something went wrong please try again')
        continue

    distance_after_move = sqrt(
        (x_key - player_position[0]) ** 2 + (y_key - player_position[1]) ** 2)

    if distance_before_move > distance_after_move:
        print('You are getting closer.')
    else:
        print('Wrong direction.')

    distance_before_move = distance_after_move

    if number_of_moves < session_record:
        session_record = number_of_moves


print('Congratulations! The Key is Yours!')
print(f'You have found the key with {number_of_moves} moves.')
print(f'This session record is equal to {session_record} moves.')
