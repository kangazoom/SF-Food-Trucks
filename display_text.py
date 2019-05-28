# below are various messages shown to the user, dictated by interface behavior

def print_welcome_message():
    print('\n')
    print('Welcome to the San Francisco Food Truck Finder!')
    print('We predict a most delicious meal in your future.')

def print_invalid_input():
    print('\n')
    print('Sorry, your input was invalid.')
    print('Please try again.')

# this text is used as user input prompt, so do not print()
def prompt_user_to_view_more_trucks():
    return 'Would you like to see if even more food trucks are open? (Y/N) '

# example formatted_date_time output: 'Sunday May 26, 2019 at 05:11:40 PM'
def print_date_time_fetched(date_time):
    formatted_date_time = date_time.strftime("%A %B %d, %Y at %I:%M:%S %p")
    print(f"(fetched above data from: {formatted_date_time} local SF time)")
    print('\n')

def print_valid_food_truck_list(truck_collection):
    print('\n')
    print('The following food trucks are currently open:')
    for truck in truck_collection:
        print(f'+ {truck.name.upper()}')
        print(f'  {truck.address.title()}')
        print('\n')

def print_empty_food_truck_list():
    print('\n')
    print('Drats! Nothing appears to be open at the moment.')
    print('Maybe you can reheat some old pizza?')

def print_at_end_of_food_truck_list():
    print('\n')
    print('We\'ve reached the end of the list.')

def quit_program():
    print('\n')
    print('Thanks for using our app. Hope you found some good food.')
    quit('This program is closing now. Goodbye!\n')
    print('\n')
