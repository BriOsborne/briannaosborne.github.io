# Brianna Osborne

def show_instructions():
    # this should print the game name goal and commands while providing a visual barrier for the player.
    print('Space Station Survival Game')
    print('Collect all 6 items before facing Malus.')
    print('Move commands: go North, go South, go East, go West')
    print('Add to Inventory: get item name')
    print('-----------------------------------') # visual barrier.


def show_status(current_room, inventory, rooms):
    # the player will need to know where they are at any point in time.
    print('You are in the {}'.format(current_room))
    print('Inventory:', inventory)

    if 'item' in rooms[current_room]:
        if rooms[current_room]['item'] not in inventory:
            print('You see {}'.format(rooms[current_room]['item']))

    print('-----------------------------------') # visual barrier.


def main():
    # this dictionary will link rooms items and directions.
    rooms = {
        'Crew Quarters': {
            'North': 'Observatory',
            'South': 'Lab',
            'East': 'Control Room',
            'West': 'Engineering Bay'
        },
        'Observatory': {
            'South': 'Crew Quarters',
            'East': 'Cafeteria',
            'item': 'Space Map'
        },
        'Cafeteria': {
            'West': 'Observatory',
            # added this so the first aid kit can be collected before entering the villain room.
            'South': 'Med Bay',
            'item': 'Ration Pack'
        },
        'Engineering Bay': {
            'East': 'Crew Quarters',
            'item': 'Wrench'
        },
        'Lab': {
            'North': 'Crew Quarters',
            'East': 'Cargo Hold',
            'item': 'Data Chip'
        },
        'Cargo Hold': {
            'West': 'Lab',
            'item': 'Oxygen Tank'
        },
        'Control Room': {
            'West': 'Crew Quarters',
            'North': 'Med Bay'
        },
        'Med Bay': {
            'North': 'Cafeteria',
            'South': 'Control Room',
            'item': 'First Aid Kit'
        }
    }

    current_room = 'Crew Quarters'
    inventory = []
    game_running = True

    show_instructions()

    # the game will keep on until the player wins or loses.
    while game_running:
        direction = ''

        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip()
        command = command.title()

        if command == 'Go North':
            direction = 'North'
        elif command == 'Go South':
            direction = 'South'
        elif command == 'Go East':
            direction = 'East'
        elif command == 'Go West':
            direction = 'West'
        elif command.startswith('Get '):
            item = command.replace('Get ', '')

            if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
                if item not in inventory:
                    inventory.append(item)
                    print('{} retrieved!'.format(item))

                    if len(inventory) == 6:
                        print('All items collected! Find Malus in the Control Room to escape.')
                else:
                    print('You already have that item.')
            else:
                print("You can't get that item here.")
        elif command == '':
            print('You did not enter a command.')
        else:
            print('Invalid command!')

        if direction != '':
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                if current_room == 'Control Room':
                    if len(inventory) == 6:
                        print('You collected every item and outsmarted Malus!')
                        print('Congratulations, you won the game!')
                    else:
                        print('Malus found you before you were ready.')
                        print('GAME OVER!')

                    print('Thanks for playing.')
                    game_running = False
            else:
                print("You can't go that way!")


main()
