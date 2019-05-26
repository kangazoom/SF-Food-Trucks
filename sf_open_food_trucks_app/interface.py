from api_wrapper import get_open_food_truck_list

def get_current_date_time():
    return '1/1/1970 00:00:00:00Z'


def handle_invalid_input():
    print('Your selection was invalid. Let\'s try again.')


def display_valid_input():
    # user_input =
    # if exist
    print('Type [Y] to see which other food trucks are open right now.')
    print('Type [N] if you do not want to view more food trucks.')  # if exist
    print('Type [Q] to quit this program.')


def handle_user_input(user_input):
    return


def show_user_interface():

    print('Welcome to the San Francisco Food Truck Finder!')
    print('\n')
    print('The following food trucks are currently open:')
    current_date_time = get_current_date_time()
    print(f"(as of {current_date_time}")
    get_open_food_truck_list()  # show first ten trucks
    print('\n')
    user_input = input(
        'Would you like to see which other food trucks are open? (Y/N)')
    print(user_input)
    if user_input == 'y'.upper():
        print(get_open_food_truck_list())  # show ten more trucks
        # if no more trucks to show print('That\'s all for now') end of the line
        # else show trucks
    elif user_input == 'n'.upper():
        print('Thanks for using our app. We predict deliciousness in your future.')
        print('Type Q to quit')
        # if user_input = q close program
        # else do_not_understand()
    else:
        # user typed a command we don't understand
        print('idk')

if __name__ == '__main__':
    show_user_interface()