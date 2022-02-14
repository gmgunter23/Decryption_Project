# Text Monster Game
# The goal of this game is to beat the boss monster and claim the prize

# Map of the dungeon
floor2 = ['sword', 'empty', 'stairs down', 'boss monster', 'prize']
floor1 = ['magic stones', 'stairs down', 'empty', 'monster1', 'stairs up']
floor0 = ['empty1', 'sword', 'stairs up', 'monster0', 'empty2']

#prizes in the prize room
prize_room_items = ['sword', 'squirrel', 'goat']

# items in players possession
inventory = []

# player's current position in the dungeon
current_floor = 0
current_room = 0
last_horizontal_move = ''

# game loop
game_state = 'running'
while game_state == 'running':

    # describe the room the player is in
    if current_floor == 0:
        floor = floor0
    elif current_floor == 1:
        floor = floor1
    else:
        floor = floor2
    room = floor[current_room]
    if room == 'empty1':
        print("You are in an empty room and look up and see glowing stones above you.")
    elif room == 'sword':
        print("You enter the room and see a sword.")
    elif room == 'stairs up':
        print("You see some stair leading up.")
    elif room == 'monster0':
        print("You see a monster.")
    elif room == 'empty2':
        print('You are in an empty room.')
    elif room == 'magic stones':
        print('You see magic purple stones laying on the ground.')
    elif room == 'monster1':
        print('You enter the room and see a Purple People Eater.')
    elif room == 'stairs down':
        print('You are now in a room that has stairs leading down.')
    elif room == 'empty':
        print('You are now in a room and hear a monster growling in the room to the right.')
    elif room == 'prize':
        print(f'You walk into the room and see {prize_room_items}!!!')
        chosen_item = input('Which item would you like to grab? > ')
        inventory.append(chosen_item)
        prize_room_items.remove(chosen_item)
    elif room == 'boss monster':
        print('You enter one of the final room and see Elon Musk with a sword wanting to duel, you can either quit and restart the game or you can fight him.')
    elif room == 'magic stones':
        print('You enter a room and see magic stone laying on the ground.')
        
        
    # more code here to describe each scenario

    # get command from the player
    while True:
        choice = input("What do you want to do? (type 'help' for a list of commands) > ")
        if choice == 'help':
            print("right, left, up, down, fight, grab, drop, inventory, look, map, quit")
            break
        elif choice == 'quit':
            print("Bye for now...")
            game_state = 'stop'
            break
        elif choice == 'right':
            if current_room == 'monster' and last_horizontal_move == 'right':
                print ('You ran past the monster and he ate you.....')
                game_state = 'over'
                break
            current_room += 1
            last_horizontal_move == 'right'
            break
        elif choice == 'left':
            if current_room == 'monster' and last_horizontal_move == 'left':
                print ('You ran past the monster and he ate you.......')
                game_state = 'lover'
                current_room -= 1
                last_horizontal_move == 'left'
                break
            else:
                print('You have gone back to the start of the floor and cannot go farther left....')
                break
        elif choice == 'up':
            if room == 'stairs up':
                current_floor += 1
                print('You climbed up the stairs.')
                break
            else: 
                print('You cannont go up the stairs here!!! Go find a room with stairs in it.')
                break  
        elif choice == 'down':
            if room == 'stairs down':
                current_floor -= 1
                break
            else:
                print('You cannont go down the stair right here.... Go find a room with stairs in it.')       
                break       
        elif choice == 'grab':
            if room == 'sword' or room == 'magic stones' or room == 'prize':
                inventory.append(room)
                floor[current_room] = 'empty2'
                break
            else:
                print("There is nothing here to grab.")
                break
        elif choice == 'inventory':
            print(inventory)
            break
        elif choice == 'drop':
            if room == 'empty':
                print[inventory]
                drop_choice = input('What would you like to drop out of your inventory? > ')
                inventory.remove(drop_choice)
                floor[current_room] = drop_choice
        elif choice == 'fight':
            if room == 'monster':
                if 'sword' in inventory:
                    print('You defeated a monster!')
                    floor[current_room] = 'empty'
                    inventory.remove('sword')
                    break
                else:
                    print('You need a sword to kill the a monster!')
                break 
            #boss monster
            elif room == 'boss monster':
                if 'sword' in inventory and 'magic stones' in inventory:
                    print('YOU HAVE BEAT ELON MUSK AND WON THE GAME!!! Congrats!!')   
                else: 
                    print('You cannot fight anything here.')
            break
        elif choice == 'map':
            print("floor2 = ['sword', 'empty', 'stairs down', 'boss monster', 'prize']")
            print("floor1 = ['magic stones', 'stairs down', 'empty', 'monster1', 'stairs up']")
            print("floor0 = ['empty1', 'sword', 'stairs up', 'monster0', 'empty2']")

        else:
            print("That is an invalid choice, try again")
        # more code for each choice

print("the game loop was broken by 'quit'")

if game_state ==  'won':
    print('You won the game!! Congrats!!!')
else:
    print('You lost the game :/:/:/:/:/:/:/:/...... Maybe you can win next time. ')