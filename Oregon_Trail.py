import random

name = input("Hello, what is your name? > ")

game_state = 'running'

miles_left = 2000
food_total = 500
health_player = 5
days_left = 305

time_travel = 0

current_day = 1
current_month = 3

months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
months_with_30_days = [2, 4, 6, 9, 11]

health_lost = 0

def add_day():
    global current_day
    global current_month
    global health_lost


    if current_month in months_with_31_days and current_day > 31:
        current_day -= 31
        current_month += 1
        health_lost = 0
    elif current_month in months_with_30_days and current_day > 30:
        current_day -= 31
        current_month += 1
        health_lost = 0
    elif current_month == 1:
        print("You ran out of time to get to Oregon, better luck next time.")
        game_state = 'not running'

def health_decrease():
    global health_player
    global current_day
    global health_lost

    if current_month in months_with_30_days and current_day == 15 and health_lost == 0: 
        health_player -= 1
        health_lost += 1
    elif current_month in months_with_30_days and current_day == 30 and health_lost == 1:
        health_player -= 1
        heatlh_lost = 0
    elif current_month in months_with_31_days and current_day == 15 and health_lost == 0: 
        health_player -= 1
        health_lost += 1
    elif current_month in months_with_31_days and current_day == 31 and health_lost == 1:
        health_player -= 1
        health_lost = 0

# making the player eat 5 lbs of food each day

def food_day():
    global current_day
    global food_total
    global time_travel
    if current_day > 0:
        food_total -= current_day * 5

##################################### ASK COACH GILPIN ABOUT THE FOOD DAY FUNCTION ################################################
        


# making the travel function
def travel():
    global miles_left
    global days_left
    global name
    global current_day
    print('You have chosen to travel.')
    travel_distance = random.randint(30, 60)
    time_travel = random.randint(3, 7)
    miles_left -= travel_distance
    days_left -= time_travel
    current_day += time_travel
    return time_travel 

# making the rest function
def rest():
    global health_player
    global days_left
    if health_player < 5:
        health_player += 1
        time_rest = random.randint(2, 5)
        days_left -= time_rest
        print("-----------------------------------------------------------------")
        print()
        print(f"You have chosen to rest, you now have {health_player} health, and {days_left} days left.")
        print()
        print("-----------------------------------------------------------------")
        return time_rest
        return days_left
    else: 
        health_player += 0
        print("You cannot heal at this time, choose a different action.")

#making the hunt function
def hunt():
    global food_total
    global days_left
    hunt_days = random.randint(2, 5)
    days_left -= hunt_days
    food_total += 100

#making the status function
def status():
    global food_total
    global health_player
    global miles_left
    global current_day
    global current_month
    print()
    print(f"You have {food_total} lbs of food, {health_player} amount of health, {miles_left} left, it is the {current_day} day of the {current_month} month of the year.")
    print()

# making the help function
def help():
    print("You can either type travel, rest, hunt, help, status or quit.")

#making the quit function
def quit():
    game_state = 'not running'


while game_state == 'running':

    choice = input(f"{name}, what would you like to do?(Type 'help' for a list of commands) > ")
    if choice == 't':
        print("-----------------------------------------------------------------")
        print()
        travel()
        print(f"{name}, you have {miles_left} miles and {days_left} days left unitl you get to Oregon!")
        print()
        print("-----------------------------------------------------------------")
    elif choice == 'help':
        help()
    elif choice == 'quit':
        quit()
        game_state = 'not running'
    elif choice == 'rest':
        rest()
    elif choice == 'hunt':
        hunt()
    elif choice == 'status':
        status()
    else:
        print("I don't know that command, plase choose a different one.")


    food_day()
    health_decrease()
    add_day()


if game_state == 'not running':
    print("You have chosen to quit the game, Thank you for playing Oregon Trail by Gavin Gunter!!!")
elif game_state == 'won':
    pass    