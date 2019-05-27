from api_wrapper import SFDataService
import display_text

def show_user_interface():
    prompt_user = True       
    display_text.print_welcome_message()
    sf_data_service = SFDataService()
    truck_collection = sf_data_service.get_open_food_truck_list()
    if isinstance(truck_collection, list) and truck_collection:
        display_text.print_date_time_fetched(sf_data_service.date_time_fetched.now)
        display_text.print_valid_food_truck_list(truck_collection) # show first ten trucks
    elif isinstance(truck_collection, list) and not truck_collection:
        display_text.print_empty_food_truck_list()
        prompt_user = False
    else:
        raise Exception('Bad format - Unable to print results')
    while prompt_user:
        user_input = input(display_text.prompt_user_to_view_more_trucks()).upper()
        if user_input == 'Y':
            display_text.print_date_time_fetched(sf_data_service.date_time_fetched.now)
            truck_collection = sf_data_service.get_open_food_truck_list()
            if isinstance(truck_collection, list) and truck_collection:
                display_text.print_valid_food_truck_list(truck_collection)
            elif isinstance(truck_collection, list) and not truck_collection:
                display_text.print_date_time_fetched
                display_text.print_at_end_of_food_truck_list()
                prompt_user = False
            else:
                raise Exception('Bad format - Unable to print results')
        elif user_input == 'N':
            prompt_user = False
        else:
            display_text.print_invalid_input()
    display_text.quit_program()

if __name__ == '__main__':
    show_user_interface()