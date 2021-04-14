#!/bin/bash

python3 /home/pi/code/e-paper/calendar/getCalendar.py
python3 /home/pi/code/e-paper/calendar/getEventsFromCalendar.py
python3 /home/pi/code/e-paper/calendar/eventsToBmp.py
python3 /home/pi/code/e-paper/calendar/BmpToDisplay.py

echo "Calendar Processes Complete!"

