import json
import requests
import os
from dotenv import load_dotenv
from food_truck import FoodTruck
from date_time_manager import DateTimeManager

class SFDataService:
	def __init__(self):
		self.pagination_index = None
		self.timestamp = DateTimeManager() # record current date+time upon service creation

	# we will increase page index each time user views more trucks
	def increment_pagination(self):
		if self.pagination_index == None:
			self.pagination_index = 0
		else:
			self.pagination_index += 10

	# invokes pagination incrementer, request call, and response parser
	def get_open_food_truck_list(self):
		self.increment_pagination()
		response = self.fetch_food_truck_data()
		return self.parse_response(response)  # returns list of open food trucks as objects

	# loads and returns the app token we use with SF Data via dotenv module
	def get_app_token(self):
		load_dotenv()
		return os.environ.get('APP_TOKEN') or '' # leave blank if no app token exists

	def build_query_collection(self):
		app_token = self.get_app_token()
		attribute_list = 'applicant, location'
		output_length = str(10)
		start_from_index = str(self.pagination_index)
		day_of_week_num = self.timestamp.day_of_the_week # values 0 --> 6
		sort_alpha_by = 'applicant, location'
		time_boundary = (self.timestamp.format_current_time_as_string() + 
		 ' between start24 and end24')  # inclusive
		query_string = (
			'?' + '$$app_token=' + app_token
			+ '&' + '$select=' + attribute_list
			+ '&' + 'dayorder=' + day_of_week_num
			+ '&' + '$order=' + sort_alpha_by
			+ '&' + '$where=' + time_boundary
			+ '&' + '$limit=' + output_length
			+ '&' + '$offset=' + start_from_index
			)
		return query_string

	# send a GET request to the SF Data API via requests module
	def fetch_food_truck_data(self):
		base_url = 'https://data.sfgov.org/resource/jjew-r69b.json'
		query_string = self.build_query_collection()
		return requests.get(base_url + query_string)  # returns raw response as serialized json

	# deserialize request's serialized json response and extract data
	def parse_response(self, response):
		if response.status_code == 200:
			response = json.loads(response.text)
			open_food_truck_collection = []
			# assemble a list of open food trucks as objects
			for item in response:
				food_truck = FoodTruck(
					name=item['applicant'], 
					address=item['location']
					)
				open_food_truck_collection.append(food_truck)
		# treat all client- and server-side errors as empty data
		else:
			return []
		return open_food_truck_collection # returns empty list or list of open food truck objects
