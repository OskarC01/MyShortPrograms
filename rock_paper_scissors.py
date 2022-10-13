import random


players_points = 0
computer_points = 0


def after_won_round_info(player_pts, computer_pts, players_choice, computer_choice):
    return f"""
            Congratulations, You won! Your {players_choice} beats {computer_choice}.
            Player - {player_pts} : {computer_pts} - Computer
            """


def after_lost_round_info(player_pts, computer_pts, players_choice, computer_choice):
    return f"""
            This time computer has won. Hes {computer_choice} beats {players_choice}.\n
            Player - {player_pts} : {computer_pts} - Computer
            """


while True:
    game_dict = {1: 'rock', 2: 'paper', 3: 'scissors'}
    computer_choice = random.sample(['rock', 'paper', 'scissors'], 1)[0]

    players_choice = int(input("""Choose what do you want to play this turn
            1 - Rock
            2 - Paper
            3 - Scissors
    """))
    players_choice = game_dict[players_choice]

    if computer_choice == players_choice:
        print(f'Draw!, both You and computer have chosen {computer_choice}.')
        print(f'Player - {players_points} : {computer_points} - Computer')

    elif computer_choice == 'rock':
        if players_choice == 'paper':
            players_points += 1
            print(after_won_round_info(
                players_points, computer_points, players_choice, computer_choice))
        elif players_choice == 'scissors':
            computer_points += 1
            print(after_lost_round_info(
                players_points, computer_points, players_choice, computer_choice))

    elif computer_choice == 'paper':
        if players_choice == 'rock':
            computer_points += 1
            print(after_lost_round_info(
                players_points, computer_points, players_choice, computer_choice))
        elif players_choice == 'scissors':
            players_points += 1
            print(after_won_round_info(
                players_points, computer_points, players_choice, computer_choice))

    elif computer_choice == 'scissors':
        if players_choice == 'rock':
            players_points += 1
            print(after_won_round_info(
                players_points, computer_points, players_choice, computer_choice))
        elif players_choice == 'paper':
            computer_points += 1
            print(after_lost_round_info(
                players_points, computer_points, players_choice, computer_choice))

    else:
        print('Some error ocurred. Try again.')
        continue

    play_again = input('Play again? (y/n):')
    if play_again.lower() != 'y':
        break
