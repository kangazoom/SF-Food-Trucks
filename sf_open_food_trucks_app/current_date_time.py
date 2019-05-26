class CurrentDateTime:
    def __init__(self, now):
        self.now = now
        self.day_of_the_week = self.shift_week_start_num(now.isoweekday())
        self.hour = self.format_hour(now.hour)
        self.minute = self.format_minute(now.minute)

    def current_time_as_string(self):
        return '\'' + str(self.hour) + ':' + str(self.minute) + '\''

    # reformatting here? for endpoint?

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
        