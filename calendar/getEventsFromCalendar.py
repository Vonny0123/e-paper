import json
import datetime
import os
from dateutil.relativedelta import relativedelta

path = "/home/pi/code/e-paper/calendar/"

with open(os.path.join(path, "data/calendarEventsFuture.json"), "r") as file:
    calendar = json.load(file)
    
event_list = []
with open(os.path.join(path, "data/eventsFull.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        event_list.append(" - ".join(line))
    event_list = sorted(event_list, key=lambda x: datetime.datetime.strptime(x[:10], "%Y-%m-%d"))
    event_list = [datetime.datetime.strptime(event[:10], '%Y-%m-%d').strftime('%d %b') + event[10:] for event in event_list]
    file.write("\n".join(event_list))

event_list = []
with open(os.path.join(path, "data/eventsWeek.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        if (datetime.datetime.now() + datetime.timedelta(days=7)).date() > datetime.datetime.strptime(date, "%Y-%m-%d").date():   
            event_list.append(" - ".join(line))
    file.write("\n".join(event_list))
            
event_list = []
with open(os.path.join(path, "data/eventsMonth.txt"), "w") as file:
    for event in calendar:
        date = event['item_date']
        event_name = event['summary']
        line = [date, event_name]
        if (datetime.datetime.now() + relativedelta(months=1)).date() > datetime.datetime.strptime(date, "%Y-%m-%d").date():   
            event_list.append(" - ".join(line))
    file.write("\n".join(event_list))