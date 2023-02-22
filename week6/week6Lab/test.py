from datetime import datetime

dt =  1677013200

timestamp = datetime.fromtimestamp(dt)

dateAndTime = timestamp.strftime('%m/%d/%Y %H')
date_time_list = dateAndTime.split(' ')
hour = date_time_list[1]
am_or_pm = 'AM'
if int(hour) >= 12:
    am_or_pm = 'PM'

print(f'{dateAndTime}{am_or_pm}')