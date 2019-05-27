from api_wrapper import SFDataService

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
    sf_data_service = SFDataService()
    # truck_starting_at_index = 0
    current_date_time = get_current_date_time() # no
    print(f"(as of {current_date_time}")
    truck_collection = sf_data_service.get_open_food_truck_list()  # show first ten trucks
    for truck in truck_collection:
        print('\n')
        print(truck.name.upper())
        print(truck.day_open)
        print(truck.address)
        print(truck.start_time)
        print(truck.end_time)
    print('\n')
    user_input = input(
        'Would you like to see which other food trucks are open? (Y/N)').upper()
    print(user_input)
    # clear page - 10 at a time?
    if user_input == 'Y':
        # truck_starting_at_index += 10
        truck_collection = sf_data_service.get_open_food_truck_list()
        # print(truck_collection)
        if truck_collection and isinstance(truck_collection, list):
            for truck in truck_collection:
                print('\n')
                print(truck.name.upper())
                print(truck.day_open)
                print(truck.address)
                print(truck.start_time)
                print(truck.end_time)
        elif not truck_collection and isinstance(truck_collection, list):
            print('That\'s all for now. Goodbye!')
        else:
            raise Exception('Error!!!')
    elif user_input == 'N':
        print('Thanks for using our app. We predict deliciousness in your future.')
        print('Type Q to quit')
        # if user_input = q close program
        # else do_not_understand()
    else:
        # user typed a command we don't understand
        print('idk')

if __name__ == '__main__':
    show_user_interface()