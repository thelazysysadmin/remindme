class CalendarEvent:

    def __init__(self):

        self.eventTitle = None
        self.eventDescription = None
        self.eventTime = None
        self.eventDate = None

    def createEvent(self, eventTitle, eventDescription, eventDate, eventTime):
        self.eventTitle = eventTitle
        self.eventDescription = eventDescription
        self.eventDate = eventDate
        self.eventTime = eventTime

        return {'eventTitle': self.eventTitle, 'eventDescription': self.eventDescription, 'eventTime': self.eventTime, 'seventDate': self.eventDate}
