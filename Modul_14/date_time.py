
from datetime import datetime

SEASONS = {'Summer': [6,7,8], 'Autumn': [9,10,11], 'Winter': [12,1,2], 'Spring': [3,4,5]}
Type_Day = {'Morning': [6,12], 'Day': [12,18], 'Evening': [18,24], 'Night': [0,6]}


class SuperDate(datetime):
    def __init__(self, year, month, day, time, *args, **kwargs):
        super(SuperDate, self).__init__(*args, **kwargs)
        self.year_in = year
        self.month_in = month
        self.day_in = day
        self.time_in = time
    def get_season(self):
        for key in SEASONS:
            if self.month_in in SEASONS[key]:
                return key
        return f'Месяц {self.month_in} не найден'
    def get_time_of_day(self):
        for key in Type_Day:
            if  Type_Day[key][0] <= self.time_in < Type_Day[key][1]:
                return key
        return f'Время {self.month_in} не определено'


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
