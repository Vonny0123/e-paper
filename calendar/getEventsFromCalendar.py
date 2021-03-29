import json
import datetime
import os
from dateutil.relativedelta import relativedelta

path = "/home/pi/code/calendar/"

with open(os.path.join(path, "calendarEventsFuture.json"), "r") as file:
    calendar = json.load(file)
    
event_list = []
with open(os.path.join(path, "eventsFull.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        event_list.append(",".join(line))
    file.write("\n".join(event_list))

event_list = []
with open(os.path.join(path, "eventsWeek.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        if (datetime.datetime.now() + datetime.timedelta(days=7)).date() > datetime.datetime.strptime(date, "%Y-%m-%d").date():   
            event_list.append(",".join(line))
    file.write("\n".join(event_list))
            
event_list = []
with open(os.path.join(path, "eventsMonth.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        if (datetime.datetime.now() + relativedelta(months=1)).date() > datetime.datetime.strptime(date, "%Y-%m-%d").date():   
            event_list.append(",".join(line))
    file.write("\n".join(event_list))