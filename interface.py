from sf_data_service import SFDataService
from display_text import (print_welcome_message, print_date_time_fetched, 
    print_valid_food_truck_list, print_empty_food_truck_list, print_at_end_of_food_truck_list, 
    print_invalid_input, quit_program, prompt_user_to_view_more_trucks)

def show_user_interface():
    prompt_user = True # when False, skip to end of program
    print_welcome_message()
    sf_data_service = SFDataService() # initialize the api request service
    truck_collection = sf_data_service.get_open_food_truck_list()
    # use same time for all requests to minimize errors if db changes
    time_request_first_sent = sf_data_service.timestamp.date_time_in_pt
    # if we have a list of 1+ open food trucks, show up to the first ten trucks
    if isinstance(truck_collection, list) and truck_collection: 
        print_valid_food_truck_list(truck_collection)
    # if we have an empty list or invalid data, we let user know and skip to end of program
    else:
        print_empty_food_truck_list()
        prompt_user = False
    while prompt_user:
        print_date_time_fetched(time_request_first_sent)
        user_input = input(prompt_user_to_view_more_trucks()).upper()
        if user_input == 'Y':
            truck_collection = sf_data_service.get_open_food_truck_list()
            # if we have a list of 1+ open food trucks, show up to the next ten trucks
            if isinstance(truck_collection, list) and truck_collection:
                print_valid_food_truck_list(truck_collection)
            else:
                print_at_end_of_food_truck_list()
                prompt_user = False
        elif user_input == 'N':
            prompt_user = False
         # if user's input is invalid, continue prompting user until they enter 'Y' or 'N'
        else:
            print_invalid_input()
    quit_program() # end of program

if __name__ == '__main__':
    show_user_interface()