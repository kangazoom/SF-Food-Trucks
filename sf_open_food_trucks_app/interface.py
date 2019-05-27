from sf_data_service import SFDataService
from display_text import (print_welcome_message, print_date_time_fetched, 
    print_valid_food_truck_list, print_empty_food_truck_list, print_at_end_of_food_truck_list, 
    print_invalid_input, quit_program, prompt_user_to_view_more_trucks)

def show_user_interface():
    prompt_user = True       
    print_welcome_message()
    sf_data_service = SFDataService()
    truck_collection = sf_data_service.get_open_food_truck_list()
    if isinstance(truck_collection, list) and truck_collection:
        print_date_time_fetched(sf_data_service.timestamp.date_time_in_pt)
        print_valid_food_truck_list(truck_collection) # show first ten trucks
    elif isinstance(truck_collection, list) and not truck_collection:
        print_empty_food_truck_list()
        prompt_user = False
    else:
        raise Exception('Bad format - Unable to print results')
    while prompt_user:
        user_input = input(prompt_user_to_view_more_trucks()).upper()
        if user_input == 'Y':
            print_date_time_fetched(sf_data_service.timestamp.date_time_in_pt)
            truck_collection = sf_data_service.get_open_food_truck_list()
            if isinstance(truck_collection, list) and truck_collection:
                print_valid_food_truck_list(truck_collection)
            elif isinstance(truck_collection, list) and not truck_collection:
                print_date_time_fetched
                print_at_end_of_food_truck_list()
                prompt_user = False
            else:
                raise Exception('Bad format - Unable to print results')
        elif user_input == 'N':
            prompt_user = False
        else:
            print_invalid_input()
    quit_program()

if __name__ == '__main__':
    show_user_interface()