import datetime
import json
import requests
from food_truck import FoodTruck
from current_date_time import CurrentDateTime

# make a class --> offset index for ex

def get_open_food_truck_list(offset_index):
    response = fetch_food_truck_data(offset_index)
    # print(response)
    print(response.status_code)
    return parse_response(response) # return parsed response

def build_query_collection(offset_index):
    # queries
    # select
    now = CurrentDateTime(datetime.datetime.now())
    output_length = str(10)
    start_from_index = str(offset_index)
    day_of_week_num = now.day_of_the_week
    sort_alpha_by = 'applicant'
    print(day_of_week_num)
    print(now.hour)
    print(now.minute)
    time_boundary = now.current_time_as_string() + ' between start24 and end24' # inclusive
    query_string = (
    '?' + '$limit=' + output_length
    + '&' + '$offset=' + start_from_index
    + '&' + 'dayorder=' + day_of_week_num
    + '&' + '$order=' + sort_alpha_by
    + '&' + '$where=' + time_boundary)
    return query_string

def fetch_food_truck_data(offset_index):
    base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
    query_string = build_query_collection(offset_index)
    return requests.get(base_url + query_string) # return raw response

def parse_response(response):
    if response.status_code == 200:
        # if []
        response = json.loads(response.text)
        open_food_truck_object_collection = []
        for item in response:
            food_truck = FoodTruck()
            food_truck.name = item['applicant']
            food_truck.address = item['location']
            food_truck.day_open = item['dayofweekstr']
            food_truck.start_time = item['start24']
            food_truck.end_time = item['end24']
            # print(food_truck.name)
            # print(food_truck.address)
            # print(food_truck.day_open)
            # print(food_truck.start_time)
            # print(food_truck.end_time)
            open_food_truck_object_collection.append(food_truck)
    return open_food_truck_object_collection # return list of open food trucks as objects
