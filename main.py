from datetime import datetime
from event import CalendarEvent
from notifications import notifications
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

nots = notifications()
events = CalendarEvent()

kwargs = events.createEvent("Test Event!", "PHONE MUM!!", "TestDate", "TestTime")

nots.buildNotification(kwargs)
