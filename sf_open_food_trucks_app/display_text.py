def print_welcome_message():
    print('\n')
    print('Welcome to the San Francisco Food Truck Finder!')
    print('We predict a most delicious meal in your future.')
    print('\n')

def print_invalid_input():
    print('\n')
    print('Sorry, your input was invalid.')
    print('Please try again.')

def prompt_user_to_view_more_trucks():
    return 'Would you like to see if even more food trucks are open? (Y/N) ' # this is used as input, so do not print()

def print_date_time_fetched(date_time):
    formatted_date_time = date_time.strftime("%A %B %d, %Y at %I:%M:%S %p")
    print(f"... Fetching data from: {formatted_date_time} local SF time ...")

def print_valid_food_truck_list(truck_collection):
    print('The following food trucks are currently open:')
    print('\n')
    for truck in truck_collection:
        print(truck.name.upper())
        print(truck.address.title())
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
