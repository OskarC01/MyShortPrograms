import random

energy = 1000
energy_per_move = 0
energy_per_move_cost = 100

coins = 0
coins_per_move = 0
coins_per_move_cost = 100

chest_drop_chance = 50
chest_drop_chance_cost = 100
better_chest_loot = 0

additional_move_chance = 0

amount_of_basic = 0
amount_of_rare = 0
amount_of_epic = 0
amount_of_legendary = 0
amount_of_MYTHIC = 0
chests_dropped_total = 0

chests_dropped_list = [['basic', amount_of_basic], ['rare', amount_of_rare], [
    'epic', amount_of_epic], ['legendary', amount_of_legendary], ['MYTHIC', amount_of_MYTHIC]]
moves_made = 0

x = 0
y = 0

chests_rarity = ['basic', 'rare', 'epic', 'legendary', 'MYTHIC']
chests_drop_chance = [0.5, 0.2, 0.15, 0.04, 0.01]

"""
    Showing player's position on the map in x, y format
    x - forward (+), backwards(-)
    y - left (-), right (+)
"""


def show_position():
    print(f"""
                Your Position on the map
                x: {x}
                y: {y}
    """)


"""
    Showing all the statistics in the game you currently have
"""


def stats():
    print(f"""
                x: {x},  y: {y}
                coins - {coins},   energy - {energy}
                total chests dropped - {chests_dropped_total}
                moves made - {moves_made}
                                                        Bonuses:
                Passive Income - +{coins_per_move},   Energy Flow - +{energy_per_move},   Luck - {chest_drop_chance}%
    """)


"""
    Allows you to buy bonuses that boost your gameplay
"""


def buy_bonus():
    print(f"""
                1 - buy Passive Income (+5) - cost: {coins_per_move_cost}
                2 - buy Energy Flow (+5) - cost: {energy_per_move_cost}
                3 - buy Luck (+5) - cost: {chest_drop_chance_cost}
                4 - exit
    """)


def list_of_bonuses():
    print(f"""
                Passive Income - Get passive income every move - {coins_per_move}
                Energy Flow - Get more energy every move - {energy_per_move}
                Luck - Higher chance for dropping chest every round - {chest_drop_chance}
    """)


def chest_drops():
    print(f"""
                Chance for any chest = {chest_drop_chance}%
                Chests can contain:
                Basic - between 90 and 110 coins (50%)
                Rare - between 180 and 220 coins (20%)
                Epic - between 450 and 550 coins (15%)
                Legendary - between 675 and 825 coins (4%)
                MYTHIC - between 900 and 1100 coins (1%)
    """)


"""
    Gives value between two price ranges
    Params: value->int percentRange->int (=10)
    Returns: int
"""


def approximate_value(value, percentRange=10):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)


def chests_dropped():
    print(f"""
                Total chests dropped: {chests_dropped_total}

                Basic chests dropped: {chests_dropped_list[0]}
                Rare chests dropped: {chests_dropped_list[1]}
                Epic chests dropped: {chests_dropped_list[2]}
                Legendary chests dropped: {chests_dropped_list[3]}
                MYTHIC chests dropped: {chests_dropped_list[4]}
    """)


print("""
                                        Game Info:

                This game is all about making choices and moving around the map.
                You can go in four directions - forward, left, backwards, right.
                Every move you have a chance to find a chest with coins inside.
                With coins you can buy bonuses which helps you in game.
                Bonus cost is growing every time you buy one.
                BE CAREFUL - if your energy runs down the game ends
                Have Fun!

""")


move_range = int(input(
    'Choose your move range for whole game (min is 1, max is 10) - move range depends on energy energy consumption every move: '))


