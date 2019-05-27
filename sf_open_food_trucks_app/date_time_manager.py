from datetime import datetime
from pytz import timezone

class DateTimeManager:
    def __init__(self):
        self.now = datetime.now()
        self.date_time_in_pt = self.standardize_to_pt_time(datetime.now())
        self.day_of_the_week = self.shift_week_start_num(self.date_time_in_pt.isoweekday())
        self.hour = self.format_hour(self.date_time_in_pt.hour)
        self.minute = self.format_minute(self.date_time_in_pt.minute)

    def standardize_to_pt_time(self, date_time):
        return date_time.astimezone(timezone('US/Pacific'))

    def format_current_time_as_string(self):
        return '\'' + str(self.hour) + ':' + str(self.minute) + '\''

    def shift_week_start_num(self, weekday_num): # start the week on Sunday, not Monday + use ordinal counting
        weekday_num = str(weekday_num)
        if weekday_num == '7': return '0'
        else: return weekday_num

    def format_hour(self, hour):
        hour = str(hour)
        if len(hour) < 2: return '0' + hour
        else: return hour

    def format_minute(self, minute):
        minute = str(minute)
        if len(minute) < 2: return '0' + minute
        else: return minute
        
