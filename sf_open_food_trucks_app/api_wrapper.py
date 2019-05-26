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


def fetch_food_truck_data():
    base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
    limit_query = str(20)
    response = requests.get(base_url + '?' + '$limit=' + limit_query)
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
            open_food_truck_object_collection.append(food_truck)
    return open_food_truck_object_collection
