import datetime
import json
import requests
from food_truck import FoodTruck

def get_open_food_truck_list():
    response = fetch_food_truck_data()
    # print(response)
    print(response.status_code)
    # print(response.raw)
    # print(response.text)
    # print(response.value)
    # print(response.data)
    for _ in range(1, 11):
        print('1: FOOD TRUCK + ADDRESS')
    parse_response(response)

def current_date_time():
    now = datetime.datetime.now()
    # day_of_the_week = now.day
    # hour = now.hour
    # minute = now.minute
    # second = now.second
    # microsecondond = now.microsecond
    return now

def build_query_collection():
    # queries
    # select
    now = current_date_time()
    limit = str(20)
    day_of_week_num = str(now.isoweekday())
    sort_alpha_by = 'applicant'
    current_time_as_string = '\'' + str(now.hour) + ':' + str(now.minute) + '\''
    start_time_boundary = 'start24<=' +  current_time_as_string
    end_time_boundary = 'end24>=' +  current_time_as_string
    complete_time_boundary = start_time_boundary + ' and ' + end_time_boundary
    query_string = (
    '?' + '$limit=' + limit 
    + '&' + 'dayorder=' + day_of_week_num
    + '&' + '$order=' + sort_alpha_by
    + '&' + '$where=' + complete_time_boundary)
    return query_string
    
    


def fetch_food_truck_data():
    base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
    query_string = build_query_collection()
    response = requests.get(base_url + query_string)
    return response


def parse_response(response):
    if response.status_code == 200:
        response = json.loads(response.text)
        open_food_truck_object_collection = []
        for item in response:
            food_truck = FoodTruck()
            food_truck.name = item['applicant']
            food_truck.address = item['location']
            food_truck.day_open = item['dayofweekstr']
            food_truck.start_time = item['start24']
            food_truck.end_time = item['end24']
            print(food_truck.name)
            print(food_truck.address)
            print(food_truck.day_open)
            print(food_truck.start_time)
            print(food_truck.end_time)
            open_food_truck_object_collection.append(food_truck)
    return open_food_truck_object_collection
