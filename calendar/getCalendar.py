from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os
import json
from collections import defaultdict
import datetime


scopes = ['https://www.googleapis.com/auth/calendar']
path = "/home/pi/code/e-paper/calendar/"

try:
    credentials = pickle.load(open(os.path.join(path, "auth/token.pkl"), "rb"))
    service = build("calendar", "v3", credentials=credentials)
    print("success")
except Exception as e:
    print("old credentials not valid, need to authenticate")
    flow = InstalledAppFlow.from_client_secrets_file(os.path.join(path, "auth/client_secret.json"), scopes=scopes)
    credentials = flow.run_console()
    pickle.dump(credentials, open(os.path.join(path, "auth/token.pkl"), "wb"))
    service = build("calendar", "v3", credentials=credentials)
    
result = service.calendarList().list().execute()
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id).execute()


with open(os.path.join(path, "data/calendarEvents.json"), "w") as file:
    json.dump(result, file)
    
with open(os.path.join(path, "data/calendarEvents.json"), "r") as file:
    result = json.load(file)
    
item_list = []
for item in result['items']:
    try:
        item_date = datetime.datetime.strptime(item['start']['date'], "%Y-%m-%d").date()
    except:
        item_date = datetime.datetime.strptime(item['start']['dateTime'][:10], "%Y-%m-%d").date()
    
    today = datetime.datetime.now().date()
    event_in_future = today < item_date
    
    if event_in_future:
        item['item_date'] = item_date.strftime("%Y-%m-%d")
        item_list.append(item)
    else:
        try:
            if item['recurrence'][0] == "RRULE:FREQ=YEARLY":
                if datetime.datetime.now().date() < item_date.replace(year=today.year):
                    item['item_date'] = item_date.replace(year=today.year)
                else:
                    item['item_date'] = item_date.replace(year=today.year+1)
                item_list.append(item)
        except Exception as e:
            pass
        
def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

with open(os.path.join(path, "data/calendarEventsFuture.json"), "w") as file:
    json.dump(item_list, file, default=myconverter)
    