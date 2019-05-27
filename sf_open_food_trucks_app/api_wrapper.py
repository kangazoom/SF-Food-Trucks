import datetime
import json
import requests
from dotenv import load_dotenv
import os
from food_truck import FoodTruck
from current_date_time import CurrentDateTime

# make a class --> offset index for ex - for wrapper and/or for query
# add token .env or ''
# pagination place-keeping
# duplicates in name but not location
# 2nd sort by location?
# string methods?
# tests


class SFDataService:
	def __init__(self):
		self.pagination_index = None

	def get_open_food_truck_list(self):
		self.increment_pagination()
		response = self.fetch_food_truck_data()
		print(response.status_code)
		return self.parse_response(response)  # return parsed response

	def get_app_token(self):
		load_dotenv()
		return os.environ.get('APP_TOKEN') or ''
	
	def increment_pagination(self):
		if self.pagination_index == None:
			self.pagination_index = 0
		else:
			self.pagination_index += 10

	def build_query_collection(self):
		# queries
		# select
		now = CurrentDateTime(datetime.datetime.now())
		app_token = self.get_app_token()
		attribute_list = 'applicant, location, dayofweekstr, start24, end24'
		output_length = str(10)
		start_from_index = str(self.pagination_index)
		day_of_week_num = now.day_of_the_week
		sort_alpha_by = 'applicant, location'
		print(day_of_week_num)
		print(now.hour)
		print(now.minute)
		time_boundary = now.current_time_as_string(
		) + ' between start24 and end24'  # inclusive
		query_string = (
			'?' + '$$app_token=' + app_token
			+ '&' + '$select=' + attribute_list
			+ '&' + 'dayorder=' + day_of_week_num
			+ '&' + '$order=' + sort_alpha_by
			+ '&' + '$where=' + time_boundary
			+ '&' + '$limit=' + output_length
			+ '&' + '$offset=' + start_from_index)
		return query_string


	def fetch_food_truck_data(self):
		base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
		query_string = self.build_query_collection()
		return requests.get(base_url + query_string)  # return raw response


	def parse_response(self, response):
		if response.status_code == 200:
			# if []
			response = json.loads(response.text)
			print(response[0])
			open_food_truck_object_collection = []
			for item in response:
				food_truck = FoodTruck()
				food_truck.name = item['applicant']
				food_truck.address = item['location']
				food_truck.day_open = item['dayofweekstr']  # TODO: remove
				food_truck.start_time = item['start24']  # TODO: remove
				food_truck.end_time = item['end24']  # TODO: remove
				open_food_truck_object_collection.append(food_truck)
		# return list of open food trucks as objects
		return open_food_truck_object_collection
