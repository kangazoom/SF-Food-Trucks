import requests

def get_open_food_truck_list():
    response = send_get_request()
    print(response.status_code)
    for _ in range(1, 11):
        print('1: FOOD TRUCK + ADDRESS')
    return parse_response(response)


def send_get_request():
    base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
    limit_query = str(20)
    response = requests.get(base_url + '?' + '$limit=' + limit_query)
    return response


def parse_response(response):
    return response.json()
