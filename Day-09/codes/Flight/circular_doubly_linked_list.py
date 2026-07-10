class list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add(self,flight):
        self.size += 1
        if self.head==None:
            self.head=flight
            self.tail=flight
        else:
            self.tail.next_flight=flight
            self.head.previous_flight=flight
            flight.previous_flight=self.tail
            flight.next_flight=self.head
            self.tail=flight

    def show(self,traverse=True):
        if traverse == True:
            flight=self.head
            while True:
                flight.show_flight()
                flight=flight.next_flight

                if flight == self.head:
                    break
        else:
            flight=self.tail
            while True:
                flight.show_flight()
                flight=flight.previous_flight

                if flight== self.tail:
                    break

    
    def add_in_front(self,flight):
        self.size += 1
        if self.head==None:
            self.head=flight
            self.tail=flight
        else:
            flight.next_flight=self.head
            flight.previous_flight=self.tail
            self.head.previous_flight=flight
            self.tail.next_flight=flight
            self.head=flight

    def add_in_between(self,flight,flight1,flight2):
        self.size += 1
        flight1.next_flight=flight
        flight.previous_flight=flight1
        flight2.previous_flight=flight
        flight.next_flight=flight2
    
    def delete_last(self):

        if self.size==1:
            self.head=None
            self.tail=None
            self.size -=1
        else:
            self.head.previous_flight=self.tail.previous_flight
            self.tail=self.tail.previous_flight
            self.tail.next_flight=self.head
            self.size -=1


            
    def delete_front(self):
        if self.size==1:
            self.head=None
            self.tail=None
            self.size -=1
        else:
            self.tail.next_flight=self.head.next_flight
            self.head=self.head.next_flight
            self.head.previous_flight=self.tail
            self.size -= 1

    def delete(self,flight):
        if self.size==1:
            self.head=None
            self.tail=None
            self.size -=1
        elif flight==self.head:
            self.delete_front()
        elif flight==self.tail:
            self.delete_last()
        else:
            flight.previous_flight=flight.next_flight
            flight.next_flight=flight.previous_flight
            self.size -=1
            