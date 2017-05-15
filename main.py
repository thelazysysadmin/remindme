from datetime import datetime
from CalanderEvent import CalendarEvent
from notifications import notifications
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

nots = notifications()
events = CalendarEvent()

data = events.createEvent("Test Event!", "PHONE MUM!!", "TestDate", "TestTime")

nots.buildNotification(data)
