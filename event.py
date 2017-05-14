class CalendarEvent:

    def __init__(self):

        self.eventTitle = None
        self.eventDescription = None
        self.eventTime = None

    def createEvent(self, eventTitle, eventDescription, eventTime):
        self.eventTitle = eventTitle
        self.eventDescription = eventDescription
        self.eventTime = eventTime

        return {'eventTitle': self.eventTitle, 'eventDescription': self.eventDescription, 'eventTime': self.eventTime}



#cal = CalendarEvent()


#for k, v in cal.createEvent("Test", "Testing", "23:00").items():
    #print(v)