while energy != 0:
    if move_range < 1 or move_range > 10:
        print("Wrong move range!")
        break
    choice = input("""
                Choose your next move: 
                w - go straight
                a - go left
                s - go back
                d - go right
                1 - check your position (the position is given as x and y)
                2 - check stats
                3 - buy bonuses
                4 - my bonuses
                5 - chests info
                6 - my chests
                7 - END GAME
    """)
    if choice == 'w':
        chest_drop = random.randint(1, 2)
        chest_loot = random.choices(chests_rarity, chests_drop_chance)
        x += move_range
        coins += coins_per_move
        energy -= move_range
        energy += energy_per_move
        moves_made += 1
        if chest_drop == 1:
            if chest_loot == ['basic']:
                coins_from_chest = approximate_value(100)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_basic += 1
                chests_dropped_list[0][1] += 1
                print(
                    f'You have found basic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['rare']:
                coins_from_chest = approximate_value(200)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_rare += 1
                chests_dropped_list[1][1] += 1
                print(
                    f'You have found rare chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['epic']:
                coins_from_chest = approximate_value(500)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_epic += 1
                chests_dropped_list[2][1] += 1
                print(
                    f'You have found epic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['legendary']:
                coins_from_chest = approximate_value(750)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_legendary += 1
                chests_dropped_list[3][1] += 1
                print(
                    f'You have found legendary chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['MYTHIC']:
                coins_from_chest = approximate_value(1000)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_MYTHIC += 1
                chests_dropped_list[4][1] += 1
                print(
                    f'You have found MYTHIC chest with {coins_from_chest} coins inside!')
        else:
            continue

    elif choice == 'a':
        chest_drop = random.randint(1, 2)
        chest_loot = random.choices(chests_rarity, chests_drop_chance)
        y -= move_range
        coins += coins_per_move
        energy -= move_range
        energy += energy_per_move
        moves_made += 1
        if chest_drop == 1:
            if chest_loot == ['basic']:
                coins_from_chest = approximate_value(100)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_basic += 1
                chests_dropped_list[0][1] += 1
                print(
                    f'You have found basic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['rare']:
                coins_from_chest = approximate_value(200)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_rare += 1
                chests_dropped_list[1][1] += 1
                print(
                    f'You have found rare chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['epic']:
                coins_from_chest = approximate_value(500)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_epic += 1
                chests_dropped_list[2][1] += 1
                print(
                    f'You have found epic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['legendary']:
                coins_from_chest = approximate_value(750)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_legendary += 1
                chests_dropped_list[3][1] += 1
                print(
                    f'You have found legendary chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['MYTHIC']:
                coins_from_chest = approximate_value(1000)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_MYTHIC += 1
                chests_dropped_list[4][1] += 1
                print(
                    f'You have found MYTHIC chest with {coins_from_chest} coins inside!')
        else:
            continue

    elif choice == 's':
        chest_drop = random.randint(1, 2)
        chest_loot = random.choices(chests_rarity, chests_drop_chance)
        x -= move_range
        coins += coins_per_move
        energy -= move_range
        energy += energy_per_move
        moves_made += 1
        if chest_drop == 1:
            if chest_loot == ['basic']:
                coins_from_chest = approximate_value(100)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_basic += 1
                chests_dropped_list[0][1] += 1
                print(
                    f'You have found basic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['rare']:
                coins_from_chest = approximate_value(200)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_rare += 1
                chests_dropped_list[1][1] += 1
                print(
                    f'You have found rare chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['epic']:
                coins_from_chest = approximate_value(500)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_epic += 1
                chests_dropped_list[2][1] += 1
                print(
                    f'You have found epic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['legendary']:
                coins_from_chest = approximate_value(750)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_legendary += 1
                chests_dropped_list[3][1] += 1
                print(
                    f'You have found legendary chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['MYTHIC']:
                coins_from_chest = approximate_value(1000)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_MYTHIC += 1
                chests_dropped_list[4][1] += 1
                print(
                    f'You have found MYTHIC chest with {coins_from_chest} coins inside!')
        else:
            continue

    elif choice == 'd':
        chest_drop = random.randint(1, 2)
        chest_loot = random.choices(chests_rarity, chests_drop_chance)
        y += move_range
        coins += coins_per_move
        energy -= move_range
        energy += energy_per_move
        moves_made += 1
        if chest_drop == 1:
            if chest_loot == ['basic']:
                coins_from_chest = approximate_value(100)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_basic += 1
                chests_dropped_list[0][1] += 1
                print(
                    f'You have found basic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['rare']:
                coins_from_chest = approximate_value(200)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_rare += 1
                chests_dropped_list[1][1] += 1
                print(
                    f'You have found rare chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['epic']:
                coins_from_chest = approximate_value(500)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_epic += 1
                chests_dropped_list[2][1] += 1
                print(
                    f'You have found epic chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['legendary']:
                coins_from_chest = approximate_value(750)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_legendary += 1
                chests_dropped_list[3][1] += 1
                print(
                    f'You have found legendary chest with {coins_from_chest} coins inside.')

            elif chest_loot == ['MYTHIC']:
                coins_from_chest = approximate_value(1000)
                coins += coins_from_chest
                chests_dropped_total += 1
                amount_of_MYTHIC += 1
                chests_dropped_list[4][1] += 1
                print(
                    f'You have found MYTHIC chest with {coins_from_chest} coins inside!')
        else:
            continue

    elif choice == '1':
        show_position()

    elif choice == '2':
        stats()

    elif choice == '3':
        buy_bonus()
        bonusChoice = (input("Your choice: "))
        if bonusChoice == '1':
            if coins > coins_per_move_cost:
                coins -= coins_per_move_cost
                coins_per_move += 5
                coins_per_move_cost += 100
                print('You have successfully bought coins_per_move bonus')
                continue
            else:
                print('Not enough coins.')
                continue

        elif bonusChoice == '2':
            if coins > energy_per_move_cost:
                coins -= energy_per_move_cost
                energy_per_move += 5
                energy_per_move_cost += 100
                print('You have successfully bought energy_per_move bonus')
                continue
            else:
                print('Not enough coins.')
                continue

        elif bonusChoice == '3':
            if coins > chest_drop_chance_cost:
                coins -= chest_drop_chance_cost
                chest_drop_chance += 5
                chest_drop_chance_cost += 100
                print('You have successfully bought chest_drop_chance bonus')
                continue
            else:
                print('Not enough coins.')
                continue

        elif choice == '4':
            continue

    elif choice == '4':
        list_of_bonuses()

    elif choice == '5':
        chest_drops()

    elif choice == '6':
        chests_dropped()

    elif choice == '7':
        endgame = input('Are You sure that You want to finish the game? (y/n)')
        if endgame.lower() == 'y':
            print('Your stats: ')
            stats()
            energy = 0

else:
    print('Out of energy, GAME OVER.')
