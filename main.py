from datetime import datetime
from CalanderEvent import CalendarEvent
from notifications import notifications


nots = notifications()
events = CalendarEvent()

data = events.createEvent("Test Event!", "PHONE MUM!!", "2017-05-16", "TestTime")


def schedule_event(data):
    current_date = datetime.now().strftime("%Y-%m-%d")
    event_date = data['eventDate']
    if current_date == event_date:
        return nots.spawn_notification(data)




schedule_event(data)



