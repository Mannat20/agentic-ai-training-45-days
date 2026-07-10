class flight:
    def __init__(self,name,number,departure_time,departure_loc,duration,message,arrival_time,arrival_loc):
        self.name=name
        self.number=number
        self.departure_time=departure_time
        self.departure_loc=departure_loc
        self.duration=duration
        self.message=message
        self.arrival_time=arrival_time
        self.arrival_loc=arrival_loc
        self.next_flight=None
        self.previous_flight=None
        print('[flight] [LOG] __init__ constructor |ID | ',self)

    def show_flight(self):
        print('\n------------------')
        print('Name: ',self.name)
        print('Number: ',self.number)
        print('Depature_time: ',self.departure_time)
        print('departure_loc: ',self.departure_loc)
        print('duration: ',self.duration)
        print('message: ',self.message)
        print('arrival_time: ',self.arrival_time)
        print('arrival_loc: ',self.arrival_loc)
        print('Next Flight: ',self.next_flight)
        print('previous flight: ',self.previous_flight)
        print('Id: ',self)
        print('------------------')

    